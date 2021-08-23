# automox_console_sdk.ReportsApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_non_compliance_report**](ReportsApi.md#get_non_compliance_report) | **GET** /reports/noncompliance | Non-Compliance Report
[**get_pre_patch_report**](ReportsApi.md#get_pre_patch_report) | **GET** /reports/prepatch | Pre-Patch Report


# **get_non_compliance_report**
> [NonCompliant] get_non_compliance_report()

Non-Compliance Report

Retrieve the non-compliant devices report.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import reports_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.non_compliant import NonCompliant
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
    api_instance = reports_api.ReportsApi(api_client)
    o = 1 # int | Organization ID. If omitted, results will include all organizations for the authenticated user. (optional)
    group_id = 1 # int | Group ID. If omitted, results will include all groups for the authenticated user. (optional)
    limit = 250 # int | Limit number of results returned per page. Typically used in combination with offset (optional) if omitted the server will use the default value of 250
    offset = 250 # int | Specifies the offset. For example, if you are paging 250 at a time, you could specify 250 for the 2nd page and 500 for the 3rd, etc. (optional) if omitted the server will use the default value of 250

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Non-Compliance Report
        api_response = api_instance.get_non_compliance_report(o=o, group_id=group_id, limit=limit, offset=offset)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling ReportsApi->get_non_compliance_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID. If omitted, results will include all organizations for the authenticated user. | [optional]
 **group_id** | **int**| Group ID. If omitted, results will include all groups for the authenticated user. | [optional]
 **limit** | **int**| Limit number of results returned per page. Typically used in combination with offset | [optional] if omitted the server will use the default value of 250
 **offset** | **int**| Specifies the offset. For example, if you are paging 250 at a time, you could specify 250 for the 2nd page and 500 for the 3rd, etc. | [optional] if omitted the server will use the default value of 250

### Return type

[**[NonCompliant]**](NonCompliant.md)

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

# **get_pre_patch_report**
> PrePatch get_pre_patch_report()

Pre-Patch Report

Retrieve the pre-patch report.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import reports_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.pre_patch import PrePatch
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
    api_instance = reports_api.ReportsApi(api_client)
    o = 1 # int | Organization ID. If omitted, results will include all organizations for the authenticated user. (optional)
    group_id = 1 # int | The ID of the server group for limiting results (optional)
    limit = 250 # int | Limit number of results returned per page. Typically used in combination with offset (optional) if omitted the server will use the default value of 250
    offset = 250 # int | Specifies the offset. For example, if you are paging 250 at a time, you could specify 250 for the 2nd page and 500 for the 3rd, etc. (optional) if omitted the server will use the default value of 250

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Pre-Patch Report
        api_response = api_instance.get_pre_patch_report(o=o, group_id=group_id, limit=limit, offset=offset)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling ReportsApi->get_pre_patch_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID. If omitted, results will include all organizations for the authenticated user. | [optional]
 **group_id** | **int**| The ID of the server group for limiting results | [optional]
 **limit** | **int**| Limit number of results returned per page. Typically used in combination with offset | [optional] if omitted the server will use the default value of 250
 **offset** | **int**| Specifies the offset. For example, if you are paging 250 at a time, you could specify 250 for the 2nd page and 500 for the 3rd, etc. | [optional] if omitted the server will use the default value of 250

### Return type

[**PrePatch**](PrePatch.md)

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

