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
> [Policy] create_policy(o)

Create a New Policy

Creates a new policy for a specified organization. For more info on filter types and scheduling, see [Policies - Scheduling and Filtering](/developer-portal/policy_filters_schedule)

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import policies_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.policy import Policy
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
    api_instance = policies_api.PoliciesApi(api_client)
    o = 1 # int | Organization ID for retrieving policies
    unknown_base_type = {
        name="name_example",
        policy_type_name="policy_type_name_example",
        organization_id=1,
        schedule_days=1,
        schedule_weeks_of_month=1,
        schedule_months=1,
        schedule_time="schedule_time_example",
        configuration=PolicyConfiguration(),
        notify_user=True,
        notes="notes_example",
        server_groups=[
            1,
        ],
        auto_patch=True,
        auto_reboot=True,
        notify_reboot_user=True,
    } # UNKNOWN_BASE_TYPE |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a New Policy
        api_response = api_instance.create_policy(o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PoliciesApi->create_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a New Policy
        api_response = api_instance.create_policy(o, unknown_base_type=unknown_base_type)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PoliciesApi->create_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID for retrieving policies |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional]

### Return type

[**[Policy]**](Policy.md)

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

# **delete_policy**
> delete_policy(id, o)

Delete Specific Policy Object

Deletes a specific policy object for the authenticated user.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import policies_api
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
    api_instance = policies_api.PoliciesApi(api_client)
    id = 1 # int | Policy ID for the specified policy
    o = 1 # int | Organization ID for the specified policy

    # example passing only required values which don't have defaults set
    try:
        # Delete Specific Policy Object
        api_instance.delete_policy(id, o)
    except automox_console_sdk.ApiException as e:
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |
**404** | Entity not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_policy**
> execute_policy(id, o, action)

Schedule a Policy for Immediate Remediation

Schedule a policy for immediate remediation.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import policies_api
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
    api_instance = policies_api.PoliciesApi(api_client)
    id = 1 # int | Policy ID for the specified policy
    o = 1 # int | Organization ID for the specified policy
    action = "remediateAll" # str | Specify the action to be taken. Possible values: remediateAll, remediateServer Format: action=remediateServer
    server_id = 1 # int | Specify the specific Server to run the policy for. Only applicable when action is set to \"remediateServer\" Format: serverId=123456 (optional)

    # example passing only required values which don't have defaults set
    try:
        # Schedule a Policy for Immediate Remediation
        api_instance.execute_policy(id, o, action)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PoliciesApi->execute_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Schedule a Policy for Immediate Remediation
        api_instance.execute_policy(id, o, action, server_id=server_id)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PoliciesApi->execute_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Policy ID for the specified policy |
 **o** | **int**| Organization ID for the specified policy |
 **action** | **str**| Specify the action to be taken. Possible values: remediateAll, remediateServer Format: action&#x3D;remediateServer |
 **server_id** | **int**| Specify the specific Server to run the policy for. Only applicable when action is set to \&quot;remediateServer\&quot; Format: serverId&#x3D;123456 | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Action Started Successfully |  -  |
**400** | Invalid Request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |
**404** | Entity not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_policy_device_filter_preview**
> [PolicyDeviceFiltersOutput] generate_policy_device_filter_preview(policy_device_filters_preview)

Policy Device Filters Preview

