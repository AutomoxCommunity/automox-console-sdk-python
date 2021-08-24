import automox_console_sdk as automox
from automox_console_sdk.api import GroupsApi
from automox_console_sdk.models import ServerGroupCreateOrUpdateRequest
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

organization = 9237
groups_api = GroupsApi(client)

# Get Default Server Group id for org
default_server_group_id = 0
for g in groups_api.get_server_groups(o=organization):
    if not g.name:
        default_server_group_id = g.id

print(f"Using Default Server Group ID: {default_server_group_id}")

# Define object of group to be created with required fields
group = ServerGroupCreateOrUpdateRequest(name="OpenAPI Test", refresh_interval=360, parent_server_group_id=default_server_group_id)
g = groups_api.create_server_group(o=organization, body=group)

print(f"Group: {g.name}, ID: {g.id}")