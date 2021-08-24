import automox_console_sdk as automox
from automox_console_sdk.api import DevicesApi
from automox_console_sdk.models import ServersIdBody
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

device_id = 1122213
group_id = 109820
server_update = ServersIdBody(server_group_id=group_id, exception=True, tags=['hello','world'])
update_result = devices_api.update_device(o=9237, id=device_id, body=server_update)

print(update_result)
