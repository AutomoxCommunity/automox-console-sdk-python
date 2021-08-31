import automox_console_sdk as automox
from automox_console_sdk.api import DevicesApi
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

devices_api = DevicesApi(client)

organization = os.getenv('AUTOMOX_ORGANIZATION_ID')

for d in devices_api.get_devices(o=organization, limit=500, page=0):
    print(f"Device ID: {d.id}, Hostname: {d.name}, Server Group ID: {d.server_group_id}, IP Addresses: {d.ip_addrs}")