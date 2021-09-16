import automox_console_sdk as automox
from automox_console_sdk.api import DevicesApi
from automox_console_sdk.api import GroupsApi
from automox_console_sdk.models import ServersIdBody, ServerGroupCreateOrUpdateRequest
from getpass import getpass
import ldap
from ldap.controls import SimplePagedResultsControl
import re
import os


def map_automox_devices(d_api):
    hostname_map, ip_map = {}, {}
    page = 0

    while True:
        devices_page = d_api.get_devices(o=org_id, limit=500, page=page)

        # All devices retrieved once no more are returned
        if len(devices_page) == 0:
            break

        for d in devices_page:
            hostname_map[d.name.lower()] = d

            # Iterate IP address
            for ip in d.ip_addrs:
                ip_map[ip] = d
        page += 1

    return hostname_map, ip_map


def get_automox_groups(g_api):
    group_list = []
    default_group_id = 0
    page = 0
    while True:
        groups_page = g_api.get_server_groups(o=org_id, limit=500, page=page)

        if len(groups_page) == 0:
            break

        for g in groups_page:
            if not g.name:
                default_group_id = g.id
            group_list.append(g)

        page += 1

    return group_list, default_group_id


def get_ou_from_dn(dn):
    exploded_dn = ldap.dn.explode_dn(dn, flags=ldap.DN_FORMAT_LDAPV2)
    parent_ou = ','.join(exploded_dn[1:])

    return(parent_ou)


if __name__ == '__main__':
    # Prompt for inputs
    # API Key
    api_key = os.getenv('AUTOMOX_API_KEY') or getpass("Enter your API Key: ")
    # Org ID
    org_id = int(os.getenv('AUTOMOX_ORGANIZATION_ID') or input("Enter your Organization ID: "))
    # LDAP/AD Details
    ldap_url = os.getenv('LDAP_URL') or input("Enter your LDAP Bind URL (eg ldap://domain-controller:389): ")
    ldap_user = os.getenv('LDAP_USER') or input("Enter your LDAP Bind User: ")
    ldap_password = os.getenv('LDAP_PASSWORD') or getpass("Enter your LDAP Bind Password: ")
    ldap_base = os.getenv('LDAP_BASE') or input("Enter your LDAP base for computers (eg dc=example, dc=com): ")
    # Computer query/filter
    ldap_computer_filter = os.getenv('LDAP_COMPUTER_FILTER') or \
                           input("Enter your LDAP Computer Filter (default: (&(objectClass=computer))") or \
                           "(&(objectClass=computer))"
    # Attribute for hostname comparison
    hn_attribute = input("Enter the LDAP/AD computer field for hostname comparison (default: name): ") or "name"
    # Attribute for FQDN Address comparison
    fqdn_attribute = input("Enter the LDAP/AD computer attribute for FQDN comparison (default: dnsHostName): ") or "dnsHostName"
    # Attributes for tagging
    tag_attributes = input("Enter a comma separated list of LDAP/AD computer attributes used for tagging devices: ")
    tag_attributes = tag_attributes.split(',')
    tag_prefix = 'AD-'

    ldap_attributes = [hn_attribute, fqdn_attribute] + tag_attributes
    counter_created_groups, counter_matched_devices, counter_unmatched_devices = 0, 0, 0

    config = automox.Configuration()
    client = automox.ApiClient(configuration=config)
    client.default_headers['Authorization'] = f"Bearer {api_key}"

    devices_api = DevicesApi(client)
    groups_api = GroupsApi(client)

    # Add devices to dict for quick lookup by ip/hostname
    device_hostname_map, device_ip_map = map_automox_devices(devices_api)

    # Get all groups
    groups, default_server_group_id = get_automox_groups(groups_api)

    # Pull computers from LDAP/Active Directory
    connect = ldap.initialize(ldap_url)
    try:
        connect.protocol_version = ldap.VERSION3
        connect.set_option(ldap.OPT_REFERRALS, 0)

        bind = connect.simple_bind_s(ldap_user, ldap_password)
    except Exception as e:
        exit(f"Failed to connect to {ldap_url}: {e}")

    page_control = SimplePagedResultsControl(True, size=1, cookie='')

    while True:
        # Page LDAP Query
        response = connect.search_ext(base=ldap_base,
                                      scope=ldap.SCOPE_SUBTREE,
                                      filterstr=ldap_computer_filter,
                                      attrlist=ldap_attributes,
                                      serverctrls=[page_control])

        rtype, ldap_devices, rmsgid, serverctrls = connect.result3(response)

        # Process devices returned by LDAP/AD
        for device_dn, d in ldap_devices:
            if device_dn is None:
                continue

            device = None
            try:
                device_hostname = d[hn_attribute][0].decode("utf-8").lower()
            except Exception:
                device_hostname = None
            try:
                device_fqdn = d.get(fqdn_attribute)[0].decode("utf-8")
            except Exception:
                device_fqdn = None
            # Check by hostname first
            if device_hostname and device_hostname in device_hostname_map:
                device = device_hostname_map.get(device_hostname, None)
            # Check for device by ip as fallback
            elif device_fqdn and device_fqdn in device_ip_map:
                device = device_ip_map.get(device_fqdn, None)

            # Device found, update group based on ServiceNow field value
            if device:
                # Pull group value based on DN of computer
                group_value = get_ou_from_dn(device_dn)
                # Trim to max group name limit
                group_value = group_value[:44]

                group = next((g for g in groups if g.name == group_value), None)

                # Gather current device tags not prefixed with AD-
                tags = set()
                for t in device.tags:
                    if not t.startswith(tag_prefix):
                        tags.add(t)
                managed_tags = set()
                for ta in tag_attributes:
                    tag_value = d.get(ta)
                    if tag_value is not None:
                        managed_tags.add(f"{tag_prefix}-{ta}-{tag_value[0].decode('utf-8')}")
                tags.update(managed_tags)

                # Create group if it doesn't exist yet
                if group is None:
                    g = ServerGroupCreateOrUpdateRequest(name=group_value, refresh_interval=1440,
                                                         parent_server_group_id=default_server_group_id,
                                                         ui_color="#FFFF00")
                    try:
                        group = groups_api.create_server_group(o=org_id, body=g)
                        groups.append(group)
                        print(f"Successfully created Group ID {group.id} ({group_value})")
                        counter_created_groups += 1
                    except Exception as e:
                        print(f"Failed to created group [{group_value}]: {e}")

                server_update = ServersIdBody(server_group_id=group.id, exception=device.exception, tags=list(tags))
                try:
                    update_result = devices_api.update_device(o=org_id, id=device.id, body=server_update)
                    print(f"Successfully updated Device ID {device.id} ({device_hostname}, {device_fqdn})")
                    counter_matched_devices += 1
                except Exception as e:
                    print(f"Failed to update Device ID {device.id} ({device_hostname}, {device_fqdn}): {e}")
            else:
                #print(f"No device matching hostname [{device_hostname}] or fqdn [{device_fqdn}]")
                counter_unmatched_devices += 1

        # Should we page again
        controls = [control for control in serverctrls
                    if control.controlType == SimplePagedResultsControl.controlType]
        if not controls:
            print('The server ignores RFC 2696 control')
            break
        if not controls[0].cookie:
            break
        page_control.cookie = controls[0].cookie

    print(f"Script complete; matched devices: {counter_matched_devices}, unmatched devices: "
          f"{counter_unmatched_devices}, groups created: {counter_created_groups}")
