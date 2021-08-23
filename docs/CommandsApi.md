# automox_console_sdk.CommandsApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_queues**](CommandsApi.md#get_device_queues) | **GET** /servers/{id}/queues | Upcoming Commands Queue for Specific Device
[**issue_device_command**](CommandsApi.md#issue_device_command) | **POST** /servers/{id}/queues | Issue a command to a device


# **get_device_queues**
> [Command] get_device_queues(id, o)

Upcoming Commands Queue for Specific Device

Returns the queue of upcoming commands for the specified device.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import commands_api
from automox_console_sdk.model.command import Command
from automox_console_sdk.model.inline_response403 import InlineResponse403
from pprint import pprint
# Defining the host is optional and defaults to https://console.automox.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = automox_console_sdk.Configuration(
    host = "https://console.automox.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = automox_console_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with automox_console_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = commands_api.CommandsApi(api_client)
    id = 1 # int | Server ID for the specified device
    o = 1 # int | Organization ID for the specified device

    # example passing only required values which don't have defaults set
    try:
        # Upcoming Commands Queue for Specific Device
        api_response = api_instance.get_device_queues(id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling CommandsApi->get_device_queues: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server ID for the specified device |
 **o** | **int**| Organization ID for the specified device |

### Return type

[**[Command]**](Command.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |
**404** | Entity not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_device_command**
> issue_device_command(id, o)

Issue a command to a device

Force a device to Scan, Patch, or Reboot for immediate execution. **Note: The `installAllUpdates` option ignores any Policy Filters**

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import commands_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.unknownbasetype import UNKNOWNBASETYPE
from pprint import pprint
# Defining the host is optional and defaults to https://console.automox.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = automox_console_sdk.Configuration(
    host = "https://console.automox.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = automox_console_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with automox_console_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = commands_api.CommandsApi(api_client)
    id = 1 # int | Server ID for the specified device
    o = 1 # int | Organization ID for the specified device
    unknown_base_type = {
        command_type_name="GetOS",
        args="args_example",
    } # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Issue a command to a device
        api_instance.issue_device_command(id, o)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling CommandsApi->issue_device_command: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Issue a command to a device
        api_instance.issue_device_command(id, o, unknown_base_type=unknown_base_type)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling CommandsApi->issue_device_command: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server ID for the specified device |
 **o** | **int**| Organization ID for the specified device |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Command submitted successfully |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

