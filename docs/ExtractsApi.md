# automox_console_sdk.ExtractsApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_extract**](ExtractsApi.md#create_extract) | **POST** /data-extracts | Creates a new Data Extract.
[**download_data_extract**](ExtractsApi.md#download_data_extract) | **GET** /data-extracts/{id}/download | Download the CSV for a completed Data Extract job.
[**get_data_extract_by_id**](ExtractsApi.md#get_data_extract_by_id) | **GET** /data-extracts/{id} | Show a new Data Extract job.
[**get_data_extracts**](ExtractsApi.md#get_data_extracts) | **GET** /data-extracts | List all Data Extracts for an Organization

# **create_extract**
> list[DataExtract] create_extract(body, o)

Creates a new Data Extract.

Create a new Data Extract.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.ExtractsApi(automox_console_sdk.ApiClient(configuration))
body = automox_console_sdk.DataextractsBody() # DataextractsBody | Create Data Extract
o = 56 # int | Organization ID

try:
    # Creates a new Data Extract.
    api_response = api_instance.create_extract(body, o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->create_extract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataextractsBody**](DataextractsBody.md)| Create Data Extract | 
 **o** | **int**| Organization ID | 

### Return type

[**list[DataExtract]**](DataExtract.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_data_extract**
> Object download_data_extract(id, o)

Download the CSV for a completed Data Extract job.

Downloads the CSV for a completed Data Extract job. Triggers an automatic download of the CSV file.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.ExtractsApi(automox_console_sdk.ApiClient(configuration))
id = 789 # int | The ID of the Data Extract to download.
o = 789 # int | Organization ID

try:
    # Download the CSV for a completed Data Extract job.
    api_response = api_instance.download_data_extract(id, o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->download_data_extract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the Data Extract to download. | 
 **o** | **int**| Organization ID | 

### Return type

[**Object**](Object.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_extract_by_id**
> list[DataExtract] get_data_extract_by_id(id)

Show a new Data Extract job.

Retrieves a specific Data Extract job.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.ExtractsApi(automox_console_sdk.ApiClient(configuration))
id = 789 # int | The ID of the Data Extract you want to view.

try:
    # Show a new Data Extract job.
    api_response = api_instance.get_data_extract_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->get_data_extract_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the Data Extract you want to view. | 

### Return type

[**list[DataExtract]**](DataExtract.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_extracts**
> list[DataExtract] get_data_extracts(o, limit=limit, page=page, sort=sort, typeequals=typeequals, created_atgreater_than=created_atgreater_than, created_atlesser_than=created_atlesser_than, created_atgreater_than_or_equals=created_atgreater_than_or_equals, created_atlesser_than_or_equals=created_atlesser_than_or_equals, statusequals=statusequals, statusin=statusin)

List all Data Extracts for an Organization

List all Data extracts for an organization with ability to filter and sort results.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.ExtractsApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Limit response to a specific Automox organization
limit = 25 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 25. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 25)
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. Default: 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 0)
sort = ['sort_example'] # list[str] | The sort for the results. Options: `created_at:desc/asc` and `status:desc/asc`. Default: `created_at:desc` (optional)
typeequals = 'patch-history' # str | The type of Data Extracts to list. Options: `patch-history`. (optional) (default to patch-history)
created_atgreater_than = '2013-10-20T19:20:30+01:00' # datetime | Created at date is greater than the value submitted. If a time is not specified, greater_than will have a time of start of day. (optional)
created_atlesser_than = '2013-10-20T19:20:30+01:00' # datetime | Created at date is less than the value submitted. If a time is not specified, less_than will have a time of end of day. (optional)
created_atgreater_than_or_equals = '2013-10-20T19:20:30+01:00' # datetime | Created at date is greater than or equals the value submitted. If a time is not specified, greater_than_or_equals will have a time of start of day. (optional)
created_atlesser_than_or_equals = '2013-10-20T19:20:30+01:00' # datetime | Created at date is lesser than or equals the value submitted. If a time is not specified, less_than_or_equals will have a time of end of day. (optional)
statusequals = 'statusequals_example' # str | Find jobs with a specific status. Options: queued, running, complete, failed, canceled, expired (optional)
statusin = ['statusin_example'] # list[str] | Find jobs with one or more of these statuses. (optional)

try:
    # List all Data Extracts for an Organization
    api_response = api_instance.get_data_extracts(o, limit=limit, page=page, sort=sort, typeequals=typeequals, created_atgreater_than=created_atgreater_than, created_atlesser_than=created_atlesser_than, created_atgreater_than_or_equals=created_atgreater_than_or_equals, created_atlesser_than_or_equals=created_atlesser_than_or_equals, statusequals=statusequals, statusin=statusin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->get_data_extracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Limit response to a specific Automox organization | 
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 25. Use with &#x60;page&#x60; parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 25]
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. Default: 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The sort for the results. Options: &#x60;created_at:desc/asc&#x60; and &#x60;status:desc/asc&#x60;. Default: &#x60;created_at:desc&#x60; | [optional] 
 **typeequals** | **str**| The type of Data Extracts to list. Options: &#x60;patch-history&#x60;. | [optional] [default to patch-history]
 **created_atgreater_than** | **datetime**| Created at date is greater than the value submitted. If a time is not specified, greater_than will have a time of start of day. | [optional] 
 **created_atlesser_than** | **datetime**| Created at date is less than the value submitted. If a time is not specified, less_than will have a time of end of day. | [optional] 
 **created_atgreater_than_or_equals** | **datetime**| Created at date is greater than or equals the value submitted. If a time is not specified, greater_than_or_equals will have a time of start of day. | [optional] 
 **created_atlesser_than_or_equals** | **datetime**| Created at date is lesser than or equals the value submitted. If a time is not specified, less_than_or_equals will have a time of end of day. | [optional] 
 **statusequals** | **str**| Find jobs with a specific status. Options: queued, running, complete, failed, canceled, expired | [optional] 
 **statusin** | [**list[str]**](str.md)| Find jobs with one or more of these statuses. | [optional] 

### Return type

[**list[DataExtract]**](DataExtract.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

