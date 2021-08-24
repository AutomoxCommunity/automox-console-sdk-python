# automox_console_sdk.EventsApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events**](EventsApi.md#get_events) | **GET** /events | Retrieve All Event Objects for the Authenticated User

# **get_events**
> list[Event] get_events(o, page=page, count_only=count_only, policy_id=policy_id, server_id=server_id, user_id=user_id, event_name=event_name, start_date=start_date, end_date=end_date, limit=limit)

Retrieve All Event Objects for the Authenticated User

Events Include: Policy Actions, Device Addition/Removal, User Addition/Removal

### Example
```python
from __future__ import print_function
import time
import automox_console_sdk
from automox_console_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = automox_console_sdk.EventsApi(automox_console_sdk.ApiClient(configuration))
o = 56 # int | Limit response to a specific Automox organization
page = 56 # int | The page of results you wish to be returned with page numbers starting at 0. (optional)
count_only = 56 # int | Retrieve only the total count of events for the organization (optional)
policy_id = 56 # int | Retrieve events for a specific policy (optional)
server_id = 56 # int | Retrieve events for a specific device (optional)
user_id = 56 # int | Retrieve events for a specific user (optional)
event_name = 'event_name_example' # str | Name for the event type (optional)
start_date = '2013-10-20' # date | Limit responses to include only events after this date (YYYY-MM-DD) (optional)
end_date = '2013-10-20' # date | Limit responses to include only events before this date (YYYY-MM-DD) (optional)
limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. (optional) (default to 500)

try:
    # Retrieve All Event Objects for the Authenticated User
    api_response = api_instance.get_events(o, page=page, count_only=count_only, policy_id=policy_id, server_id=server_id, user_id=user_id, event_name=event_name, start_date=start_date, end_date=end_date, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o** | **int**| Limit response to a specific Automox organization | 
 **page** | **int**| The page of results you wish to be returned with page numbers starting at 0. | [optional] 
 **count_only** | **int**| Retrieve only the total count of events for the organization | [optional] 
 **policy_id** | **int**| Retrieve events for a specific policy | [optional] 
 **server_id** | **int**| Retrieve events for a specific device | [optional] 
 **user_id** | **int**| Retrieve events for a specific user | [optional] 
 **event_name** | **str**| Name for the event type | [optional] 
 **start_date** | **date**| Limit responses to include only events after this date (YYYY-MM-DD) | [optional] 
 **end_date** | **date**| Limit responses to include only events before this date (YYYY-MM-DD) | [optional] 
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. | [optional] [default to 500]

### Return type

[**list[Event]**](Event.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

