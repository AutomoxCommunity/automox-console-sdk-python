# Upload CSV Report to Vulnerability Sync
Automox provides customers the ability to ingest vulnerability reports (CVEs) into the Automox Console via a CSV file uploaded to the API. This use case example illustrates a script that scans a directory for CSVs and uploads them to the [Automox Vulnerability Sync CSV batch upload endpoint](https://developer.automox.com/openapi/vulnsync/operation/UploadCSVBatch/). This script can be particularly useful in organizations which delegate the responsibilities of IT Operations and Security to different teams.

## Before Running the Script
This script does not programmatically reach out to any CVE Vulnerability Database. You will still have to populate the [cve_queue](./cve_queue) directory yourself.

## Running the Script
To run the scripts, first make sure Python 3 is installed on the host system and clone this repository locally then
follow the below steps:
1. Create a virtual environment: `python3 -m venv venv`
2. Source virtual environment: `source venv/bin/activate`
3. Install the Automox Console SDK: `pip install automox-console-sdk`
4. Navigate to the script directory: `cd examples/use-cases/vuln_sync_csv_upload`
5. Run the script: `python vuln_upload.py`

This will execute the script and prompt for inputs. Validation will be performed to ensure there
are alerts for improper input(s) if encountered.

Both the Automox API Key and Organization ID inputs can be defined as environment variables prior to running the `vuln_upload.py` script
to avoid continual prompting. This can be accomplished by exporting the AUTOMOX_API_KEY and AUTOMOX_ORGANIZATION_ID environment
variables:
```shell
AUTOMOX_API_KEY=<API KEY HERE> AUTOMOX_ORGANIZATION_ID=<ORG ID HERE> python vuln_upload.py
```

## Script Output
When running the script, output will be sent to standard out in the case of an input issue, errors, or informational
messages. This output could be redirected to a file for storing on disk as needed.

After running the script, it will scan the [cve_queue](./cve_queue) directory for any CSV files.
```
Found 2 file(s) to upload.
```

If the script finds any CSV files, it will iterate over the files and attempt to upload them to the [Automox Vulnerability Sync API](https://developer.automox.com/openapi/vulnsync/operation/UploadCSVBatch/). If successful, it will automatically move the file to [cve_queue/processed](./cve_queue/processed).
```
Sending vuln.csv to Automox Vulnerability Sync...
==============================
BATCH ID: 501
vuln.csv has been uploaded.
==============================
Moving vuln.csv to /automox-console-sdk-python/examples/use-cases/vuln_sync_csv_upload/cve_queue/processed/vuln.csv
```

Once the script has iterated over all of the elgibile files for upload, it will poll the API for the build status of the batches sent, and when all the batches are marked as "Awaiting Approval", a pre-task report for each batch will be outputted.
```
Batches are still building... Checking for updates...
Batches are done processing!
==============================
BATCH ID: 501
vuln.csv has been processed.
Total Vulnerabilities: 5
Devices Impacted: 0
Tasks Pending Creation: 2
Batch Issues: 0
Unknown Hosts: 0
==============================
```

Batches are viewable in the [Automox Console](https://console.automox.com/manage/tasks/batches) for approval.
