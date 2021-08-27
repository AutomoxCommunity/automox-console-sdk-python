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
> ApiKey create_user_api_key(o, user_id, body=body)

Creates an API key for a user

Creates an API key for a user

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.APIKeysApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | The Organization of the user.
user_id = 56 # int | User ID of the user to create an API key
body = automox_console_sdk.UserIdApiKeysBody() # UserIdApiKeysBody |  (optional)

try:
    # Creates an API key for a user
    api_response = api_instance.create_user_api_key(o, user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->create_user_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| The Organization of the user. | 
 **user_id** | **int**| User ID of the user to create an API key | 
 **body** | [**UserIdApiKeysBody**](UserIdApiKeysBody.md)|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decrypt_user_api_key**
> InlineResponse2002 decrypt_user_api_key(user_id, id, o)

Retrieves the API Key secret by ID

Retrieves the API Key secret by ID

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.APIKeysApi(automox_console_sdk.ApiClient(configuration))
user_id = 56 # int | User ID of the user to retrieve API Keys
id = 56 # int | The ID of the API key to retrieve
o = 56 # int | The Organization of the user.

try:
    # Retrieves the API Key secret by ID
    api_response = api_instance.decrypt_user_api_key(user_id, id, o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->decrypt_user_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the user to retrieve API Keys | 
 **id** | **int**| The ID of the API key to retrieve | 
 **o** | **int**| The Organization of the user. | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_api_key**
> delete_user_api_key(user_id, id, o, content_type)

Deletes an API Key by ID

Deletes an API Key by ID

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.APIKeysApi(automox_console_sdk.ApiClient(configuration))
user_id = 56 # int | User ID of the user to delete API Key for
id = 56 # int | The ID of the API key to delete
o = 56 # int | The Organization of the user.
content_type = 'application/json' # str | Specify JSON as the content type for body parameters (default to application/json)

try:
    # Deletes an API Key by ID
    api_instance.delete_user_api_key(user_id, id, o, content_type)
except ApiException as e:
    print("Exception when calling APIKeysApi->delete_user_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the user to delete API Key for | 
 **id** | **int**| The ID of the API key to delete | 
 **o** | **int**| The Organization of the user. | 
 **content_type** | **str**| Specify JSON as the content type for body parameters | [default to application/json]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_api_keys**
> InlineResponse200 get_organization_api_keys(id, limit=limit, page=page)

List All API Keys for Organization

You must have Full Administrator privileges for this endpoint

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.APIKeysApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Organization ID for retrieving API Keys
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. (optional) (default to 500)
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) (default to 0)

try:
    # List All API Keys for Organization
    api_response = api_instance.get_organization_api_keys(id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->get_organization_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Organization ID for retrieving API Keys | 
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. | [optional] [default to 500]
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] [default to 0]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_api_key**
> ApiKey get_user_api_key(user_id, id, o)

Retrieves an API key object by ID

Retrieves an API key object by ID

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.APIKeysApi(automox_console_sdk.ApiClient(configuration))
user_id = 56 # int | User ID of the user to retrieve API key objects
id = 56 # int | The ID of the API key object to retrieve
o = 56 # int | The Organization of the user.

try:
    # Retrieves an API key object by ID
    api_response = api_instance.get_user_api_key(user_id, id, o)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_api_keys**
> InlineResponse2001 get_user_api_keys(user_id, o, page=page, limit=limit)

Retrieves a list of API key objects for a user

Retrieves a list of API key objects for a user

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.APIKeysApi(automox_console_sdk.ApiClient(configuration))
user_id = 56 # int | User ID of the user to retrieve API key objects
o = 56 # int | The Organization of the user.
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) (default to 0)
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. (optional) (default to 500)

try:
    # Retrieves a list of API key objects for a user
    api_response = api_instance.get_user_api_keys(user_id, o, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->get_user_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the user to retrieve API key objects | 
 **o** | **int**| The Organization of the user. | 
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] [default to 0]
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. | [optional] [default to 500]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_api_key**
> ApiKey update_user_api_key(o, user_id, id, body=body)

Update an API Key by ID

Update an API Key by ID

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.APIKeysApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | The Organization of the key.
user_id = 56 # int | User ID of the user to update keys for
id = 56 # int | The ID of the API key to update
body = automox_console_sdk.ApiKeysIdBody() # ApiKeysIdBody | The API Key updates (optional)

try:
    # Update an API Key by ID
    api_response = api_instance.update_user_api_key(o, user_id, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->update_user_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| The Organization of the key. | 
 **user_id** | **int**| User ID of the user to update keys for | 
 **id** | **int**| The ID of the API key to update | 
 **body** | [**ApiKeysIdBody**](ApiKeysIdBody.md)| The API Key updates | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

