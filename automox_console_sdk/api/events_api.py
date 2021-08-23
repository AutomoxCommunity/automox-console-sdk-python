"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    The version of the OpenAPI document: 2021-08-10
    Contact: support@automox.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from automox_console_sdk.api_client import ApiClient, Endpoint as _Endpoint
from automox_console_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from automox_console_sdk.model.event import Event
from automox_console_sdk.model.inline_response403 import InlineResponse403


class EventsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_events(
            self,
            o,
            **kwargs
        ):
            """Retrieve All Event Objects for the Authenticated User  # noqa: E501

            Events Include: Policy Actions, Device Addition/Removal, User Addition/Removal  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_events(o, async_req=True)
            >>> result = thread.get()

            Args:
                o (int): Limit response to a specific Automox organization

            Keyword Args:
                page (int): The page of results you wish to be returned with page numbers starting at 0.. [optional]
                count_only (int): Retrieve only the total count of events for the organization. [optional]
                policy_id (int): Retrieve events for a specific policy. [optional]
                server_id (int): Retrieve events for a specific device. [optional]
                user_id (int): Retrieve events for a specific user. [optional]
                event_name (str): Name for the event type. [optional]
                start_date (date): Limit responses to include only events after this date (YYYY-MM-DD). [optional]
                end_date (date): Limit responses to include only events before this date (YYYY-MM-DD). [optional]
                limit (int): A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with page parameter.. [optional] if omitted the server will use the default value of 500
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [Event]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['o'] = \
                o
            return self.call_with_http_info(**kwargs)

        self.get_events = _Endpoint(
            settings={
                'response_type': ([Event],),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/events',
                'operation_id': 'get_events',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'o',
                    'page',
                    'count_only',
                    'policy_id',
                    'server_id',
                    'user_id',
                    'event_name',
                    'start_date',
                    'end_date',
                    'limit',
                ],
                'required': [
                    'o',
                ],
                'nullable': [
                ],
                'enum': [
                    'count_only',
                    'event_name',
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 500,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('count_only',): {

                        "0": 0,
                        "1": 1
                    },
                    ('event_name',): {

                        "ORG.EXCEEDED_ENDPOINT_LIMIT": "org.exceeded_endpoint_limit",
                        "SAML.USER.CREATE": "saml.user.create",
                        "SLACK.APP.ADDED": "slack.app.added",
                        "SLACK.APP.REINSTALLED": "slack.app.reinstalled",
                        "SYSTEM.ADD": "system.add",
                        "SYSTEM.DELETE": "system.delete",
                        "SYSTEM.GROUP.ACTION": "system.group.action",
                        "SYSTEM.NOTIFICATION.RESPONSE": "system.notification.response",
                        "SYSTEM.NOTIFICATION.SENT": "system.notification.sent",
                        "SYSTEM.PATCH.APPLIED": "system.patch.applied",
                        "SYSTEM.PATCH.FAILED": "system.patch.failed",
                        "SYSTEM.PATCH.UNINSTALL": "system.patch.uninstall",
                        "SYSTEM.POLICY.ACTION": "system.policy.action",
                        "USER.CREATE": "user.create",
                        "USER.LOGIN": "user.login",
                        "USER.LOGOUT": "user.logout",
                        "USER.REMOVED": "user.removed"
                    },
                },
                'openapi_types': {
                    'o':
                        (int,),
                    'page':
                        (int,),
                    'count_only':
                        (int,),
                    'policy_id':
                        (int,),
                    'server_id':
                        (int,),
                    'user_id':
                        (int,),
                    'event_name':
                        (str,),
                    'start_date':
                        (date,),
                    'end_date':
                        (date,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'o': 'o',
                    'page': 'page',
                    'count_only': 'countOnly',
                    'policy_id': 'policyId',
                    'server_id': 'serverId',
                    'user_id': 'userId',
                    'event_name': 'eventName',
                    'start_date': 'startDate',
                    'end_date': 'endDate',
                    'limit': 'limit',
                },
                'location_map': {
                    'o': 'query',
                    'page': 'query',
                    'count_only': 'query',
                    'policy_id': 'query',
                    'server_id': 'query',
                    'user_id': 'query',
                    'event_name': 'query',
                    'start_date': 'query',
                    'end_date': 'query',
                    'limit': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_events
        )
