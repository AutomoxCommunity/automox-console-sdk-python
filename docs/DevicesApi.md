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
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.DevicesApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Server ID for the specified device
o = 56 # int | Organization ID for the specified device

try:
    # Deletes a device (server object).
    api_instance.delete_device(id, o)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_packages**
> list[Packages] get_device_packages(id, o, page=page, limit=limit)

List Software Packages for Specific Device

Returns the software packages for the specified device. Packages Include: Pending updates and currently installed updates/applications

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.DevicesApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Server ID for the specified device
o = 56 # int | Organization ID for the specified device
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) (default to 0)
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. (optional) (default to 500)

try:
    # List Software Packages for Specific Device
    api_response = api_instance.get_device_packages(id, o, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server ID for the specified device | 
 **o** | **int**| Organization ID for the specified device | 
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] [default to 0]
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. | [optional] [default to 500]

### Return type

[**list[Packages]**](Packages.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_queues**
> list[Command] get_device_queues(id, o)

Upcoming Commands Queue for Specific Device

Returns the queue of upcoming commands for the specified device.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.DevicesApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Server ID for the specified device
o = 56 # int | Organization ID for the specified device

try:
    # Upcoming Commands Queue for Specific Device
    api_response = api_instance.get_device_queues(id, o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_queues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server ID for the specified device | 
 **o** | **int**| Organization ID for the specified device | 

### Return type

[**list[Command]**](Command.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**
> ServerList get_devices(o, limit, page, group_id=group_id, ps_version=ps_version, pending=pending, patch_status=patch_status, policy_id=policy_id, exception=exception, managed=managed)

List All Devices

This retrieves a detailed list of all devices (server objects) for the authenticated user.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.DevicesApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Organization ID. Response will include devices for the specified Automox Organization
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. (default to 500)
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (default to 0)
group_id = 56 # int | Filter based on membership to a specific Server Group ID (optional)
ps_version = 56 # int | Shows version of PowerShell running on the device, if applicable. (optional)
pending = 56 # int | Filter based on status of pending patches. Format: pending=1 (optional)
patch_status = 'patch_status_example' # str | Filter based on presence of ANY available patches that aren't already installed. Value must be 'missing' Format: patchStatus=missing (optional)
policy_id = 56 # int | Filter based on association to a given Policy ID (optional)
exception = 56 # int | Filter based on device's Exception status (optional)
managed = 56 # int | Filter based on device's Managed status. Unmanaged indicates no linked policies. (optional)

try:
    # List All Devices
    api_response = api_instance.get_devices(o, limit, page, group_id=group_id, ps_version=ps_version, pending=pending, patch_status=patch_status, policy_id=policy_id, exception=exception, managed=managed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID. Response will include devices for the specified Automox Organization | 
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. | [default to 500]
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [default to 0]
 **group_id** | **int**| Filter based on membership to a specific Server Group ID | [optional] 
 **ps_version** | **int**| Shows version of PowerShell running on the device, if applicable. | [optional] 
 **pending** | **int**| Filter based on status of pending patches. Format: pending&#x3D;1 | [optional] 
 **patch_status** | **str**| Filter based on presence of ANY available patches that aren&#x27;t already installed. Value must be &#x27;missing&#x27; Format: patchStatus&#x3D;missing | [optional] 
 **policy_id** | **int**| Filter based on association to a given Policy ID | [optional] 
 **exception** | **int**| Filter based on device&#x27;s Exception status | [optional] 
 **managed** | **int**| Filter based on device&#x27;s Managed status. Unmanaged indicates no linked policies. | [optional] 

### Return type

[**ServerList**](ServerList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server**
> ServerWithPolicies get_server(id, o)

List a Specific Device

Returns a specific device (server object) for the authenticated user.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.DevicesApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Server ID for the specified device
o = 56 # int | Organization ID for the specified device

try:
    # List a Specific Device
    api_response = api_instance.get_server(id, o)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_device_command**
> issue_device_command(o, id, body=body)

Issue a command to a device

Force a device to Scan, Patch, or Reboot for immediate execution. **Note: The `installAllUpdates` option ignores any Policy Filters**

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.DevicesApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Organization ID for the specified device
id = 56 # int | Server ID for the specified device
body = automox_console_sdk.IdQueuesBody() # IdQueuesBody |  (optional)

try:
    # Issue a command to a device
    api_instance.issue_device_command(o, id, body=body)
except ApiException as e:
    print("Exception when calling DevicesApi->issue_device_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID for the specified device | 
 **id** | **int**| Server ID for the specified device | 
 **body** | [**IdQueuesBody**](IdQueuesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> update_device(body, id, o=o)

Updates a device (server object).

Updates a device (server object).

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.DevicesApi(automox_console_sdk.ApiClient(configuration))
body = automox_console_sdk.ServersIdBody() # ServersIdBody | Device update
id = 56 # int | Server ID for the specified device
o = 56 # int | Organization ID for the specified device (optional)

try:
    # Updates a device (server object).
    api_instance.update_device(body, id, o=o)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServersIdBody**](ServersIdBody.md)| Device update | 
 **id** | **int**| Server ID for the specified device | 
 **o** | **int**| Organization ID for the specified device | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

