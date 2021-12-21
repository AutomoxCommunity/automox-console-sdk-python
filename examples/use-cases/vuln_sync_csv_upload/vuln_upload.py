"""Use case for automating the ingestion of CVE reports"""
import os
import sys
import time
from getpass import getpass
from io import FileIO

import requests


def upload_cve(file: FileIO):
    """ Uploads vulnerability list to Automox Vulnerability Sync endpoint.

    Args:
        file (FileIO): A CSV file containing vulnerability data.

    Returns:
        response_data (dict): API response from Automox Vulnerability Sync
        https://developer.automox.com/openapi/vulnsync/operation/UploadCSVBatch/
    """

    response_data = {}

    task = "patch"
    url  = f"https://console.automox.com/api/orgs/{organization}/tasks/{task}/batches/upload"

    filename = os.path.basename(file.name)

    try:
        headers = {
            "Authorization": f"Bearer {api_secret}",
        }

        files = [
            ('file', (filename, file, 'text/csv'))
        ]

        response = requests.request("POST", url, headers=headers, files=files)

        response_data = response.json()

        if "errors" in response_data and len(response_data['errors']) > 0:
            msg = ""
            msg = msg.join(response_data['errors'])

            raise Exception(msg)
    except requests.RequestException as error:
        print(f"Error: Unable to complete CSV upload request. ({error})")

    return response_data

def get_unprocessed_cves(directory: str):
    """Returns a list of CSV files to upload and process.

    Args:
        directory (str): Directory to look in for CSVs.

    Returns:
        cve_files (list): List of files to be processed and uploaded.
    """

    cve_files = []

    paths = os.listdir(directory)

    for path in paths:
        try:
            # To only query CSV files
            if not path.endswith(".csv"):
                continue

            cve_file = open(f"{directory}/{path}", "rb")

            cve_files.append(cve_file)
        except (OSError, IOError) as error:
            print(f"Error: Could not open a CSV. {error}")

    print(f"Found {len(cve_files)} file(s) to upload.")

    return cve_files

def process_cves(unprocessed_cve_list: list):
    """Handles uploading and moving the CSV file to the processed directory.

    Args:
        unprocessed_cve_list (list): List of files to process.
    """

    uploaded_batches = {}

    for file in unprocessed_cve_list:
        try:
            # Make the request to upload the batch file
            print(f"Sending {os.path.basename(file.name)} to Automox Vulnerability Sync...")

            response = upload_cve(file)

            if response['id']:
                uploaded_batches[response['id']] = response

            upload_output = (
                "==============================\n"
                f"BATCH ID: {response['id']}\n"
                f"{response['source']} has been uploaded.\n"
                "=============================="
            )

            print(upload_output)

            path      = os.path.realpath(file.name)
            directory = os.path.dirname(path)
            filename  = os.path.basename(file.name)
            new_path  = f"{directory}/processed/{filename}"

            print(f"Moving {filename} to {new_path}\n")

            os.rename(path, new_path)
        except OSError as error:
            print(f"Error processing CVE: {error}")

    return uploaded_batches

def update_batches(uploaded_batches: dict):
    """Polls the Automox API for the status of batches contained in this dictionary.

    When CSV files containing CVE information is uploaded to the Automox Vulnerability Sync API, a task list is built

    Args:
        uploaded_batches (dict): A dictionary of the latest responses from the Automox API about the status of a batch.

    Returns:
        uploaded_batches: An updated dictionary of the latest responses from the Automox API about the status of a batch.
    """

    for batch_id, batch in uploaded_batches.items():
        if uploaded_batches[batch_id]['status'] != "awaiting_approval":
            headers = {
                "Authorization": f"Bearer {api_secret}",
            }

            response = requests.get(f"https://console.automox.com/api/orgs/{organization}/tasks/batches/{batch['id']}", headers=headers)

            batches[batch_id] = response.json()

    return uploaded_batches

try:
    # Directory to watch for new CVE CSVs
    WATCH_DIR = os.getenv("WATCH_DIR") or "./cve_queue"

    # Prompt for inputs
    api_secret   = os.getenv('AUTOMOX_API_KEY') or getpass('Enter your API Key: ')
    organization = os.getenv('AUTOMOX_ORGANIZATION_ID') or input("Enter your Organization ID: ")

    cve_list = get_unprocessed_cves(WATCH_DIR)

    if len(cve_list) == 0:
        sys.exit()

    batches  = process_cves(cve_list)

    # Assumes the batches have not been built upon receipt.
    batches_complete = len(batches) == 0

    while not batches_complete:
        print("Batches are still building... Checking for updates...")
        batches = update_batches(batches)

        for batch_id, batch in batches.items():
            batches_complete = True

            if not batches[batch_id]['status'] == "awaiting_approval":
                batches_complete = False

        time.sleep(10)

    print("Batches are done processing!")

    for batch_id, batch in batches.items():
        output = (
            "==============================\n"
            f"BATCH ID: {batch['id']}\n"
            f"{batch['source']} has been processed.\n"
            f"Total Vulnerabilities: {batch['cve_count']}\n"
            f"Devices Impacted: {batch['impacted_device_count']}\n"
            f"Tasks Pending Creation: {batch['task_count']}\n"
            f"Batch Issues: {batch['issue_count']}\n"
            f"Unknown Hosts: {batch['unknown_host_count']}\n"
            "=============================="
        )

        print(output)
except Exception as e:
    print(f"Error: {e}\n")
    raise
except KeyboardInterrupt:
    print ("Crtl+C Pressed. Shutting down.")
