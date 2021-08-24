# automox_console_sdk.WorkletsApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_community_worklet**](WorkletsApi.md#get_community_worklet) | **GET** /community-worklets/{id} | Retrieve Community Worklet by ID
[**get_community_worklets**](WorkletsApi.md#get_community_worklets) | **GET** /community-worklets | Retrieve Community Worklets

# **get_community_worklet**
> WorkletDetails get_community_worklet(id)

Retrieve Community Worklet by ID

Retrieves details for a specific Community Worklet by ID

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.WorkletsApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | The ID of the Community Worklet to retrieve

try:
    # Retrieve Community Worklet by ID
    api_response = api_instance.get_community_worklet(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkletsApi->get_community_worklet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the Community Worklet to retrieve | 

### Return type

[**WorkletDetails**](WorkletDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_community_worklets**
> Worklet get_community_worklets(page=page, limit=limit)

Retrieve Community Worklets

Retrieves a list of Community Worklets

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.WorkletsApi(automox_console_sdk.ApiClient(configuration))
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) (default to 0)
limit = 25 # int | A limit on the number of results to be returned, between 1 and 500 with a default of 25. Use with page parameter. (optional) (default to 25)

try:
    # Retrieve Community Worklets
    api_response = api_instance.get_community_worklets(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkletsApi->get_community_worklets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] [default to 0]
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500 with a default of 25. Use with page parameter. | [optional] [default to 25]

### Return type

[**Worklet**](Worklet.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

