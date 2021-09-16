import automox_console_sdk as automox
from automox_console_sdk.api import DevicesApi
from automox_console_sdk.api import GroupsApi
from automox_console_sdk.models import ServersIdBody, ServerGroupCreateOrUpdateRequest
from getpass import getpass
import os
import requests


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


def get_servicenow_cmdb_devices(instance, username, password, table, o, l, query, fields):
    url = f"https://{instance}.service-now.com/api/now/table/{table}"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    try:
        r = requests.get(url, auth=(username, password), headers=headers,
                         params={'sysparm_query': query, 'sysparm_offset': o, 'sysparm_limit': l,
                                 'sysparm_display_value': 'true',
                                 'sysparm_fields': fields})
        r.raise_for_status()
    except Exception as e:
        exit(f"ServiceNow request failed to {url} page [{offset: o}]: {e}")

    try:
        response_json = r.json()
    except requests.exceptions.JSONDecodeError as jde:
        exit(f"Failed to parse response from ServiceNow: {jde}")

    return response_json.get('result', [])


if __name__ == '__main__':
    # Prompt for inputs
    # API Key
    api_key = os.getenv('AUTOMOX_API_KEY') or getpass("Enter your API Key: ")
    # Org ID
    org_id = int(os.getenv('AUTOMOX_ORGANIZATION_ID') or input("Enter your Organization ID: "))
    # ServiceNow Details
    servicenow_instance = os.getenv('SERVICENOW_INSTANCE_NAME') or input(
        "Enter your ServiceNow Instance Name (eg dev1234): ")
    servicenow_username = os.getenv('SERVICENOW_USERNAME') or input("Enter your ServiceNow Username: ")
    servicenow_password = os.getenv('SERVICENOW_PASSWORD') or getpass("Enter your ServiceNow Password: ")
    # Field for Hostname
    servicenow_table = input("Enter the ServiceNow CMDB Table for pulling devices (default: cmdb_ci_computer): ") or "cmdb_ci_computer"
    # Field for Hostname
    hn_field = input("Enter the ServiceNow CMDB field for Hostname (default: name): ") or "name"
    # Field for IP Address
    ip_field = input("Enter the ServiceNow CMDB field for IP Address (default: ip_address): ") or "ip_address"
    # Field for group
    group_field = input("Enter the ServiceNow CMDB field to map to the Automox Server Group (default: support_group): ") or "support_group"

    config = automox.Configuration()
    client = automox.ApiClient(configuration=config)
    client.default_headers['Authorization'] = f"Bearer {api_key}"

    devices_api = DevicesApi(client)
    groups_api = GroupsApi(client)

    # Add devices to dict for quick lookup by ip/hostname
    device_hostname_map, device_ip_map = map_automox_devices(devices_api)

    # Get all groups
    groups, default_server_group_id = get_automox_groups(groups_api)

    # Pull devices from ServiceNow CMDB
    offset, limit = 0, 1000
    fields = f"{hn_field},{ip_field},{group_field}"
    counter_created_groups, counter_matched_devices, counter_unmatched_devices = 0, 0, 0
    while True:
        servicenow_devices = get_servicenow_cmdb_devices(servicenow_instance,
                                                         servicenow_username,
                                                         servicenow_password,
                                                         servicenow_table,
                                                         offset,
                                                         limit,
                                                         "active=true",
                                                         fields)

        if len(servicenow_devices) == 0:
            break

        # Process devices returned by ServiceNow
        for d in servicenow_devices:
            device = None
            # Check by hostname first
            if hn_field and d[hn_field].lower() in device_hostname_map:
                device = device_hostname_map.get(d[hn_field].lower(), None)
            # Check for device by ip as fallback
            elif ip_field and d[ip_field] in device_ip_map:
                device = device_ip_map.get(d[ip_field], None)

            # Device found, update group based on ServiceNow field value
            if device:
                servicenow_group_value = d[group_field] if group_field in d else "Default"

                # If returned value is a dict, must pull display_value
                if isinstance(servicenow_group_value, dict):
                    servicenow_group_value = servicenow_group_value['display_value']

                group = next((g for g in groups if g.name == servicenow_group_value), None)

                # Create group if it doesn't exist yet
                if group is None:
                    g = ServerGroupCreateOrUpdateRequest(name=servicenow_group_value, refresh_interval=1440,
                                                         parent_server_group_id=default_server_group_id,
                                                         ui_color="#FFFF00")
                    try:
                        group = groups_api.create_server_group(o=org_id, body=g)
                        groups.append(group)
                        print(f"Successfully created Group ID {group.id} ({servicenow_group_value})")
                        counter_created_groups += 1
                    except Exception as e:
                        print(f"Failed to created group [{servicenow_group_value}]: {e}")

                server_update = ServersIdBody(server_group_id=group.id, exception=device.exception, tags=device.tags)
                try:
                    update_result = devices_api.update_device(o=org_id, id=device.id, body=server_update)
                    print(f"Successfully updated Device ID {device.id} ({d[hn_field]}, {d[ip_field]})")
                    counter_matched_devices += 1
                except Exception as e:
                    print(f"Failed to update Device ID {device.id} ({d[hn_field]}, {d[ip_field]}): {e}")
            else:
                # print(f"No device matching hostname [{d[hn_field]}] or ip address [{d[ip_field]}]")
                counter_unmatched_devices += 1

        offset += limit

    print(f"Script complete; matched devices: {counter_matched_devices}, unmatched devices: "
          f"{counter_unmatched_devices}, groups created: {counter_created_groups}")
