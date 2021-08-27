# automox_console_sdk.GroupsApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_server_group**](GroupsApi.md#create_server_group) | **POST** /servergroups | Creates a new server group.
[**delete_server_group**](GroupsApi.md#delete_server_group) | **DELETE** /servergroups/{id} | Deletes a server group.
[**get_server_group**](GroupsApi.md#get_server_group) | **GET** /servergroups/{id} | List Specific Group Object
[**get_server_groups**](GroupsApi.md#get_server_groups) | **GET** /servergroups | List All Group Objects
[**update_server_group**](GroupsApi.md#update_server_group) | **PUT** /servergroups/{id} | Updates a new server group.

# **create_server_group**
> ServerGroup create_server_group(o, body=body)

Creates a new server group.

Creates a new server group.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.GroupsApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Organization ID for the created group
body = automox_console_sdk.ServerGroupCreateOrUpdateRequest() # ServerGroupCreateOrUpdateRequest |  (optional)

try:
    # Creates a new server group.
    api_response = api_instance.create_server_group(o, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->create_server_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID for the created group | 
 **body** | [**ServerGroupCreateOrUpdateRequest**](ServerGroupCreateOrUpdateRequest.md)|  | [optional] 

### Return type

[**ServerGroup**](ServerGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_server_group**
> delete_server_group(id, o)

Deletes a server group.

Any devices that belong to the deleted group will be moved to the organization's Default Group

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.GroupsApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Server Group ID for the specified group
o = 56 # int | Organization ID for the created group

try:
    # Deletes a server group.
    api_instance.delete_server_group(id, o)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_server_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server Group ID for the specified group | 
 **o** | **int**| Organization ID for the created group | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_group**
> ServerGroup get_server_group(id, o)

List Specific Group Object

Returns a specific server group object for the authenticated user.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.GroupsApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Server Group ID for the specified group
o = 56 # int | Organization ID for the specified group

try:
    # List Specific Group Object
    api_response = api_instance.get_server_group(id, o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_server_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server Group ID for the specified group | 
 **o** | **int**| Organization ID for the specified group | 

### Return type

[**ServerGroup**](ServerGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_groups**
> list[ServerGroup] get_server_groups(o, page=page, limit=limit)

List All Group Objects

Retrieves all server group objects for the authenticated user.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.GroupsApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Organization ID for retrieving groups
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) (default to 0)
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. (optional) (default to 500)

try:
    # List All Group Objects
    api_response = api_instance.get_server_groups(o, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_server_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID for retrieving groups | 
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] [default to 0]
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. | [optional] [default to 500]

### Return type

[**list[ServerGroup]**](ServerGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_server_group**
> update_server_group(body, o, id)

Updates a new server group.

Updates a new server group.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.GroupsApi(automox_console_sdk.ApiClient(configuration))
body = automox_console_sdk.ServerGroupCreateOrUpdateRequest() # ServerGroupCreateOrUpdateRequest | 
o = 56 # int | Organization ID for the created group
id = 56 # int | Server Group ID for the specified group

try:
    # Updates a new server group.
    api_instance.update_server_group(body, o, id)
except ApiException as e:
    print("Exception when calling GroupsApi->update_server_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServerGroupCreateOrUpdateRequest**](ServerGroupCreateOrUpdateRequest.md)|  | 
 **o** | **int**| Organization ID for the created group | 
 **id** | **int**| Server Group ID for the specified group | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

