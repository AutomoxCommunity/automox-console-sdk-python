# automox_console_sdk.CommandsApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_queues**](CommandsApi.md#get_device_queues) | **GET** /servers/{id}/queues | Upcoming Commands Queue for Specific Device
[**issue_device_command**](CommandsApi.md#issue_device_command) | **POST** /servers/{id}/queues | Issue a command to a device

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
api_instance = automox_console_sdk.CommandsApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Server ID for the specified device
o = 56 # int | Organization ID for the specified device

try:
    # Upcoming Commands Queue for Specific Device
    api_response = api_instance.get_device_queues(id, o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->get_device_queues: %s\n" % e)
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
api_instance = automox_console_sdk.CommandsApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Organization ID for the specified device
id = 56 # int | Server ID for the specified device
body = automox_console_sdk.IdQueuesBody() # IdQueuesBody |  (optional)

try:
    # Issue a command to a device
    api_instance.issue_device_command(o, id, body=body)
except ApiException as e:
    print("Exception when calling CommandsApi->issue_device_command: %s\n" % e)
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

