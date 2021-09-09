![Automox logo]

# Automox SDK for Python

[![Continuous Integration](https://github.com/AutomoxCommunity/automox-console-sdk-python/actions/workflows/ci.yml/badge.svg)](https://github.com/AutomoxCommunity/automox-console-sdk-python/actions/workflows/ci.yml)
[![Release](https://github.com/AutomoxCommunity/automox-console-sdk-python/actions/workflows/release.yml/badge.svg)](https://github.com/AutomoxCommunity/automox-console-sdk-python/actions/workflows/release.yml)

The Automox SDK for Python includes an out-of-the-box Python library used to interact with the [Automox Console API] 
in order to:
- Perform automated tasks
- Retrieve Automox data
- Perform management and administration functions
- All other Automox Console API functionality!

This SDK automatically generated and maintained with the use of [Swagger Codegen](https://github.com/swagger-api/swagger-codegen). 
By providing a supported mechanism with usage examples, we hope that customers can quickly get comfortable with the
Automox API without the need to generate or build the library themselves.

## Requirements

The SDK has been tested and supported for the following versions of Python:
- Python 3 versions 3.9 and later

While the library will work with Python 2.7, we discourage and do not support Python 2 use as it has since been sunset 
and python.org [recommends upgrading to Python 3](https://www.python.org/doc/sunset-python-2/).

## Installation & Usage

### pip install

The Automox SDK for Python is most easily installed with a single `pip` command to pull the latest package version from 
the [Python package Index (PyPi)](https://pypi.org/). The published versions of the project are maintained at the 
[PyPi Project page](https://pypi.org/project/automox-console-sdk/). Getting started is generally a simple as running 
the following command on a system with Python 3.9+ installed:

```shell
pip install automox-console-sdk
```

### Github Release install

With each new release of the SDK, a published tag and Github Release will be created. To install the latest version of 
SDK from Github:
1. Download the latest wheel from the project's [Github Releases](https://github.com/AutomoxCommunity/automox-console-sdk-python/releases)
2. Install the wheel locally: `pip install automox_console_sdk-0.1.1-py3-none-any.whl`
3. Import the package:
```python
import automox_console_sdk 
```

## Getting Started

Please follow the [installation procedure](https://github.com/AutomoxCommunity/automox-console-sdk-python#installation--usage) and then move on to the following sections.

### The Basics

Prior to using the SDK, it is necessary to generate an [Automox API Key](https://docs.automox.com/home/automox-settings/accessing-your-api-keys#api-key) 
used for authorizing requests to the Automox API. Steps for creating an API key for you user account can be found 
[here](https://docs.automox.com/home/automox-settings/accessing-your-api-keys#adding-api-keys).

Once an API key has been created, it can then be used with the [example scripts](https://github.com/AutomoxCommunity/automox-console-sdk-python/tree/main/examples/scripts) provided with the 
SDK. By importing the package and creating an Automox ApiClient, you will then be ready to leverage SDK functionality:

```python
import automox_console_sdk as automox
import os

config = automox.Configuration()

client = automox.ApiClient(configuration=config)
client.default_headers['Authorization'] = f"Bearer {os.getenv('AUTOMOX_API_KEY')}"
```

The example above imports the package, creates a base configuration, and initializes the `ApiClient` with the 
Authorization header set with your API key. All examples avoid hard-coding API Keys in the script by leveraging the 
`AUTOMOX_API_KEY` environment variable. When running scripts, remember to set or pass your API key as an environment 
variable to avoid authorization exceptions:
```shell
AUTOMOX_API_KEY=<API KEY GOES HERE> python example.py
```

Once defining the base client with authorization, the script can be updated to include a specific API implementation. In 
the example below we will be using the DevicesApi to list devices:
```python
devices_api = DevicesApi(client)

for d in devices_api.get_devices(limit=500, page=0):
    print(f"Device ID: {d.id}, Hostname: {d.name}, Server Group ID: {d.server_group_id}, IP Addresses: {d.ip_addrs}")
```

A fully-implemented [script example](https://github.com/AutomoxCommunity/automox-console-sdk-python/blob/main/examples/scripts/list_devices.py) of listing devices is provided along with a
growing number of other examples of using the Automox SDK for Python. Feel free to contribute any scripts you have found 
helpful with the Community!

### Example Scripts

To get started without writing a single line of Python, [Example Scripts](https://github.com/AutomoxCommunity/automox-console-sdk-python/tree/main/examples/scripts) have been included with the 
SDK. These scripts show off simple functionality such as:
- Listing Devices
- Updating a Device
- Creating a Device Group

They should be used as reference as you are building your own scripts and utilities with the Automox SDK.

### Use Cases Examples (COMING SOON)

[Use Case Examples](https://github.com/AutomoxCommunity/automox-console-sdk-python/tree/main/examples/use-cases) have been provided to show off end to end utility of leveraging the Automox SDK
within varying environments. These use cases can be used as-is or modified to meet your environment needs. 

## Limitations

All functionality provided by the Automox Console SDK for Python is based on the Autmox Console API specification that 
is publicly published. If there is functionality that is incomplete or does not yet exist, please reached out to your 
Customer Success Manager or [contact support](https://support.automox.com/help/contacting-automox-support) along with
the details of what you would like to see in future releases of the SDK.

[//]: # "Link anchor definitions"
[Automox Logo]: https://raw.githubusercontent.com/AutomoxCommunity/automox-console-sdk-python/main/assets/AX-Horiz-Logo.png
[Automox Console API]: https://developer.automox.com/developer-portal/
[Documentation]: https://github.com/AutomoxCommunity/automox-console-sdk-python/blob/main/docs/README.md
