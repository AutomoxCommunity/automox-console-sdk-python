# automox_console_sdk.ReportsApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_needs_attention_report**](ReportsApi.md#get_needs_attention_report) | **GET** /reports/needs-attention | Needs Attention Report
[**get_non_compliance_report**](ReportsApi.md#get_non_compliance_report) | **GET** /reports/noncompliance | Non-Compliance Report
[**get_pre_patch_report**](ReportsApi.md#get_pre_patch_report) | **GET** /reports/prepatch | Pre-Patch Report

# **get_needs_attention_report**
> list[NeedsAttention] get_needs_attention_report(o, group_id=group_id, limit=limit, offset=offset)

Needs Attention Report

Retrieve a report containing devices that need attention.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.ReportsApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Organization ID. If omitted, results will include all organizations for the authenticated user.
group_id = 56 # int | Group ID. If omitted, results will include all groups for the authenticated user. (optional)
limit = 250 # int | Limit number of results returned per page. Typically used in combination with offset (optional) (default to 250)
offset = 250 # int | Specifies the offset. For example, if you are paging 250 at a time, you could specify 250 for the 2nd page and 500 for the 3rd, etc. (optional) (default to 250)

try:
    # Needs Attention Report
    api_response = api_instance.get_needs_attention_report(o, group_id=group_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_needs_attention_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID. If omitted, results will include all organizations for the authenticated user. | 
 **group_id** | **int**| Group ID. If omitted, results will include all groups for the authenticated user. | [optional] 
 **limit** | **int**| Limit number of results returned per page. Typically used in combination with offset | [optional] [default to 250]
 **offset** | **int**| Specifies the offset. For example, if you are paging 250 at a time, you could specify 250 for the 2nd page and 500 for the 3rd, etc. | [optional] [default to 250]

### Return type

[**list[NeedsAttention]**](NeedsAttention.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_compliance_report**
> list[NonCompliant] get_non_compliance_report(o, group_id=group_id, limit=limit, offset=offset)

Non-Compliance Report

Retrieve the non-compliant devices report. This endpoint is deprecated. Please use [GET /reports/needs-attention](/openapi/axconsole/operation/getNeedsAttentionReport) instead.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.ReportsApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Organization ID. If omitted, results will include all organizations for the authenticated user.
group_id = 56 # int | Group ID. If omitted, results will include all groups for the authenticated user. (optional)
limit = 250 # int | Limit number of results returned per page. Typically used in combination with offset (optional) (default to 250)
offset = 250 # int | Specifies the offset. For example, if you are paging 250 at a time, you could specify 250 for the 2nd page and 500 for the 3rd, etc. (optional) (default to 250)

try:
    # Non-Compliance Report
    api_response = api_instance.get_non_compliance_report(o, group_id=group_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_non_compliance_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID. If omitted, results will include all organizations for the authenticated user. | 
 **group_id** | **int**| Group ID. If omitted, results will include all groups for the authenticated user. | [optional] 
 **limit** | **int**| Limit number of results returned per page. Typically used in combination with offset | [optional] [default to 250]
 **offset** | **int**| Specifies the offset. For example, if you are paging 250 at a time, you could specify 250 for the 2nd page and 500 for the 3rd, etc. | [optional] [default to 250]

### Return type

[**list[NonCompliant]**](NonCompliant.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pre_patch_report**
> PrePatch get_pre_patch_report(o, group_id=group_id, limit=limit, offset=offset)

Pre-Patch Report

Retrieve the pre-patch report.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.ReportsApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Organization ID. If omitted, results will include all organizations for the authenticated user.
group_id = 56 # int | The ID of the server group for limiting results (optional)
limit = 250 # int | Limit number of results returned per page. Typically used in combination with offset (optional) (default to 250)
offset = 250 # int | Specifies the offset. For example, if you are paging 250 at a time, you could specify 250 for the 2nd page and 500 for the 3rd, etc. (optional) (default to 250)

try:
    # Pre-Patch Report
    api_response = api_instance.get_pre_patch_report(o, group_id=group_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_pre_patch_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID. If omitted, results will include all organizations for the authenticated user. | 
 **group_id** | **int**| The ID of the server group for limiting results | [optional] 
 **limit** | **int**| Limit number of results returned per page. Typically used in combination with offset | [optional] [default to 250]
 **offset** | **int**| Specifies the offset. For example, if you are paging 250 at a time, you could specify 250 for the 2nd page and 500 for the 3rd, etc. | [optional] [default to 250]

### Return type

[**PrePatch**](PrePatch.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

