# automox_console_sdk.DevicesApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /servers/{id} | Deletes a device (server object).
[**get_device_packages**](DevicesApi.md#get_device_packages) | **GET** /servers/{id}/packages | List Software Packages for Specific Device
[**get_device_queues**](DevicesApi.md#get_device_queues) | **GET** /servers/{id}/queues | Upcoming Commands Queue for Specific Device
[**get_devices**](DevicesApi.md#get_devices) | **GET** /servers | List All Devices
[**get_server**](DevicesApi.md#get_server) | **GET** /servers/{id} | List a Specific Device
[**issue_device_command**](DevicesApi.md#issue_device_command) | **POST** /servers/{id}/queues | Issue a command to a device
[**update_device**](DevicesApi.md#update_device) | **PUT** /servers/{id} | Updates a device (server object).


# **delete_device**
> delete_device(id, o)

Deletes a device (server object).

Deletes a device (server object). The associated command queue will be purged. Any pending custom commands for the device are removed.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import devices_api
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
    api_instance = devices_api.DevicesApi(api_client)
    id = 1 # int | Server ID for the specified device
    o = 1 # int | Organization ID for the specified device

    # example passing only required values which don't have defaults set
    try:
        # Deletes a device (server object).
        api_instance.delete_device(id, o)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling DevicesApi->delete_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server ID for the specified device |
 **o** | **int**| Organization ID for the specified device |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Delete Successful |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_packages**
> [Packages] get_device_packages(id, o)

List Software Packages for Specific Device

Returns the software packages for the specified device. Packages Include: Pending updates and currently installed updates/applications

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import devices_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.packages import Packages
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
    api_instance = devices_api.DevicesApi(api_client)
    id = 1 # int | Server ID for the specified device
    o = 1 # int | Organization ID for the specified device
    page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) if omitted the server will use the default value of 0
    limit = 500 # int | A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. (optional) if omitted the server will use the default value of 500

    # example passing only required values which don't have defaults set
    try:
        # List Software Packages for Specific Device
        api_response = api_instance.get_device_packages(id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling DevicesApi->get_device_packages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Software Packages for Specific Device
        api_response = api_instance.get_device_packages(id, o, page=page, limit=limit)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling DevicesApi->get_device_packages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server ID for the specified device |
 **o** | **int**| Organization ID for the specified device |
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. | [optional] if omitted the server will use the default value of 500

### Return type

[**[Packages]**](Packages.md)

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

# **get_device_queues**
> [Command] get_device_queues(id, o)

Upcoming Commands Queue for Specific Device

Returns the queue of upcoming commands for the specified device.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import devices_api
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
    api_instance = devices_api.DevicesApi(api_client)
    id = 1 # int | Server ID for the specified device
    o = 1 # int | Organization ID for the specified device

    # example passing only required values which don't have defaults set
    try:
        # Upcoming Commands Queue for Specific Device
        api_response = api_instance.get_device_queues(id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling DevicesApi->get_device_queues: %s\n" % e)
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

# **get_devices**
> [ServerList] get_devices(o, )

List All Devices

This retrieves a detailed list of all devices (server objects) for the authenticated user.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import devices_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.server_list import ServerList
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
    api_instance = devices_api.DevicesApi(api_client)
    o = 1 # int | Organization ID. Response will include devices for the specified Automox Organization
    group_id = 1 # int | Filter based on membership to a specific Server Group ID (optional)
    ps_version = 1 # int | Shows version of PowerShell running on the device, if applicable. (optional)
    pending = 0 # int | Filter based on status of pending patches. Format: pending=1 (optional)
    patch_status = "patchStatus_example" # str | Filter based on presence of ANY available patches that aren't already installed. Value must be 'missing' Format: patchStatus=missing (optional)
    policy_id = 1 # int | Filter based on association to a given Policy ID (optional)
    exception = 0 # int | Filter based on device's Exception status (optional)
    managed = 0 # int | Filter based on device's Managed status. Unmanaged indicates no linked policies. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List All Devices
        api_response = api_instance.get_devices(o, )
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling DevicesApi->get_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Devices
        api_response = api_instance.get_devices(o, group_id=group_id, ps_version=ps_version, pending=pending, patch_status=patch_status, policy_id=policy_id, exception=exception, managed=managed)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling DevicesApi->get_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID. Response will include devices for the specified Automox Organization |
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. | defaults to 500
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | defaults to 0
 **group_id** | **int**| Filter based on membership to a specific Server Group ID | [optional]
 **ps_version** | **int**| Shows version of PowerShell running on the device, if applicable. | [optional]
 **pending** | **int**| Filter based on status of pending patches. Format: pending&#x3D;1 | [optional]
 **patch_status** | **str**| Filter based on presence of ANY available patches that aren&#39;t already installed. Value must be &#39;missing&#39; Format: patchStatus&#x3D;missing | [optional]
 **policy_id** | **int**| Filter based on association to a given Policy ID | [optional]
 **exception** | **int**| Filter based on device&#39;s Exception status | [optional]
 **managed** | **int**| Filter based on device&#39;s Managed status. Unmanaged indicates no linked policies. | [optional]

### Return type

[**[ServerList]**](ServerList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |
**404** | Entity not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server**
> ServerWithPolicies get_server(id, o)

List a Specific Device

Returns a specific device (server object) for the authenticated user.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import devices_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.server_with_policies import ServerWithPolicies
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
    api_instance = devices_api.DevicesApi(api_client)
    id = 1 # int | Server ID for the specified device
    o = 1 # int | Organization ID for the specified device

    # example passing only required values which don't have defaults set
    try:
        # List a Specific Device
        api_response = api_instance.get_server(id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling DevicesApi->get_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server ID for the specified device |
 **o** | **int**| Organization ID for the specified device |

### Return type

[**ServerWithPolicies**](ServerWithPolicies.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
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
from automox_console_sdk.api import devices_api
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
    api_instance = devices_api.DevicesApi(api_client)
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
        print("Exception when calling DevicesApi->issue_device_command: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Issue a command to a device
        api_instance.issue_device_command(id, o, unknown_base_type=unknown_base_type)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling DevicesApi->issue_device_command: %s\n" % e)
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

# **update_device**
> update_device(id, unknown_base_type)

Updates a device (server object).

Updates a device (server object).

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import devices_api
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
    api_instance = devices_api.DevicesApi(api_client)
    id = 1 # int | Server ID for the specified device
    unknown_base_type = {
        server_group_id=1,
        exception=True,
        tags=[
            "tags_example",
        ],
        custom_name="custom_name_example",
    } # UNKNOWN_BASE_TYPE | Device update
    o = 1 # int | Organization ID for the specified device (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a device (server object).
        api_instance.update_device(id, unknown_base_type)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling DevicesApi->update_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a device (server object).
        api_instance.update_device(id, unknown_base_type, o=o)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling DevicesApi->update_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server ID for the specified device |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Device update |
 **o** | **int**| Organization ID for the specified device | [optional]

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
**204** | Update Successful |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

