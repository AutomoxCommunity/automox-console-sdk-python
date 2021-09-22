# automox_console_sdk.DevicesApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_update_devices**](DevicesApi.md#batch_update_devices) | **POST** /servers/batch | Updates multiple devices (server objects).
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /servers/{id} | Deletes a device (server object) from the organization.
[**get_device_packages**](DevicesApi.md#get_device_packages) | **GET** /servers/{id}/packages | List Software Packages for Specific Device
[**get_device_queues**](DevicesApi.md#get_device_queues) | **GET** /servers/{id}/queues | Upcoming Commands Queue for Specific Device
[**get_devices**](DevicesApi.md#get_devices) | **GET** /servers | List All Devices
[**get_server**](DevicesApi.md#get_server) | **GET** /servers/{id} | List a Specific Device
[**issue_device_command**](DevicesApi.md#issue_device_command) | **POST** /servers/{id}/queues | Issue a command to a device
[**update_device**](DevicesApi.md#update_device) | **PUT** /servers/{id} | Updates a device (server object).

# **batch_update_devices**
> Batch batch_update_devices(body, o)

Updates multiple devices (server objects).

Updates multiple devices (server objects) in a batch.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.DevicesApi(automox_console_sdk.ApiClient(configuration))
body = automox_console_sdk.ServersBatchBody() # ServersBatchBody | Update devices
o = 56 # int | Organization ID for the specified devices

try:
    # Updates multiple devices (server objects).
    api_response = api_instance.batch_update_devices(body, o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->batch_update_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServersBatchBody**](ServersBatchBody.md)| Update devices | 
 **o** | **int**| Organization ID for the specified devices | 

### Return type

[**Batch**](Batch.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> delete_device(id, o)

Deletes a device (server object) from the organization.

**NOTE:** The associated command queue will be purged. Any pending custom commands for the device are removed.

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
    # Deletes a device (server object) from the organization.
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
id = 56 # int | Server ID for the specified device.
o = 56 # int | Organization ID for the specified device
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 0)
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 500)

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
 **id** | **int**| Server ID for the specified device. | 
 **o** | **int**| Organization ID for the specified device | 
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 0]
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with &#x60;page&#x60; parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 500]

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
id = 56 # int | Server ID for the specified device.
o = 56 # int | Organization ID for the specified device.

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
 **id** | **int**| Server ID for the specified device. | 
 **o** | **int**| Organization ID for the specified device. | 

### Return type

[**list[Command]**](Command.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**
> list[Server] get_devices(o, limit, page, group_id=group_id, ps_version=ps_version, pending=pending, patch_status=patch_status, policy_id=policy_id, exception=exception, managed=managed, filters=filters, sort_columns=sort_columns, sort_dir=sort_dir)

List All Devices

Retrieves a detailed list of all devices (server objects) for the authenticated user.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.DevicesApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Organization ID. Response will include devices for the specified Automox Organization. The organization will be assumed based on the API key, if not specified.
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (default to 500)
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (default to 0)
group_id = 56 # int | Filter based on membership to a specific Server Group ID (optional)
ps_version = 56 # int | Shows version of PowerShell running on the device, if applicable. (optional)
pending = 56 # int | Filter based on status of pending patches. Format: `pending=1` (optional)
patch_status = 'missing' # str | Filter based on presence of ANY available patches that aren't already installed. Value must be 'missing' Format: `patchStatus=missing` (optional) (default to missing)
policy_id = 56 # int | Filter based on association to a given Policy ID. Format: `policyId=12345` (optional)
exception = 56 # int | Filter based on the exception property to exclude the device from reports. Device is still monitored when excluded from reports and statistics. Format: `exception=1` (optional)
managed = 56 # int | Filter based on device's Managed status. Unmanaged indicates no linked policies. Format: `managed=0` (optional)
filters = automox_console_sdk.Filters() # Filters | Filter on compatible devices (optional)
sort_columns = 'sort_columns_example' # str | The column you want to sort by. (optional)
sort_dir = 'sort_dir_example' # str | The sort direction, ascending or descending. (optional)

try:
    # List All Devices
    api_response = api_instance.get_devices(o, limit, page, group_id=group_id, ps_version=ps_version, pending=pending, patch_status=patch_status, policy_id=policy_id, exception=exception, managed=managed, filters=filters, sort_columns=sort_columns, sort_dir=sort_dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID. Response will include devices for the specified Automox Organization. The organization will be assumed based on the API key, if not specified. | 
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [default to 500]
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [default to 0]
 **group_id** | **int**| Filter based on membership to a specific Server Group ID | [optional] 
 **ps_version** | **int**| Shows version of PowerShell running on the device, if applicable. | [optional] 
 **pending** | **int**| Filter based on status of pending patches. Format: &#x60;pending&#x3D;1&#x60; | [optional] 
 **patch_status** | **str**| Filter based on presence of ANY available patches that aren&#x27;t already installed. Value must be &#x27;missing&#x27; Format: &#x60;patchStatus&#x3D;missing&#x60; | [optional] [default to missing]
 **policy_id** | **int**| Filter based on association to a given Policy ID. Format: &#x60;policyId&#x3D;12345&#x60; | [optional] 
 **exception** | **int**| Filter based on the exception property to exclude the device from reports. Device is still monitored when excluded from reports and statistics. Format: &#x60;exception&#x3D;1&#x60; | [optional] 
 **managed** | **int**| Filter based on device&#x27;s Managed status. Unmanaged indicates no linked policies. Format: &#x60;managed&#x3D;0&#x60; | [optional] 
 **filters** | [**Filters**](.md)| Filter on compatible devices | [optional] 
 **sort_columns** | **str**| The column you want to sort by. | [optional] 
 **sort_dir** | **str**| The sort direction, ascending or descending. | [optional] 

### Return type

[**list[Server]**](Server.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server**
> ServerWithPolicies get_server(id, o, ps_version=ps_version)

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
id = 56 # int | Server ID for the specified device.
o = 56 # int | Organization ID for the specified device.
ps_version = 56 # int | The version of PowerShell running on the device. (optional)

try:
    # List a Specific Device
    api_response = api_instance.get_server(id, o, ps_version=ps_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server ID for the specified device. | 
 **o** | **int**| Organization ID for the specified device. | 
 **ps_version** | **int**| The version of PowerShell running on the device. | [optional] 

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
> update_device(body, o, id)

Updates a device (server object).

Send a JSON object in the request body to update device details).

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
o = 56 # int | Organization ID for the specified device.
id = 56 # int | Server ID for the specified device.

try:
    # Updates a device (server object).
    api_instance.update_device(body, o, id)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServersIdBody**](ServersIdBody.md)| Device update | 
 **o** | **int**| Organization ID for the specified device. | 
 **id** | **int**| Server ID for the specified device. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

