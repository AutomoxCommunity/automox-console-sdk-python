# automox_console_sdk.ExtractsApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_extract**](ExtractsApi.md#create_extract) | **POST** /data-extracts | Creates a new Data Extract.
[**download_data_extract**](ExtractsApi.md#download_data_extract) | **GET** /data-extracts/{id}/download | Download the CSV for a completed Data Extract job.
[**get_data_extract_by_id**](ExtractsApi.md#get_data_extract_by_id) | **GET** /data-extracts/{id} | Show a new Data Extract job.
[**get_data_extracts**](ExtractsApi.md#get_data_extracts) | **GET** /data-extracts | List all Data Extracts for an Organization


# **create_extract**
> [DataExtract] create_extract(o, unknown_base_type)

Creates a new Data Extract.

Create a new Data Extract.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import extracts_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.data_extract import DataExtract
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
    api_instance = extracts_api.ExtractsApi(api_client)
    o = 1 # int | Organization ID
    unknown_base_type = {
        type="patch-history",
        parameters={
            start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        },
    } # UNKNOWN_BASE_TYPE | Create Data Extract

    # example passing only required values which don't have defaults set
    try:
        # Creates a new Data Extract.
        api_response = api_instance.create_extract(o, unknown_base_type)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling ExtractsApi->create_extract: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Create Data Extract |

### Return type

[**[DataExtract]**](DataExtract.md)

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

# **download_data_extract**
> bool, date, datetime, dict, float, int, list, str, none_type download_data_extract(id, o)

Download the CSV for a completed Data Extract job.

Downloads the CSV for a completed Data Extract job. Triggers an automatic download of the CSV file.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import extracts_api
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
    api_instance = extracts_api.ExtractsApi(api_client)
    id = 1 # int | The ID of the Data Extract to download.
    o = 1 # int | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Download the CSV for a completed Data Extract job.
        api_response = api_instance.download_data_extract(id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling ExtractsApi->download_data_extract: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the Data Extract to download. |
 **o** | **int**| Organization ID |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Downloads the extract file automatically. |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |
**404** | Entity not found |  -  |
**410** | Returned when the extract download is no longer available. |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_extract_by_id**
> [DataExtract] get_data_extract_by_id(id)

Show a new Data Extract job.

Retrieves a specific Data Extract job.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import extracts_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.data_extract import DataExtract
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
    api_instance = extracts_api.ExtractsApi(api_client)
    id = 1 # int | The ID of the Data Extract you want to view.

    # example passing only required values which don't have defaults set
    try:
        # Show a new Data Extract job.
        api_response = api_instance.get_data_extract_by_id(id)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling ExtractsApi->get_data_extract_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the Data Extract you want to view. |

### Return type

[**[DataExtract]**](DataExtract.md)

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

# **get_data_extracts**
> [DataExtract] get_data_extracts(o)

List all Data Extracts for an Organization

List all Data extracts for an organization with ability to filter and sort results.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import extracts_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.data_extract import DataExtract
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
    api_instance = extracts_api.ExtractsApi(api_client)
    o = 1 # int | Limit response to a specific Automox organization
    limit = 25 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 25. Use with page parameter. (optional) if omitted the server will use the default value of 25
    page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. Default: 0. (optional) if omitted the server will use the default value of 0
    sort = [
        "created_at:desc",
    ] # [str] | The sort for the results. Options: created_at:desc/asc and status:desc/asc. Default: created_at:desc (optional)
    typeequals = "patch-history" # str | The type of Data Extracts to list. Options: data-extract. (optional) if omitted the server will use the default value of "patch-history"
    created_atgreater_than = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Created at date is greater than the value submitted. If a time is not specified, greater_than will have a time of start of day. (optional)
    created_atlesser_than = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Created at date is less than the value submitted. If a time is not specified, less_than will have a time of end of day. (optional)
    created_atgreater_than_or_equals = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Created at date is greater than or equals the value submitted. If a time is not specified, greater_than_or_equals will have a time of start of day. (optional)
    created_atlesser_than_or_equals = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Created at date is lesser than or equals the value submitted. If a time is not specified, less_than_or_equals will have a time of end of day. (optional)
    statusequals = "queued" # str | Find jobs with a specific status. Options: queued, running, complete, failed, canceled, expired (optional)
    statusin = [
        "queued",
    ] # [str] | Find jobs with one or more of these statuses. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all Data Extracts for an Organization
        api_response = api_instance.get_data_extracts(o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling ExtractsApi->get_data_extracts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all Data Extracts for an Organization
        api_response = api_instance.get_data_extracts(o, limit=limit, page=page, sort=sort, typeequals=typeequals, created_atgreater_than=created_atgreater_than, created_atlesser_than=created_atlesser_than, created_atgreater_than_or_equals=created_atgreater_than_or_equals, created_atlesser_than_or_equals=created_atlesser_than_or_equals, statusequals=statusequals, statusin=statusin)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling ExtractsApi->get_data_extracts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Limit response to a specific Automox organization |
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 25. Use with page parameter. | [optional] if omitted the server will use the default value of 25
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. Default: 0. | [optional] if omitted the server will use the default value of 0
 **sort** | **[str]**| The sort for the results. Options: created_at:desc/asc and status:desc/asc. Default: created_at:desc | [optional]
 **typeequals** | **str**| The type of Data Extracts to list. Options: data-extract. | [optional] if omitted the server will use the default value of "patch-history"
 **created_atgreater_than** | **datetime**| Created at date is greater than the value submitted. If a time is not specified, greater_than will have a time of start of day. | [optional]
 **created_atlesser_than** | **datetime**| Created at date is less than the value submitted. If a time is not specified, less_than will have a time of end of day. | [optional]
 **created_atgreater_than_or_equals** | **datetime**| Created at date is greater than or equals the value submitted. If a time is not specified, greater_than_or_equals will have a time of start of day. | [optional]
 **created_atlesser_than_or_equals** | **datetime**| Created at date is lesser than or equals the value submitted. If a time is not specified, less_than_or_equals will have a time of end of day. | [optional]
 **statusequals** | **str**| Find jobs with a specific status. Options: queued, running, complete, failed, canceled, expired | [optional]
 **statusin** | **[str]**| Find jobs with one or more of these statuses. | [optional]

### Return type

[**[DataExtract]**](DataExtract.md)

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

