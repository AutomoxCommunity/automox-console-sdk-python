# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-08-10
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from automox_console_sdk.api_client import ApiClient


class WorkletsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_community_worklet(self, id, **kwargs):  # noqa: E501
        """Retrieve Community Worklet by ID  # noqa: E501

        Retrieves details for a specific Community Worklet by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_community_worklet(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the Community Worklet to retrieve (required)
        :return: WorkletDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_community_worklet_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_community_worklet_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_community_worklet_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve Community Worklet by ID  # noqa: E501

        Retrieves details for a specific Community Worklet by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_community_worklet_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the Community Worklet to retrieve (required)
        :return: WorkletDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_community_worklet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_community_worklet`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/community-worklets/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkletDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_community_worklets(self, **kwargs):  # noqa: E501
        """Retrieve Community Worklets  # noqa: E501

        Retrieves a list of Community Worklets  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_community_worklets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of results you wish to be returned with page numbers starting at 0.
        :param int limit: A limit on the number of results to be returned, between 1 and 500 with a default of 25. Use with page parameter.
        :return: Worklet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_community_worklets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_community_worklets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_community_worklets_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve Community Worklets  # noqa: E501

        Retrieves a list of Community Worklets  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_community_worklets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of results you wish to be returned with page numbers starting at 0.
        :param int limit: A limit on the number of results to be returned, between 1 and 500 with a default of 25. Use with page parameter.
        :return: Worklet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_community_worklets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/community-worklets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Worklet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
