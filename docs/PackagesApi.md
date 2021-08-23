# automox_console_sdk.PackagesApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_packages**](PackagesApi.md#get_device_packages) | **GET** /servers/{id}/packages | List Software Packages for Specific Device
[**get_organization_packages**](PackagesApi.md#get_organization_packages) | **GET** /orgs/{id}/packages | List All Software Packages for All Devices


# **get_device_packages**
> [Packages] get_device_packages(id, o)

List Software Packages for Specific Device

Returns the software packages for the specified device. Packages Include: Pending updates and currently installed updates/applications

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import packages_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.packages import Packages
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
    api_instance = packages_api.PackagesApi(api_client)
    id = 1 # int | Server ID for the specified device
    o = 1 # int | Organization ID for the specified device
    page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) if omitted the server will use the default value of 0
    limit = 500 # int | A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. (optional) if omitted the server will use the default value of 500

    # example passing only required values which don't have defaults set
    try:
        # List Software Packages for Specific Device
        api_response = api_instance.get_device_packages(id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PackagesApi->get_device_packages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Software Packages for Specific Device
        api_response = api_instance.get_device_packages(id, o, page=page, limit=limit)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PackagesApi->get_device_packages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server ID for the specified device |
 **o** | **int**| Organization ID for the specified device |
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. | [optional] if omitted the server will use the default value of 500

### Return type

[**[Packages]**](Packages.md)

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

# **get_organization_packages**
> [Packages] get_organization_packages(id, o)

List All Software Packages for All Devices

Returns a list of all software packages discovered on all devices of an organization.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import packages_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.packages import Packages
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
    api_instance = packages_api.PackagesApi(api_client)
    id = 1 # int | Organization ID for retrieving package list
    o = 1 # int | Organization ID. Required. If authenticated, the user has access to multiple organizations.
    include_unmanaged = 0 # int | Include applications Automox does not currently support for patching (optional)
    awaiting = 0 # int | Filter based installation status of package. awaiting=1:  Packages that are currently available but not installed. awaiting=0:  Packages that are already installed. (optional)
    page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. (optional) if omitted the server will use the default value of 0
    limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. (optional) if omitted the server will use the default value of 500

    # example passing only required values which don't have defaults set
    try:
        # List All Software Packages for All Devices
        api_response = api_instance.get_organization_packages(id, o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PackagesApi->get_organization_packages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List All Software Packages for All Devices
        api_response = api_instance.get_organization_packages(id, o, include_unmanaged=include_unmanaged, awaiting=awaiting, page=page, limit=limit)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling PackagesApi->get_organization_packages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Organization ID for retrieving package list |
 **o** | **int**| Organization ID. Required. If authenticated, the user has access to multiple organizations. |
 **include_unmanaged** | **int**| Include applications Automox does not currently support for patching | [optional]
 **awaiting** | **int**| Filter based installation status of package. awaiting&#x3D;1:  Packages that are currently available but not installed. awaiting&#x3D;0:  Packages that are already installed. | [optional]
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. | [optional] if omitted the server will use the default value of 500

### Return type

[**[Packages]**](Packages.md)

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

