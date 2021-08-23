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
from automox_console_sdk.model.inline_response403 import InlineResponse403
from automox_console_sdk.model.packages import Packages


class PackagesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_device_packages(
            self,
            id,
            o,
            **kwargs
        ):
            """List Software Packages for Specific Device  # noqa: E501

            Returns the software packages for the specified device. Packages Include: Pending updates and currently installed updates/applications  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_device_packages(id, o, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Server ID for the specified device
                o (int): Organization ID for the specified device

            Keyword Args:
                page (int): The page of results you wish to be returned with page numbers starting at 0.. [optional] if omitted the server will use the default value of 0
                limit (int): A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter.. [optional] if omitted the server will use the default value of 500
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
                [Packages]
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
            kwargs['id'] = \
                id
            kwargs['o'] = \
                o
            return self.call_with_http_info(**kwargs)

        self.get_device_packages = _Endpoint(
            settings={
                'response_type': ([Packages],),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/servers/{id}/packages',
                'operation_id': 'get_device_packages',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'o',
                    'page',
                    'limit',
                ],
                'required': [
                    'id',
                    'o',
                ],
                'nullable': [
                ],
                'enum': [
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
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'o':
                        (int,),
                    'page':
                        (int,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'o': 'o',
                    'page': 'page',
                    'limit': 'limit',
                },
                'location_map': {
                    'id': 'path',
                    'o': 'query',
                    'page': 'query',
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
            callable=__get_device_packages
        )

        def __get_organization_packages(
            self,
            id,
            o,
            **kwargs
        ):
            """List All Software Packages for All Devices  # noqa: E501

            Returns a list of all software packages discovered on all devices of an organization.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_organization_packages(id, o, async_req=True)
            >>> result = thread.get()

            Args:
                id (int): Organization ID for retrieving package list
                o (int): Organization ID. Required. If authenticated, the user has access to multiple organizations.

            Keyword Args:
                include_unmanaged (int): Include applications Automox does not currently support for patching. [optional]
                awaiting (int): Filter based installation status of package. awaiting=1:  Packages that are currently available but not installed. awaiting=0:  Packages that are already installed.. [optional]
                page (int): The page of results you wish to be returned with page numbers starting at 0.. [optional] if omitted the server will use the default value of 0
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
                [Packages]
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
            kwargs['id'] = \
                id
            kwargs['o'] = \
                o
            return self.call_with_http_info(**kwargs)

        self.get_organization_packages = _Endpoint(
            settings={
                'response_type': ([Packages],),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/orgs/{id}/packages',
                'operation_id': 'get_organization_packages',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'o',
                    'include_unmanaged',
                    'awaiting',
                    'page',
                    'limit',
                ],
                'required': [
                    'id',
                    'o',
                ],
                'nullable': [
                ],
                'enum': [
                    'include_unmanaged',
                    'awaiting',
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
                    ('include_unmanaged',): {

                        "0": 0,
                        "1": 1
                    },
                    ('awaiting',): {

                        "0": 0,
                        "1": 1
                    },
                },
                'openapi_types': {
                    'id':
                        (int,),
                    'o':
                        (int,),
                    'include_unmanaged':
                        (int,),
                    'awaiting':
                        (int,),
                    'page':
                        (int,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'o': 'o',
                    'include_unmanaged': 'includeUnmanaged',
                    'awaiting': 'awaiting',
                    'page': 'page',
                    'limit': 'limit',
                },
                'location_map': {
                    'id': 'path',
                    'o': 'query',
                    'include_unmanaged': 'query',
                    'awaiting': 'query',
                    'page': 'query',
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
            callable=__get_organization_packages
        )
