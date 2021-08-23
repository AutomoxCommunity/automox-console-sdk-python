# automox_console_sdk.ApprovalsApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_approvals**](ApprovalsApi.md#update_approvals) | **PUT** /approvals/{id} | Update a Manual Approval Record


# **update_approvals**
> [SoftwareApprovals] update_approvals(id)

Update a Manual Approval Record

Update a manual approval record. Set the `manual_approval` attribute of approval object to `true` to approve a patch; set it to `false` to reject a patch.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import approvals_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.software_approvals import SoftwareApprovals
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
    api_instance = approvals_api.ApprovalsApi(api_client)
    id = 1 # int | Approval ID. Contact [Automox Support](mailto:support@automox.com) for further assistance.
    unknown_base_type = {
        manual_approval=True,
    } # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Manual Approval Record
        api_response = api_instance.update_approvals(id)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling ApprovalsApi->update_approvals: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Manual Approval Record
        api_response = api_instance.update_approvals(id, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling ApprovalsApi->update_approvals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Approval ID. Contact [Automox Support](mailto:support@automox.com) for further assistance. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

[**[SoftwareApprovals]**](SoftwareApprovals.md)

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
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

