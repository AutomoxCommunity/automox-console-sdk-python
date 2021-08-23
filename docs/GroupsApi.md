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
> [ServerGroup] create_server_group(o)

Creates a new server group.

Creates a new server group.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import groups_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.server_group_create_or_update_request import ServerGroupCreateOrUpdateRequest
from automox_console_sdk.model.server_group import ServerGroup
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
    api_instance = groups_api.GroupsApi(api_client)
    o = 1 # int | Organization ID for the created group
    server_group_create_or_update_request = ServerGroupCreateOrUpdateRequest(
        name="name_example",
        refresh_interval=360,
        parent_server_group_id=1,
        ui_color="ui_color_example",
        notes="notes_example",
        enable_os_auto_update=True,
        enable_wsus=True,
        wsus_server="wsus_server_example",
        policies=[
            1,
        ],
    ) # ServerGroupCreateOrUpdateRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a new server group.
        api_response = api_instance.create_server_group(o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling GroupsApi->create_server_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new server group.
        api_response = api_instance.create_server_group(o, server_group_create_or_update_request=server_group_create_or_update_request)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling GroupsApi->create_server_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID for the created group |
 **server_group_create_or_update_request** | [**ServerGroupCreateOrUpdateRequest**](ServerGroupCreateOrUpdateRequest.md)|  | [optional]

### Return type

[**[ServerGroup]**](ServerGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Operation |  -  |
**400** | Invalid Request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_server_group**
> delete_server_group(id, o)

Deletes a server group.

Any devices that belong to the deleted group will be moved to the organization's Default Group

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | Server Group ID for the specified group
    o = 1 # int | Organization ID for the created group

    # example passing only required values which don't have defaults set
    try:
        # Deletes a server group.
        api_instance.delete_server_group(id, o)
    except automox_console_sdk.ApiException as e:
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deletion Successful |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_group**
> ServerGroup get_server_group(id, o)

List Specific Group Object

Returns a specific server group object for the authenticated user.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import groups_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.server_group import ServerGroup
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | Server Group ID for the specified group
    o = 1 # int | Organization ID for the specified group

    # example passing only required values which don't have defaults set
    try:
        # List Specific Group Object
        api_response = api_instance.get_server_group(id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
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

# **get_server_groups**
> [ServerGroup] get_server_groups(o)

List All Group Objects

Retrieves all server group objects for the authenticated user.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import groups_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.server_group import ServerGroup
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
    api_instance = groups_api.GroupsApi(api_client)
    o = 1 # int | Organization ID for retrieving groups
    page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) if omitted the server will use the default value of 0
    limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. (optional) if omitted the server will use the default value of 500

    # example passing only required values which don't have defaults set
    try:
        # List All Group Objects
        api_response = api_instance.get_server_groups(o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling GroupsApi->get_server_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Group Objects
        api_response = api_instance.get_server_groups(o, page=page, limit=limit)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling GroupsApi->get_server_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID for retrieving groups |
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. | [optional] if omitted the server will use the default value of 500

### Return type

[**[ServerGroup]**](ServerGroup.md)

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

# **update_server_group**
> update_server_group(id, o, server_group_create_or_update_request)

Updates a new server group.

Updates a new server group.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import groups_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.server_group_create_or_update_request import ServerGroupCreateOrUpdateRequest
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | Server Group ID for the specified group
    o = 1 # int | Organization ID for the created group
    server_group_create_or_update_request = ServerGroupCreateOrUpdateRequest(
        name="name_example",
        refresh_interval=360,
        parent_server_group_id=1,
        ui_color="ui_color_example",
        notes="notes_example",
        enable_os_auto_update=True,
        enable_wsus=True,
        wsus_server="wsus_server_example",
        policies=[
            1,
        ],
    ) # ServerGroupCreateOrUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a new server group.
        api_instance.update_server_group(id, o, server_group_create_or_update_request)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling GroupsApi->update_server_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server Group ID for the specified group |
 **o** | **int**| Organization ID for the created group |
 **server_group_create_or_update_request** | [**ServerGroupCreateOrUpdateRequest**](ServerGroupCreateOrUpdateRequest.md)|  |

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
**204** | Successful Operation |  -  |
**400** | Invalid Request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

