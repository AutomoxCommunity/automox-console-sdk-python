import automox_console_sdk as automox
from automox_console_sdk.api import DevicesApi
from automox_console_sdk.api import GroupsApi
from automox_console_sdk.models import ServersIdBody, ServerGroupCreateOrUpdateRequest
import csv
from getpass import getpass
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
            hostname_map[d.name] = d

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


def check_csv_headers(csv_file, field_list):
    with open(csv_file, 'r') as fh:
        reader = csv.DictReader(fh, skipinitialspace=True)

        dict_from_csv = dict(list(reader)[0])

        for field in field_list:
            if field not in dict_from_csv:
                exit(f"ERROR: {field} is not a header value in {csv_file}")


if __name__ == '__main__':
    # Prompt for inputs
    # API Key
    api_key = os.getenv('AUTOMOX_API_KEY') or getpass("Enter your API Key: ")
    # Org ID
    org_id = int(os.getenv('AUTOMOX_ORGANIZATION_ID') or input("Enter your Organization ID: "))
    # Location of CSV
    csv_location = input("Enter the location of the CSV: ") or exit("ERROR: Must provide location to csv file")
    # Field for Hostname
    hn_field = input("Enter the CSV field for Hostname (default: hostname): ") or "hostname"
    # Field for IP Address
    ip_field = input("Enter the CSV field for IP Address (default: ip_address): ") or "ip_address"
    # Field for group
    group_field = input("Enter the CSV field to map to the Automox Server Group: ")
    # Field(s) for tags
    tag_fields = input("Enter the comma separated CSV field names to map to Automox device tags: ").split(',')

    # Check if provided inputs are valid headers in CSV
    check_csv_headers(csv_location, [hn_field, ip_field, group_field] + tag_fields)

    config = automox.Configuration()
    client = automox.ApiClient(configuration=config)
    client.default_headers['Authorization'] = f"Bearer {api_key}"

    devices_api = DevicesApi(client)
    groups_api = GroupsApi(client)

    # Add devices to dict for quick lookup by ip/hostname
    device_hostname_map, device_ip_map = map_automox_devices(devices_api)

    # Get all groups
    groups, default_server_group_id = get_automox_groups(groups_api)

    # Iterate CSV
    with open(csv_location, 'r') as fh:
        reader = csv.DictReader(fh, skipinitialspace=True)
        for row in reader:
            device = None
            # Check by hostname first
            if hn_field and row[hn_field] in device_hostname_map:
                device = device_hostname_map.get(row[hn_field], None)
            # Check for device by ip as fallback
            elif ip_field and row[ip_field] in device_ip_map:
                device = device_ip_map.get(row[ip_field], None)

            # Device found, update based on CSV values
            if device:
                tags = [row[tf] for tf in tag_fields if row.get(tf, None)]

                group_name = row[group_field] if group_field in row else "Default"
                group = next((g for g in groups if g.name == row[group_field]), None)

                # Create group if it doesn't exist yet
                if group is None:
                    g = ServerGroupCreateOrUpdateRequest(name=row[group_field], refresh_interval=1440,
                                                         parent_server_group_id=default_server_group_id,
                                                         ui_color="#FFFF00")
                    try:
                        group = groups_api.create_server_group(o=org_id, body=g)
                        groups.append(group)
                        print(f"Successfully created Group ID {group.id} ({row[group_field]})")
                    except Exception as e:
                        print(f"Failed to created group [{row[group_field]}]: {e}")

                server_update = ServersIdBody(server_group_id=group.id, exception=device.exception, tags=tags)
                try:
                    update_result = devices_api.update_device(o=org_id, id=device.id, body=server_update)
                    print(f"Successfully updated Device ID {device.id} ({row[hn_field]}, {row[ip_field]})")
                except Exception as e:
                    print(f"Failed to update Device ID {device.id} ({row[hn_field]}, {row[ip_field]}): {e}")
            else:
                print(f"No device matching hostname [{row[hn_field]}] or ip address [{row[ip_field]}]")
