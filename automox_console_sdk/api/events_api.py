# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-09-20
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from automox_console_sdk.api_client import ApiClient


class EventsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_events(self, o, **kwargs):  # noqa: E501
        """Retrieve All Event Objects for the Authenticated User  # noqa: E501

        Events Include: Policy Actions, Device Addition/Removal, User Addition/Removal  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events(o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID. Response will include devices for the specified Automox organization. The organization will be assumed based on the API key, if not specified. (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :param int count_only: Use instead of `page` or `limit` to retrieve only the total count of events for the organization, or when used with an `eventName`, retrieve a count of that specific type of event.
        :param int policy_id: Retrieve events for a specific policy.
        :param int server_id: Retrieve events for a specific device.
        :param int user_id: Retrieve events for a specific user.
        :param str event_name: Name for the event type.
        :param date start_date: Limit responses to include only events after this date. Format: (YYYY-MM-DD).
        :param date end_date: Limit responses to include only events before this date. Format: (YYYY-MM-DD).
        :param int limit: A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :return: list[Event]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_events_with_http_info(o, **kwargs)  # noqa: E501
        else:
            (data) = self.get_events_with_http_info(o, **kwargs)  # noqa: E501
            return data

    def get_events_with_http_info(self, o, **kwargs):  # noqa: E501
        """Retrieve All Event Objects for the Authenticated User  # noqa: E501

        Events Include: Policy Actions, Device Addition/Removal, User Addition/Removal  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events_with_http_info(o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID. Response will include devices for the specified Automox organization. The organization will be assumed based on the API key, if not specified. (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :param int count_only: Use instead of `page` or `limit` to retrieve only the total count of events for the organization, or when used with an `eventName`, retrieve a count of that specific type of event.
        :param int policy_id: Retrieve events for a specific policy.
        :param int server_id: Retrieve events for a specific device.
        :param int user_id: Retrieve events for a specific user.
        :param str event_name: Name for the event type.
        :param date start_date: Limit responses to include only events after this date. Format: (YYYY-MM-DD).
        :param date end_date: Limit responses to include only events before this date. Format: (YYYY-MM-DD).
        :param int limit: A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :return: list[Event]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['o', 'page', 'count_only', 'policy_id', 'server_id', 'user_id', 'event_name', 'start_date', 'end_date', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `get_events`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'count_only' in params:
            query_params.append(('countOnly', params['count_only']))  # noqa: E501
        if 'policy_id' in params:
            query_params.append(('policyId', params['policy_id']))  # noqa: E501
        if 'server_id' in params:
            query_params.append(('serverId', params['server_id']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('userId', params['user_id']))  # noqa: E501
        if 'event_name' in params:
            query_params.append(('eventName', params['event_name']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Event]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
