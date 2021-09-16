# Update Automox Devices by CSV
In order to improve the efficiency and administration of Automox devices, it is possible to leverage a CSV source file and the provided script for the grouping and tagging of Automox devices.  By grouping devices, it makes it that much easier to search for devices, leverage reporting filtering, and scope policies. This script shows how to leverage the Automox Console SDK to:
1. Pull Automox Devices
2. Pull Automox Groups; identifying the default group
3. Process a CSV by mapping the provided hostname and IP address of each row
4. Update the matched Automox device by hostname or IP address with the defined field values

An example CSV is included with columns denoting the `hostname`, `ip_address`, `group`, `location`, and `environment` 
fields. This CSV is simply used as an example and the columns can be updated to reflect your environment needs.

## Running the Script
To run the script, first make sure Python 3 is installed on the host system and clone this repository locally then 
follow the below steps:
1. Create a virtual environment: `python3 -m venv venv`
2. Source virtual environment: `source venv/bin/activate`
3. Install the Automox Console SDK: `pip install automox-console-sdk`
4. Navigate to the script directory: `cd examples/use-cases/update_devices_by_csv`   
4. Run the scripts: `python update_devices_by_csv.py`

This will execute the script and prompt for inputs. Validation will be performed to ensure there 
are alerts for improper input(s) if encountered.

Both the API Key and Organization ID inputs can be defined as environment variables prior to running the script to avoid
continual prompting. This can be accomplished by exporting the AUTOMOX_API_KEY and AUTOMOX_ORGANIZATION_ID environment 
variables:
```shell
AUTOMOX_API_KEY=<API KEY HERE> AUTOMOX_ORGANIZATION_ID=<ORG ID HERE> python update_devices_by_csv.py
```

## Script Prompts
When the script is run, the user will be prompted for a handful of inputs. These inputs define:
1. The location of the CSV to be processed (relative or absolute paths allowed)
2. The column name used for matching on device hostname 
3. The column name used for matching on device IP address
4. The column name used for the expected device group
5. Comma separated list of column names used for the expected device tags 

```shell
Enter your API Key: 
Enter your Organization ID: 1234
Enter the location of the CSV: ./sample.csv
Enter the CSV field for Hostname: hostname
Enter the CSV field for IP Address: ip_address
Enter the CSV field to map to the Automox Server Group: group
Enter the comma separated CSV field names to map to Automox device tags: location,environment
```

## Script Output
When running the script, output will be sent to standard out in the case of an input issue, errors, or informational 
messages. This output could be redirected to a file for storing on disk as needed.