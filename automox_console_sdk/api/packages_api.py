# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-11-16
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from automox_console_sdk.api_client import ApiClient


class PackagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_device_packages(self, id, o, **kwargs):  # noqa: E501
        """List Software Packages for Specific Device  # noqa: E501

        Returns the software packages for the specified device. Packages Include: Pending updates and currently installed updates/applications  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_packages(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server ID for the specified device. (required)
        :param int o: Organization ID for the specified device (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :param int limit: A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :return: list[Packages]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_device_packages_with_http_info(id, o, **kwargs)  # noqa: E501
        else:
            (data) = self.get_device_packages_with_http_info(id, o, **kwargs)  # noqa: E501
            return data

    def get_device_packages_with_http_info(self, id, o, **kwargs):  # noqa: E501
        """List Software Packages for Specific Device  # noqa: E501

        Returns the software packages for the specified device. Packages Include: Pending updates and currently installed updates/applications  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_packages_with_http_info(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server ID for the specified device. (required)
        :param int o: Organization ID for the specified device (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :param int limit: A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :return: list[Packages]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'o', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_packages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_device_packages`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `get_device_packages`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501
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
            '/servers/{id}/packages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Packages]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_organization_packages(self, id, o, **kwargs):  # noqa: E501
        """List All Software Packages for All Devices  # noqa: E501

        This will list all pending/installed updates, and all installed applications, for all devices in a given organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_organization_packages(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Organization ID for retrieving package list. (required)
        :param int o: Organization ID of the target organization. (required)
        :param int include_unmanaged: Include applications Automox does not currently support for patching.
        :param int awaiting: Filter based installation status of package. `awaiting=1`:  Packages that are currently available but not installed. `awaiting=0`:  Packages that are already installed.
        :param int page: The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :param int limit: A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :return: list[Packages]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_organization_packages_with_http_info(id, o, **kwargs)  # noqa: E501
        else:
            (data) = self.get_organization_packages_with_http_info(id, o, **kwargs)  # noqa: E501
            return data

    def get_organization_packages_with_http_info(self, id, o, **kwargs):  # noqa: E501
        """List All Software Packages for All Devices  # noqa: E501

        This will list all pending/installed updates, and all installed applications, for all devices in a given organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_organization_packages_with_http_info(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Organization ID for retrieving package list. (required)
        :param int o: Organization ID of the target organization. (required)
        :param int include_unmanaged: Include applications Automox does not currently support for patching.
        :param int awaiting: Filter based installation status of package. `awaiting=1`:  Packages that are currently available but not installed. `awaiting=0`:  Packages that are already installed.
        :param int page: The page of results you wish to be returned with page numbers starting at 0. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :param int limit: A limit on the number of results to be returned, between 1 and 500, with a default of 500. Use with `page` parameter. See [About Automox API - Pagination](/developer-portal/about-ax-api/#pagination)
        :return: list[Packages]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'o', 'include_unmanaged', 'awaiting', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_organization_packages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_organization_packages`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `get_organization_packages`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'include_unmanaged' in params:
            query_params.append(('includeUnmanaged', params['include_unmanaged']))  # noqa: E501
        if 'awaiting' in params:
            query_params.append(('awaiting', params['awaiting']))  # noqa: E501
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501
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
            '/orgs/{id}/packages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Packages]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
