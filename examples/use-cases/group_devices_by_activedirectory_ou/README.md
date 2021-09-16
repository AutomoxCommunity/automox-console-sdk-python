# Group Automox Devices by Active Directory/LDAP OU
The Group Devices by Active Directory OU script is a quick way for teams to leverage Active Directory (or any
other LDAPv3 compatible directory service storing computer details) to:
1. Group Automox devices based on Computer Organizational Unit (OU)
2. Tag Automox devices with Active Directory Computer attributes
   
This script facilitates the following process when run:
1. Pull Automox Devices
2. Pull Automox Groups; identifying the default group
3. Pull Active Directory/LDAP Computers and retrieving the hostname, FQDN, distinguishedName, and (optional) attributes 
   used for tagging a device
4. Update the matched Automox device by hostname or FQDN with the device parent Organizational Unit along with tags
   for any additionally defined AD computer attributes

In a default Active Directory environment, the hostname field for comparison is `name` and the FQDN attribute for 
comparison is `dnsHostName`. When a comma separated list of attributes used for tagging devices is provided, the script
will update devices with Active Directory provided tag values prefixed with `AD-`. This ensures manually defined tags 
are not overwritten when the script is run.

Please not, when creating new Device groups in Automox based off computer OUs, the script will truncate
the name of the group to 44 characters.

## Running the Script
To run the script, first make sure Python 3 is installed on the host system and clone this repository locally then 
follow the below steps:
1. Create a virtual environment: `python3 -m venv venv`
2. Source virtual environment: `source venv/bin/activate`
3. Install the Automox Console SDK and python-ldap library: `pip install automox-console-sdk python-ldap`
4. Navigate to the script directory: `cd examples/use-cases/group_devices_by_activedirectory_ou`   
4. Run the scripts: `python group_devices_by_activedirectory_ou.py`

This will execute the script and prompt for inputs. Validation will be performed to ensure there are alerts for improper 
input(s) if encountered.

Both the Automox API Key and Organization ID inputs can be defined as environment variables prior to running the script 
to avoid continual prompting. This can be accomplished by exporting the AUTOMOX_API_KEY and AUTOMOX_ORGANIZATION_ID environment 
variables:
```shell
AUTOMOX_API_KEY=<API KEY HERE> AUTOMOX_ORGANIZATION_ID=<ORG ID HERE> python group_devices_by_activedirectory_ou.py
```

In addition, it is possible to set the following environment variables for defining Active Directory/LDAP 
configurations:
- `LDAP_URL` 
- `LDAP_USER`
- `LDAP_PASSWORD`
- `LDAP_BASE`
- `LDAP_COMPUTER_FILTER`

Below is an example of defining all environment variables when running the script:
```shell
AUTOMOX_API_KEY=<API KEY HERE> \
AUTOMOX_ORGANIZATION_ID=<ORG ID HERE> \
LDAP_URL="ldap://example.local:389" \
LDAP_USER="user@example.local" \
LDAP_PASSWORD=<PASSWORD HERE> \
LDAP_BASE="DC=example,DC=local" \
LDAP_COMPUTER_FILTER="(&(objectClass=computer))" \
python group_devices_by_activedirectory_ou.py
```

## Script Prompts
When the script is run, the user will be prompted for a handful of inputs. These inputs define:
1. The LDAP/AD computer field for hostname comparison (default: name)
2. The LDAP/AD computer attribute for FQDN comparison (default: dnsHostName)
3. A comma separated list of LDAP/AD computer attributes used for tagging devices

```shell
Enter the LDAP/AD computer field for hostname comparison (default: name): 
Enter the LDAP/AD computer attribute for FQDN comparison (default: dnsHostName): 
Enter a comma separated list of LDAP/AD computer attributes used for tagging devices: countryCode,primaryGroupID
```

## Script Output
When running the script, output will be sent to standard output in the case of any input issue, errors, or informational 
messages. This output could be redirected to a file for storing on disk as needed. To avoid verbose output, the script 
does not currently output unmatched device messages; however, a counter message is provided when the script completes to 
give an overview of what occurred:
```
Successfully updated Device ID 1234 (hostname-4, None)
Successfully updated Device ID 5678 (hostname-3, None)
Successfully updated Device ID 9012 (hostname-2, None)
Successfully updated Device ID 3456 (hostname-1, hostname-1.example.local)
Script complete; matched devices: 4, unmatched devices: 2, groups created: 0
```
