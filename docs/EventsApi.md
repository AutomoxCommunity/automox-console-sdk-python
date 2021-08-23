# automox_console_sdk.EventsApi

All URIs are relative to *https://console.automox.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events**](EventsApi.md#get_events) | **GET** /events | Retrieve All Event Objects for the Authenticated User


# **get_events**
> [Event] get_events(o)

Retrieve All Event Objects for the Authenticated User

Events Include: Policy Actions, Device Addition/Removal, User Addition/Removal

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import automox_console_sdk
from automox_console_sdk.api import events_api
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.event import Event
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
    api_instance = events_api.EventsApi(api_client)
    o = 1 # int | Limit response to a specific Automox organization
    page = 1 # int | The page of results you wish to be returned with page numbers starting at 0. (optional)
    count_only = 0 # int | Retrieve only the total count of events for the organization (optional)
    policy_id = 1 # int | Retrieve events for a specific policy (optional)
    server_id = 1 # int | Retrieve events for a specific device (optional)
    user_id = 1 # int | Retrieve events for a specific user (optional)
    event_name = "org.exceeded_endpoint_limit" # str | Name for the event type (optional)
    start_date = dateutil_parser('1970-01-01').date() # date | Limit responses to include only events after this date (YYYY-MM-DD) (optional)
    end_date = dateutil_parser('1970-01-01').date() # date | Limit responses to include only events before this date (YYYY-MM-DD) (optional)
    limit = 500 # int | A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. (optional) if omitted the server will use the default value of 500

    # example passing only required values which don't have defaults set
    try:
        # Retrieve All Event Objects for the Authenticated User
        api_response = api_instance.get_events(o)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
        print("Exception when calling EventsApi->get_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve All Event Objects for the Authenticated User
        api_response = api_instance.get_events(o, page=page, count_only=count_only, policy_id=policy_id, server_id=server_id, user_id=user_id, event_name=event_name, start_date=start_date, end_date=end_date, limit=limit)
        pprint(api_response)
    except automox_console_sdk.ApiException as e:
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
 **limit** | **int**| A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. | [optional] if omitted the server will use the default value of 500

### Return type

[**[Event]**](Event.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | You do not have permission to perform this action. |  -  |
**404** | Entity not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

