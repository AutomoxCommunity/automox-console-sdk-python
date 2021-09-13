# Group Automox Devices by ServiceNow CMDB
For organization leveraging ServiceNow CMDB, it is frequently seen as the source of truth for tagging and grouping 
devices within an environment. To ease grouping Automox devices based on a ServiceNow environment, this script can be
leveraged in order to:
1. Pull Automox Devices
2. Pull Automox Groups; identifying the default group
3. Pull ServiceNow CMDB Computers/Devices by mapping the provided hostname and IP address of each CI record
4. Update the matched Automox device by hostname or IP address with the defined group value to be pulled from the 
   ServiceNow response

In an unmodified ServiceNow instance, the hostname field for comparison is `name`, the IP address field for comparison 
is `ip_address`, and the `asset_tag` or `support_broup` fields can easily be leveraged for grouping needs.

## Running the Script
To run the script, first make sure Python 3 is installed on the host system and clone this repository locally then 
follow the below steps:
1. Create a virtual environment: `python3 -m venv venv`
2. Source virtual environment: `source venv/bin/activate`
3. Install the Automox Console SDK and requests library: `pip install automox-console-sdk requests`
4. Navigate to the script directory: `cd examples/use-cases/group_devices_by_servicenow_cmdb`   
4. Run the scripts: `python group_devices_by_servicenow_cmdb.py`

This will execute the script and prompt for inputs. Validation will be performed to ensure there 
are alerts for improper input(s) if encountered.

Both the Automox API Key and Organization ID inputs can be defined as environment variables prior to running the script 
to avoid continual prompting. This can be accomplished by exporting the AUTOMOX_API_KEY and AUTOMOX_ORGANIZATION_ID environment 
variables:
```shell
AUTOMOX_API_KEY=<API KEY HERE> AUTOMOX_ORGANIZATION_ID=<ORG ID HERE> python update_devices_by_csv.py
```

In addition, it is possible to set the `SERVICENOW_INSTANCE_NAME`, `SERVICENOW_USERNAME`, and `SERVICENOW_PASSWORD` 
environment variables to define the necessary ServiceNow details.

## Script Prompts
When the script is run, the user will be prompted for a handful of inputs. These inputs define:
1. The ServiceNow CMDB table to be used (default: cmdb_ci_computer)
2. The field name used for matching on device hostname (default: name)
3. The field name used for matching on device IP address (default: ip_address)
4. The field name used for pulling the group value (default: support_group)

```shell
Enter the ServiceNow CMDB Table for pulling devices (default: cmdb_ci_computer): 
Enter the ServiceNow CMDB field for Hostname (default: name): name
Enter the ServiceNow CMDB field for IP Address (default: ip_address): ip_address
Enter the ServiceNow CMDB field to map to the Automox Server Group (default: support_group): support_group
```

## Script Output
When running the script, output will be sent to standard out in the case of an input issue, errors, or informational 
messages. This output could be redirected to a file for storing on disk as needed. To avoid verbose output, the script 
is not currently outputing unmatched devices; however, a counter message is provided when the script completes to give a
overview of what occurred:
```
Successfully updated Device ID 1234 (hostname-1, 192.168.0.1)
Successfully updated Device ID 5678 (hostname-2, )
Script complete; matched devices: 2, unmatched devices: 855, groups created: 0
```