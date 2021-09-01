# automox_console_sdk.ApprovalsApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_approvals**](ApprovalsApi.md#update_approvals) | **PUT** /approvals/{id} | Update a Manual Approval Record

# **update_approvals**
> list[SoftwareApprovals] update_approvals(id, body=body)

Update a Manual Approval Record

Update a manual approval record. Set the `manual_approval` attribute of approval object to `true` to approve a patch; set it to `false` to reject a patch.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.ApprovalsApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Approval ID. Contact [Automox Support](mailto:support@automox.com) for further assistance.
body = automox_console_sdk.ApprovalsIdBody() # ApprovalsIdBody |  (optional)

try:
    # Update a Manual Approval Record
    api_response = api_instance.update_approvals(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApprovalsApi->update_approvals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Approval ID. Contact [Automox Support](mailto:support@automox.com) for further assistance. | 
 **body** | [**ApprovalsIdBody**](ApprovalsIdBody.md)|  | [optional] 

### Return type

[**list[SoftwareApprovals]**](SoftwareApprovals.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](./README.md#documentation-for-models) [[Back to README]](../README.md)

