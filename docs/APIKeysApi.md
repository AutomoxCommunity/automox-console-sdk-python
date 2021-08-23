# automox_console_sdk.APIKeysApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_api_key**](APIKeysApi.md#create_user_api_key) | **POST** /users/{userId}/api_keys | Creates an API key for a user
[**decrypt_user_api_key**](APIKeysApi.md#decrypt_user_api_key) | **POST** /users/{userId}/api_keys/{id}/decrypt | Retrieves the API Key secret by ID
[**delete_user_api_key**](APIKeysApi.md#delete_user_api_key) | **DELETE** /users/{userId}/api_keys/{id} | Deletes an API Key by ID
[**get_organization_api_keys**](APIKeysApi.md#get_organization_api_keys) | **GET** /orgs/{id}/api_keys | List All API Keys for Organization
[**get_user_api_key**](APIKeysApi.md#get_user_api_key) | **GET** /users/{userId}/api_keys/{id} | Retrieves an API key object by ID
[**get_user_api_keys**](APIKeysApi.md#get_user_api_keys) | **GET** /users/{userId}/api_keys | Retrieves a list of API key objects for a user
[**update_user_api_key**](APIKeysApi.md#update_user_api_key) | **PUT** /users/{userId}/api_keys/{id} | Update an API Key by ID


# **create_user_api_key**
> ApiKey create_user_api_key(user_id, o)

Creates an API key for a user

Creates an API key for a user

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import api_keys_api
from automox_console_sdk.model.api_key import ApiKey
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
    api_instance = api_keys_api.APIKeysApi(api_client)
    user_id = 1 # int | User ID of the user to create an API key
    o = 1 # int | The Organization of the user.
    unknown_base_type = {
        name="name_example",
        expires_at="expires_at_example",
    } # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates an API key for a user
        api_response = api_instance.create_user_api_key(user_id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling APIKeysApi->create_user_api_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates an API key for a user
        api_response = api_instance.create_user_api_key(user_id, o, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling APIKeysApi->create_user_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the user to create an API key |
 **o** | **int**| The Organization of the user. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **decrypt_user_api_key**
> dict decrypt_user_api_key(user_id, id, o)

Retrieves the API Key secret by ID

Retrieves the API Key secret by ID

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import api_keys_api
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
    api_instance = api_keys_api.APIKeysApi(api_client)
    user_id = 1 # int | User ID of the user to retrieve API Keys
    id = 1 # int | The ID of the API key to retrieve
    o = 1 # int | The Organization of the user.

    # example passing only required values which don't have defaults set
    try:
        # Retrieves the API Key secret by ID
        api_response = api_instance.decrypt_user_api_key(user_id, id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling APIKeysApi->decrypt_user_api_key: %s\n" % e)
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

# **delete_user_api_key**
> delete_user_api_key(user_id, id, o, )

Deletes an API Key by ID

Deletes an API Key by ID

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import api_keys_api
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
    api_instance = api_keys_api.APIKeysApi(api_client)
    user_id = 1 # int | User ID of the user to delete API Key for
    id = 1 # int | The ID of the API key to delete
    o = 1 # int | The Organization of the user.

    # example passing only required values which don't have defaults set
    try:
        # Deletes an API Key by ID
        api_instance.delete_user_api_key(user_id, id, o, )
    except automox_console_sdk.ApiException as e:
        print("Exception when calling APIKeysApi->delete_user_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the user to delete API Key for |
 **id** | **int**| The ID of the API key to delete |
 **o** | **int**| The Organization of the user. |
 **content_type** | **str**| Specify JSON as the content type for body parameters | defaults to "application/json"

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
**204** | Successful Operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |
**404** | Entity not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_api_keys**
> InlineResponse200 get_organization_api_keys(id)

List All API Keys for Organization

You must have Full Administrator privileges for this endpoint

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import api_keys_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.inline_response200 import InlineResponse200
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
    api_instance = api_keys_api.APIKeysApi(api_client)
    id = 1 # int | Organization ID for retrieving API Keys
    limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. (optional) if omitted the server will use the default value of 500
    page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List All API Keys for Organization
        api_response = api_instance.get_organization_api_keys(id)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling APIKeysApi->get_organization_api_keys: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All API Keys for Organization
        api_response = api_instance.get_organization_api_keys(id, limit=limit, page=page)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling APIKeysApi->get_organization_api_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Organization ID for retrieving API Keys |
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. | [optional] if omitted the server will use the default value of 500
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] if omitted the server will use the default value of 0

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **get_user_api_key**
> ApiKey get_user_api_key(user_id, id, o)

Retrieves an API key object by ID

Retrieves an API key object by ID

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import api_keys_api
from automox_console_sdk.model.api_key import ApiKey
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
    api_instance = api_keys_api.APIKeysApi(api_client)
    user_id = 1 # int | User ID of the user to retrieve API key objects
    id = 1 # int | The ID of the API key object to retrieve
    o = 1 # int | The Organization of the user.

    # example passing only required values which don't have defaults set
    try:
        # Retrieves an API key object by ID
        api_response = api_instance.get_user_api_key(user_id, id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling APIKeysApi->get_user_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the user to retrieve API key objects |
 **id** | **int**| The ID of the API key object to retrieve |
 **o** | **int**| The Organization of the user. |

### Return type

[**ApiKey**](ApiKey.md)

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

# **get_user_api_keys**
> InlineResponse2001 get_user_api_keys(user_id, o)

Retrieves a list of API key objects for a user

Retrieves a list of API key objects for a user

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import api_keys_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.inline_response2001 import InlineResponse2001
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
    api_instance = api_keys_api.APIKeysApi(api_client)
    user_id = 1 # int | User ID of the user to retrieve API key objects
    o = 1 # int | The Organization of the user.
    page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) if omitted the server will use the default value of 0
    limit = 500 # int | A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. (optional) if omitted the server will use the default value of 500

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a list of API key objects for a user
        api_response = api_instance.get_user_api_keys(user_id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling APIKeysApi->get_user_api_keys: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieves a list of API key objects for a user
        api_response = api_instance.get_user_api_keys(user_id, o, page=page, limit=limit)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling APIKeysApi->get_user_api_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the user to retrieve API key objects |
 **o** | **int**| The Organization of the user. |
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. | [optional] if omitted the server will use the default value of 500

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **update_user_api_key**
> ApiKey update_user_api_key(user_id, id, o)

Update an API Key by ID

Update an API Key by ID

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import api_keys_api
from automox_console_sdk.model.api_key import ApiKey
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
    api_instance = api_keys_api.APIKeysApi(api_client)
    user_id = 1 # int | User ID of the user to update keys for
    id = 1 # int | The ID of the API key to update
    o = 1 # int | The Organization of the key.
    unknown_base_type = {
        is_enabled=True,
    } # UNKNOWN_BASE_TYPE | The API Key updates (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an API Key by ID
        api_response = api_instance.update_user_api_key(user_id, id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling APIKeysApi->update_user_api_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an API Key by ID
        api_response = api_instance.update_user_api_key(user_id, id, o, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling APIKeysApi->update_user_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the user to update keys for |
 **id** | **int**| The ID of the API key to update |
 **o** | **int**| The Organization of the key. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| The API Key updates | [optional]

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

