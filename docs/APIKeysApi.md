# automox_console_sdk.APIKeysApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_api_key**](APIKeysApi.md#create_user_api_key) | **POST** /users/{userId}/api_keys | Creates an API key for a user
[**decrypt_user_api_key**](APIKeysApi.md#decrypt_user_api_key) | **POST** /users/{userId}/api_keys/{id}/decrypt | Decrypt User API Key
[**delete_user_api_key**](APIKeysApi.md#delete_user_api_key) | **DELETE** /users/{userId}/api_keys/{id} | Deletes an API Key by ID
[**get_organization_api_keys**](APIKeysApi.md#get_organization_api_keys) | **GET** /orgs/{id}/api_keys | List All API Keys for Organization
[**get_user_api_key**](APIKeysApi.md#get_user_api_key) | **GET** /users/{userId}/api_keys/{id} | Retrieves an API key object by ID
[**get_user_api_keys**](APIKeysApi.md#get_user_api_keys) | **GET** /users/{userId}/api_keys | Retrieves a list of API key objects for a user
[**update_user_api_key**](APIKeysApi.md#update_user_api_key) | **PUT** /users/{userId}/api_keys/{id} | Update an API Key by ID

# **create_user_api_key**
> ApiKey create_user_api_key(o, user_id, body=body)

Creates an API key for a user

**Note:** A user is only allowed to have a maximum of 10 active keys per organization at any given time.

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
> InlineResponse2003 decrypt_user_api_key(user_id, id, o)

Decrypt User API Key

This endpoint allows you to decrypt the API key for an authenticated user.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.APIKeysApi(automox_console_sdk.ApiClient(configuration))
user_id = 56 # int | The ID of the user to decrypt keys for.
id = 56 # int | The ID of the API key to decrypt
o = 56 # int | The Organization of the user.

try:
    # Decrypt User API Key
    api_response = api_instance.decrypt_user_api_key(user_id, id, o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->decrypt_user_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the user to decrypt keys for. | 
 **id** | **int**| The ID of the API key to decrypt | 
 **o** | **int**| The Organization of the user. | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_api_key**
> delete_user_api_key(user_id, id, o)

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
o = 56 # int | The Organization whose keys you want to delete.

try:
    # Deletes an API Key by ID
    api_instance.delete_user_api_key(user_id, id, o)
except ApiException as e:
    print("Exception when calling APIKeysApi->delete_user_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID of the user to delete API Key for | 
 **id** | **int**| The ID of the API key to delete | 
 **o** | **int**| The Organization whose keys you want to delete. | 

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

**PREREQUISITES:** You must have **Full Administrator** privileges! This endpoint allows you to list all keys for an organization.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.APIKeysApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | The ID of the organization to list keys for.
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 500)
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 0)

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
 **id** | **int**| The ID of the organization to list keys for. | 
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with &#x60;page&#x60; parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 500]
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 0]

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

Note: The response does not contain the encrypted portion of the key. See [Decrypt User API Key](/openapi/axconsole/operation/decryptUserApiKey/)  

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.APIKeysApi(automox_console_sdk.ApiClient(configuration))
user_id = 56 # int | The ID of the user to view keys for.
id = 56 # int | The ID of the API key object to retrieve
o = 56 # int | The Organization whose keys you want to view.

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
 **user_id** | **int**| The ID of the user to view keys for. | 
 **id** | **int**| The ID of the API key object to retrieve | 
 **o** | **int**| The Organization whose keys you want to view. | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_api_keys**
> InlineResponse2002 get_user_api_keys(user_id, o, page=page, limit=limit)

Retrieves a list of API key objects for a user

Returns a list of API keys for the given user under the requested organization. This response does not include the encrypted portion of the key.

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
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 0)
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 500)

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
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 0]
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 500]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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
body = automox_console_sdk.ApiKeysIdBody() # ApiKeysIdBody | Enable/Disable API key (optional)

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
 **body** | [**ApiKeysIdBody**](ApiKeysIdBody.md)| Enable/Disable API key | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

