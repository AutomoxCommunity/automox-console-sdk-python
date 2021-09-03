# automox_console_sdk.UsersApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decrypt_user_api_key**](UsersApi.md#decrypt_user_api_key) | **POST** /users/{userId}/api_keys/{id}/decrypt | Decrypt User API Key
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{userId} | Retrieves a user by user ID
[**get_users**](UsersApi.md#get_users) | **GET** /users | List All Users With Access to a Given Organization

# **decrypt_user_api_key**
> InlineResponse2002 decrypt_user_api_key(user_id, id, o)

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
api_instance = automox_console_sdk.UsersApi(automox_console_sdk.ApiClient(configuration))
user_id = 56 # int | The ID of the user to decrypt keys for.
id = 56 # int | The ID of the API key to decrypt
o = 56 # int | The Organization of the user.

try:
    # Decrypt User API Key
    api_response = api_instance.decrypt_user_api_key(user_id, id, o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->decrypt_user_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the user to decrypt keys for. | 
 **id** | **int**| The ID of the API key to decrypt | 
 **o** | **int**| The Organization of the user. | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> list[User] get_user_by_id(user_id, o)

Retrieves a user by user ID

Retrieves a user by user ID

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.UsersApi(automox_console_sdk.ApiClient(configuration))
user_id = 56 # int | The User ID of the user to retrieve
o = 56 # int | The Organization whose users you wish to list. If you omit this value, the application will detect and use your default Organization.

try:
    # Retrieves a user by user ID
    api_response = api_instance.get_user_by_id(user_id, o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The User ID of the user to retrieve | 
 **o** | **int**| The Organization whose users you wish to list. If you omit this value, the application will detect and use your default Organization. | 

### Return type

[**list[User]**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[User] get_users(o, page=page, limit=limit)

List All Users With Access to a Given Organization

Retrieves a list of all users with access to an organization

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.UsersApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | The Organization whose users you wish to list. If you omit this value, the application will detect and use your default Organization.
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 0)
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 500)

try:
    # List All Users With Access to a Given Organization
    api_response = api_instance.get_users(o, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| The Organization whose users you wish to list. If you omit this value, the application will detect and use your default Organization. | 
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 0]
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with &#x60;page&#x60; parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 500]

### Return type

[**list[User]**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

