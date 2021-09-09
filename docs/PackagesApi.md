# automox_console_sdk.PackagesApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_packages**](PackagesApi.md#get_device_packages) | **GET** /servers/{id}/packages | List Software Packages for Specific Device
[**get_organization_packages**](PackagesApi.md#get_organization_packages) | **GET** /orgs/{id}/packages | List All Software Packages for All Devices

# **get_device_packages**
> list[Packages] get_device_packages(id, o, page=page, limit=limit)

List Software Packages for Specific Device

Returns the software packages for the specified device. Packages Include: Pending updates and currently installed updates/applications

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.PackagesApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Server ID for the specified device.
o = 56 # int | Organization ID for the specified device
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 0)
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 500)

try:
    # List Software Packages for Specific Device
    api_response = api_instance.get_device_packages(id, o, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_device_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Server ID for the specified device. | 
 **o** | **int**| Organization ID for the specified device | 
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 0]
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with &#x60;page&#x60; parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 500]

### Return type

[**list[Packages]**](Packages.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_packages**
> list[Packages] get_organization_packages(id, o, include_unmanaged=include_unmanaged, awaiting=awaiting, page=page, limit=limit)

List All Software Packages for All Devices

This will list all pending/installed updates, and all installed applications, for all devices in a given organization.

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.PackagesApi(automox_console_sdk.ApiClient(configuration))
id = 56 # int | Organization ID for retrieving package list.
o = 56 # int | Organization ID of the target organization.
include_unmanaged = 789 # int | Include applications Automox does not currently support for patching. (optional)
awaiting = 789 # int | Filter based installation status of package. `awaiting=1`:  Packages that are currently available but not installed. `awaiting=0`:  Packages that are already installed. (optional)
page = 0 # int | The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 0)
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) (optional) (default to 500)

try:
    # List All Software Packages for All Devices
    api_response = api_instance.get_organization_packages(id, o, include_unmanaged=include_unmanaged, awaiting=awaiting, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesApi->get_organization_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Organization ID for retrieving package list. | 
 **o** | **int**| Organization ID of the target organization. | 
 **include_unmanaged** | **int**| Include applications Automox does not currently support for patching. | [optional] 
 **awaiting** | **int**| Filter based installation status of package. &#x60;awaiting&#x3D;1&#x60;:  Packages that are currently available but not installed. &#x60;awaiting&#x3D;0&#x60;:  Packages that are already installed. | [optional] 
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 0]
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with &#x60;page&#x60; parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination) | [optional] [default to 500]

### Return type

[**list[Packages]**](Packages.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

