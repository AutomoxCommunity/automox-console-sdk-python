# automox_console_sdk.UsersApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decrypt_user_api_key**](UsersApi.md#decrypt_user_api_key) | **POST** /users/{userId}/api_keys/{id}/decrypt | Retrieves the API Key secret by ID
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{userId} | Retrieves a user by user ID
[**get_users**](UsersApi.md#get_users) | **GET** /users | List All Users With Access to a Given Organization


# **decrypt_user_api_key**
> dict decrypt_user_api_key(user_id, id, o)

Retrieves the API Key secret by ID

Retrieves the API Key secret by ID

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    user_id = 1 # int | User ID of the user to retrieve API Keys
    id = 1 # int | The ID of the API key to retrieve
    o = 1 # int | The Organization of the user.

    # example passing only required values which don't have defaults set
    try:
        # Retrieves the API Key secret by ID
        api_response = api_instance.decrypt_user_api_key(user_id, id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling UsersApi->decrypt_user_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the user to retrieve API Keys |
 **id** | **int**| The ID of the API key to retrieve |
 **o** | **int**| The Organization of the user. |

### Return type

**dict**

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

# **get_user_by_id**
> [User] get_user_by_id(user_id)

Retrieves a user by user ID

Retrieves a user by user ID

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import users_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    user_id = 1 # int | The User ID of the user to retrieve
    o = 1 # int | The Organization whose users you wish to list. If you omit this value, the application will detect and use your default Organization. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a user by user ID
        api_response = api_instance.get_user_by_id(user_id)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieves a user by user ID
        api_response = api_instance.get_user_by_id(user_id, o=o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The User ID of the user to retrieve |
 **o** | **int**| The Organization whose users you wish to list. If you omit this value, the application will detect and use your default Organization. | [optional]

### Return type

[**[User]**](User.md)

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

# **get_users**
> [User] get_users()

List All Users With Access to a Given Organization

Retrieves a list of all users with access to an organization

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import users_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    o = 1 # int | The Organization whose users you wish to list. If you omit this value, the application will detect and use your default Organization. (optional)
    page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) if omitted the server will use the default value of 0
    limit = 500 # int | A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. (optional) if omitted the server will use the default value of 500

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Users With Access to a Given Organization
        api_response = api_instance.get_users(o=o, page=page, limit=limit)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| The Organization whose users you wish to list. If you omit this value, the application will detect and use your default Organization. | [optional]
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. | [optional] if omitted the server will use the default value of 500

### Return type

[**[User]**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |
**404** | Entity not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

