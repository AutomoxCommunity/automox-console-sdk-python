import automox_console_sdk as automox
from automox_console_sdk.api import PoliciesApi
import logging
import os
import sys

config = automox.Configuration()

client = automox.ApiClient(configuration=config)
client.default_headers['Authorization'] = f"Bearer {os.getenv('AUTOMOX_API_KEY')}"

# Logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
logger.addHandler(ch)
config.debug = False

policies_api = PoliciesApi(client)

organization = os.getenv('AUTOMOX_ORGANIZATION_ID')

page = 0
while True:
    policies_page = policies_api.get_policies(o=organization, limit=500, page=page)
    for policy in policies_page:
        print(f"Policy ID: {policy['id']}, Name: {policy['name']}, Type: {policy['policy_type_name']}")

    if len(policies_page) == 0:
        break

    page += 1
