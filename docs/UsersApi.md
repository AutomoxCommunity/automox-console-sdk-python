# automox_console_sdk.UsersApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decrypt_user_api_key**](UsersApi.md#decrypt_user_api_key) | **POST** /users/{userId}/api_keys/{id}/decrypt | Retrieves the API Key secret by ID
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{userId} | Retrieves a user by user ID
[**get_users**](UsersApi.md#get_users) | **GET** /users | List All Users With Access to a Given Organization

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
api_instance = automox_console_sdk.UsersApi(automox_console_sdk.ApiClient(configuration))
user_id = 56 # int | User ID of the user to retrieve API Keys
id = 56 # int | The ID of the API key to retrieve
o = 56 # int | The Organization of the user.

try:
    # Retrieves the API Key secret by ID
    api_response = api_instance.decrypt_user_api_key(user_id, id, o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->decrypt_user_api_key: %s\n" % e)
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

# **get_user_by_id**
> list[User] get_user_by_id(user_id, o=o)

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
o = 56 # int | The Organization whose users you wish to list. If you omit this value, the application will detect and use your default Organization. (optional)

try:
    # Retrieves a user by user ID
    api_response = api_instance.get_user_by_id(user_id, o=o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The User ID of the user to retrieve | 
 **o** | **int**| The Organization whose users you wish to list. If you omit this value, the application will detect and use your default Organization. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[User] get_users(o=o, page=page, limit=limit)

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
o = 56 # int | The Organization whose users you wish to list. If you omit this value, the application will detect and use your default Organization. (optional)
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) (default to 0)
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. (optional) (default to 500)

try:
    # List All Users With Access to a Given Organization
    api_response = api_instance.get_users(o=o, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| The Organization whose users you wish to list. If you omit this value, the application will detect and use your default Organization. | [optional] 
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] [default to 0]
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. | [optional] [default to 500]

### Return type

[**list[User]**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

