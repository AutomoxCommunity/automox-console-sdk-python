# automox_console_sdk.PoliciesApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy**](PoliciesApi.md#create_policy) | **POST** /policies | Create a New Policy
[**delete_policy**](PoliciesApi.md#delete_policy) | **DELETE** /policies/{id} | Delete Specific Policy Object
[**execute_policy**](PoliciesApi.md#execute_policy) | **POST** /policies/{id}/action | Schedule a Policy for Immediate Remediation
[**generate_policy_device_filter_preview**](PoliciesApi.md#generate_policy_device_filter_preview) | **POST** /policies/device-filters-preview | Policy Device Filters Preview
[**get_policies**](PoliciesApi.md#get_policies) | **GET** /policies | List All Policy Objects
[**get_policy**](PoliciesApi.md#get_policy) | **GET** /policies/{id} | List Specific Policy Object
[**get_policy_stats**](PoliciesApi.md#get_policy_stats) | **GET** /policystats | List Policy Compliance Stats
[**update_policy**](PoliciesApi.md#update_policy) | **PUT** /policies/{id} | Updates a specific policy object for the authenticated user.

# **create_policy**
> list[Object] create_policy(o, body=body)

Create a New Policy

Creates a new policy for a specified organization. For more info on filter types and scheduling, see [Policy and Device Filters, and Scheduling](/developer-portal/policy_filters_schedule).

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.PoliciesApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Organization ID for the specified policy.
body = automox_console_sdk.Object() # Object |  (optional)

try:
    # Create a New Policy
    api_response = api_instance.create_policy(o, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID for the specified policy. | 
 **body** | [**Object**](Object.md)|  | [optional] 

### Return type

[**list[Object]**](Object.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(id, o)

Delete Specific Policy Object

Deletes a specific policy object for the authenticated user.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.PoliciesApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Policy ID for the specified policy
o = 56 # int | Organization ID for the specified policy

try:
    # Delete Specific Policy Object
    api_instance.delete_policy(id, o)
except ApiException as e:
    print("Exception when calling PoliciesApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Policy ID for the specified policy | 
 **o** | **int**| Organization ID for the specified policy | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_policy**
> execute_policy(id, o, action, server_id=server_id)

Schedule a Policy for Immediate Remediation

Schedule a policy for immediate remediation.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.PoliciesApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Policy ID for the specified policy
o = 56 # int | Organization ID for the specified policy
action = 'action_example' # str | Specify the action to be taken. Possible values: `remediateAll`, `remediateServer` Format: `action=remediateServer`
server_id = 56 # int | Specify the specific Server to run the policy for. Only applicable when action is set to \"remediateServer\" Format: serverId=123456 (optional)

try:
    # Schedule a Policy for Immediate Remediation
    api_instance.execute_policy(id, o, action, server_id=server_id)
except ApiException as e:
    print("Exception when calling PoliciesApi->execute_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Policy ID for the specified policy | 
 **o** | **int**| Organization ID for the specified policy | 
 **action** | **str**| Specify the action to be taken. Possible values: &#x60;remediateAll&#x60;, &#x60;remediateServer&#x60; Format: &#x60;action&#x3D;remediateServer&#x60; | 
 **server_id** | **int**| Specify the specific Server to run the policy for. Only applicable when action is set to \&quot;remediateServer\&quot; Format: serverId&#x3D;123456 | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_policy_device_filter_preview**
> list[PolicyDeviceFiltersOutput] generate_policy_device_filter_preview(body, o, page=page, limit=limit)

Policy Device Filters Preview

Generate a preview of the list of devices that matches the provided device filter set. For more information, see [Policy and Device Filters, and Scheduling](/developer-portal/policy_filters_schedule).

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.PoliciesApi(automox_console_sdk.ApiClient(configuration))
body = automox_console_sdk.PolicyDeviceFiltersPreview() # PolicyDeviceFiltersPreview | 
o = 56 # int | Organization ID. If omitted, results will include all organizations for the authenticated user.
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 0)
limit = 25 # int | A limit on the number of results to be returned, between 1 and 200 with a default of 25. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 25)

try:
    # Policy Device Filters Preview
    api_response = api_instance.generate_policy_device_filter_preview(body, o, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->generate_policy_device_filter_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyDeviceFiltersPreview**](PolicyDeviceFiltersPreview.md)|  | 
 **o** | **int**| Organization ID. If omitted, results will include all organizations for the authenticated user. | 
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 0]
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 200 with a default of 25. Use with &#x60;page&#x60; parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 25]

### Return type

[**list[PolicyDeviceFiltersOutput]**](PolicyDeviceFiltersOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies**
> list[Object] get_policies(o, page=page, limit=limit)

List All Policy Objects

Retrieves a list of all policy objects for the authenticated user.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.PoliciesApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Organization ID for retrieving policies
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 0)
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 500)

try:
    # List All Policy Objects
    api_response = api_instance.get_policies(o, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID for retrieving policies | 
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 0]
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with &#x60;page&#x60; parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 500]

### Return type

[**list[Object]**](Object.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> InlineResponse2001 get_policy(id, o)

List Specific Policy Object

Returns a specific policy object for the authenticated user.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.PoliciesApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Policy ID for the specified policy
o = 56 # int | Organization ID for the specified policy

try:
    # List Specific Policy Object
    api_response = api_instance.get_policy(id, o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Policy ID for the specified policy | 
 **o** | **int**| Organization ID for the specified policy | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_stats**
> list[PolicyStats] get_policy_stats(o)

List Policy Compliance Stats

Retrieve policy compliance statistics for all policies.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.PoliciesApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Organization ID for retrieving policy stats. Omit this to retrieve stats for policies in all organizations that the authenticated user can access

try:
    # List Policy Compliance Stats
    api_response = api_instance.get_policy_stats(o)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policy_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID for retrieving policy stats. Omit this to retrieve stats for policies in all organizations that the authenticated user can access | 

### Return type

[**list[PolicyStats]**](PolicyStats.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> update_policy(body, o, id)

Updates a specific policy object for the authenticated user.

Updates a specific policy object for the authenticated user. For more info on filter types and scheduling, see [Policy and Device Filters, and Scheduling](/developer-portal/policy_filters_schedule).

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.PoliciesApi(automox_console_sdk.ApiClient(configuration))
body = automox_console_sdk.Object() # Object | 
o = 56 # int | Organization ID for the specified policy
id = 56 # int | Policy ID for the specified policy

try:
    # Updates a specific policy object for the authenticated user.
    api_instance.update_policy(body, o, id)
except ApiException as e:
    print("Exception when calling PoliciesApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **o** | **int**| Organization ID for the specified policy | 
 **id** | **int**| Policy ID for the specified policy | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