Generate a preview of the list of devices that matches the provided device filter set. For more information, see [Device Filter Preview - Filter Parameters](/developer-portal/device-filters).

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import policies_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.policy_device_filters_output import PolicyDeviceFiltersOutput
from automox_console_sdk.model.policy_device_filters_preview import PolicyDeviceFiltersPreview
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
    api_instance = policies_api.PoliciesApi(api_client)
    policy_device_filters_preview = PolicyDeviceFiltersPreview(
        device_filters=[
            PolicyDeviceFiltersPreviewDeviceFilters(
                field="tag",
                op="in",
                value=[
                    ,
                ],
            ),
        ],
        server_groups=[
            1,
        ],
    ) # PolicyDeviceFiltersPreview | 
    o = 1 # int | Organization ID. If omitted, results will include all organizations for the authenticated user. (optional)
    page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) if omitted the server will use the default value of 0
    limit = 25 # int | A limit on the number of results to be returned, between 1 and 200 with a default of 25. Use with page parameter. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Policy Device Filters Preview
        api_response = api_instance.generate_policy_device_filter_preview(policy_device_filters_preview)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PoliciesApi->generate_policy_device_filter_preview: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Policy Device Filters Preview
        api_response = api_instance.generate_policy_device_filter_preview(policy_device_filters_preview, o=o, page=page, limit=limit)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PoliciesApi->generate_policy_device_filter_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_device_filters_preview** | [**PolicyDeviceFiltersPreview**](PolicyDeviceFiltersPreview.md)|  |
 **o** | **int**| Organization ID. If omitted, results will include all organizations for the authenticated user. | [optional]
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 200 with a default of 25. Use with page parameter. | [optional] if omitted the server will use the default value of 25

### Return type

[**[PolicyDeviceFiltersOutput]**](PolicyDeviceFiltersOutput.md)

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

# **get_policies**
> [Policy] get_policies(o)

List All Policy Objects

Retrieves a list of all policy objects for the authenticated user.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import policies_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.policy import Policy
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
    api_instance = policies_api.PoliciesApi(api_client)
    o = 1 # int | Organization ID for retrieving policies
    page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) if omitted the server will use the default value of 0
    limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. (optional) if omitted the server will use the default value of 500

    # example passing only required values which don't have defaults set
    try:
        # List All Policy Objects
        api_response = api_instance.get_policies(o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PoliciesApi->get_policies: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Policy Objects
        api_response = api_instance.get_policies(o, page=page, limit=limit)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PoliciesApi->get_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID for retrieving policies |
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. | [optional] if omitted the server will use the default value of 500

### Return type

[**[Policy]**](Policy.md)

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

# **get_policy**
> Policy get_policy(id, o)

List Specific Policy Object

Returns a specific policy object for the authenticated user.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import policies_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.policy import Policy
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
    api_instance = policies_api.PoliciesApi(api_client)
    id = 1 # int | Policy ID for the specified policy
    o = 1 # int | Organization ID for the specified policy

    # example passing only required values which don't have defaults set
    try:
        # List Specific Policy Object
        api_response = api_instance.get_policy(id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PoliciesApi->get_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Policy ID for the specified policy |
 **o** | **int**| Organization ID for the specified policy |

### Return type

[**Policy**](Policy.md)

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

# **get_policy_stats**
> [PolicyStats] get_policy_stats()

List Policy Compliance Stats

Retrieve policy compliance statistics for all policies.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import policies_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.policy_stats import PolicyStats
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
    api_instance = policies_api.PoliciesApi(api_client)
    o = 1 # int | Organization ID for retrieving policy stats. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Policy Compliance Stats
        api_response = api_instance.get_policy_stats(o=o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PoliciesApi->get_policy_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Organization ID for retrieving policy stats. | [optional]

### Return type

[**[PolicyStats]**](PolicyStats.md)

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

# **update_policy**
> update_policy(id, o, policy)

Updates a specific policy object for the authenticated user.

Updates a specific policy object for the authenticated user.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import policies_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.policy import Policy
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
    api_instance = policies_api.PoliciesApi(api_client)
    id = 1 # int | Policy ID for the specified policy
    o = 1 # int | Organization ID for the specified policy
    policy = Policy(
        configuration=PolicyConfiguration(),
        id=1,
        name="name_example",
        notes="notes_example",
        organization_id=1,
        policy_type_name="policy_type_name_example",
        schedule_days=1,
        schedule_weeks_of_month=1,
        schedule_months=1,
        schedule_time="schedule_time_example",
        next_remediation=dateutil_parser('1970-01-01T00:00:00.00Z'),
        server_groups=[
            1,
        ],
    ) # Policy | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a specific policy object for the authenticated user.
        api_instance.update_policy(id, o, policy)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PoliciesApi->update_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Policy ID for the specified policy |
 **o** | **int**| Organization ID for the specified policy |
 **policy** | [**Policy**](Policy.md)|  |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Update Successful |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

