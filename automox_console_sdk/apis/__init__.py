
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.api_keys_api import APIKeysApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from automox_console_sdk.api.api_keys_api import APIKeysApi
from automox_console_sdk.api.approvals_api import ApprovalsApi
from automox_console_sdk.api.commands_api import CommandsApi
from automox_console_sdk.api.devices_api import DevicesApi
from automox_console_sdk.api.events_api import EventsApi
from automox_console_sdk.api.extracts_api import ExtractsApi
from automox_console_sdk.api.groups_api import GroupsApi
from automox_console_sdk.api.organizations_api import OrganizationsApi
from automox_console_sdk.api.packages_api import PackagesApi
from automox_console_sdk.api.policies_api import PoliciesApi
from automox_console_sdk.api.reports_api import ReportsApi
from automox_console_sdk.api.users_api import UsersApi
from automox_console_sdk.api.worklets_api import WorkletsApi
