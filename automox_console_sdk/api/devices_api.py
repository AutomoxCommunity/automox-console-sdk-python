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


class DevicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_device(self, id, o, **kwargs):  # noqa: E501
        """Deletes a device (server object).  # noqa: E501

        Deletes a device (server object). The associated command queue will be purged. Any pending custom commands for the device are removed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_device(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server ID for the specified device (required)
        :param int o: Organization ID for the specified device (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_device_with_http_info(id, o, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_device_with_http_info(id, o, **kwargs)  # noqa: E501
            return data

    def delete_device_with_http_info(self, id, o, **kwargs):  # noqa: E501
        """Deletes a device (server object).  # noqa: E501

        Deletes a device (server object). The associated command queue will be purged. Any pending custom commands for the device are removed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_device_with_http_info(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server ID for the specified device (required)
        :param int o: Organization ID for the specified device (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'o']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_device`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `delete_device`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
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
            '/servers/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_device_packages(self, id, o, **kwargs):  # noqa: E501
        """List Software Packages for Specific Device  # noqa: E501

        Returns the software packages for the specified device. Packages Include: Pending updates and currently installed updates/applications  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_packages(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server ID for the specified device (required)
        :param int o: Organization ID for the specified device (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0.
        :param int limit: A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter.
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
        :param int id: Server ID for the specified device (required)
        :param int o: Organization ID for the specified device (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0.
        :param int limit: A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter.
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

    def get_device_queues(self, id, o, **kwargs):  # noqa: E501
        """Upcoming Commands Queue for Specific Device  # noqa: E501

        Returns the queue of upcoming commands for the specified device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_queues(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server ID for the specified device (required)
        :param int o: Organization ID for the specified device (required)
        :return: list[Command]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_device_queues_with_http_info(id, o, **kwargs)  # noqa: E501
        else:
            (data) = self.get_device_queues_with_http_info(id, o, **kwargs)  # noqa: E501
            return data

    def get_device_queues_with_http_info(self, id, o, **kwargs):  # noqa: E501
        """Upcoming Commands Queue for Specific Device  # noqa: E501

        Returns the queue of upcoming commands for the specified device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_queues_with_http_info(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server ID for the specified device (required)
        :param int o: Organization ID for the specified device (required)
        :return: list[Command]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'o']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_queues" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_device_queues`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `get_device_queues`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
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
            '/servers/{id}/queues', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Command]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_devices(self, o, limit, page, **kwargs):  # noqa: E501
        """List All Devices  # noqa: E501

        This retrieves a detailed list of all devices (server objects) for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_devices(o, limit, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID. Response will include devices for the specified Automox Organization (required)
        :param int limit: A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0. (required)
        :param int group_id: Filter based on membership to a specific Server Group ID
        :param int ps_version: Shows version of PowerShell running on the device, if applicable.
        :param int pending: Filter based on status of pending patches. Format: pending=1
        :param str patch_status: Filter based on presence of ANY available patches that aren't already installed. Value must be 'missing' Format: patchStatus=missing
        :param int policy_id: Filter based on association to a given Policy ID
        :param int exception: Filter based on device's Exception status
        :param int managed: Filter based on device's Managed status. Unmanaged indicates no linked policies.
        :return: ServerList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_devices_with_http_info(o, limit, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_devices_with_http_info(o, limit, page, **kwargs)  # noqa: E501
            return data

    def get_devices_with_http_info(self, o, limit, page, **kwargs):  # noqa: E501
        """List All Devices  # noqa: E501

        This retrieves a detailed list of all devices (server objects) for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_devices_with_http_info(o, limit, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID. Response will include devices for the specified Automox Organization (required)
        :param int limit: A limit on the number of results to be returned, between 1 and 500 with a default of 500. Use with page parameter. (required)
        :param int page: The page of results you wish to be returned with page numbers starting at 0. (required)
        :param int group_id: Filter based on membership to a specific Server Group ID
        :param int ps_version: Shows version of PowerShell running on the device, if applicable.
        :param int pending: Filter based on status of pending patches. Format: pending=1
        :param str patch_status: Filter based on presence of ANY available patches that aren't already installed. Value must be 'missing' Format: patchStatus=missing
        :param int policy_id: Filter based on association to a given Policy ID
        :param int exception: Filter based on device's Exception status
        :param int managed: Filter based on device's Managed status. Unmanaged indicates no linked policies.
        :return: ServerList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['o', 'limit', 'page', 'group_id', 'ps_version', 'pending', 'patch_status', 'policy_id', 'exception', 'managed']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_devices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `get_devices`")  # noqa: E501
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_devices`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_devices`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in params:
            query_params.append(('groupId', params['group_id']))  # noqa: E501
        if 'ps_version' in params:
            query_params.append(('PS_VERSION', params['ps_version']))  # noqa: E501
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501
        if 'pending' in params:
            query_params.append(('pending', params['pending']))  # noqa: E501
        if 'patch_status' in params:
            query_params.append(('patchStatus', params['patch_status']))  # noqa: E501
        if 'policy_id' in params:
            query_params.append(('policyId', params['policy_id']))  # noqa: E501
        if 'exception' in params:
            query_params.append(('exception', params['exception']))  # noqa: E501
        if 'managed' in params:
            query_params.append(('managed', params['managed']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/servers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServerList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_server(self, id, o, **kwargs):  # noqa: E501
        """List a Specific Device  # noqa: E501

        Returns a specific device (server object) for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_server(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server ID for the specified device (required)
        :param int o: Organization ID for the specified device (required)
        :return: ServerWithPolicies
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_server_with_http_info(id, o, **kwargs)  # noqa: E501
        else:
            (data) = self.get_server_with_http_info(id, o, **kwargs)  # noqa: E501
            return data

    def get_server_with_http_info(self, id, o, **kwargs):  # noqa: E501
        """List a Specific Device  # noqa: E501

        Returns a specific device (server object) for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_server_with_http_info(id, o, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Server ID for the specified device (required)
        :param int o: Organization ID for the specified device (required)
        :return: ServerWithPolicies
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'o']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_server" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_server`")  # noqa: E501
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `get_server`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
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
            '/servers/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServerWithPolicies',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def issue_device_command(self, o, id, **kwargs):  # noqa: E501
        """Issue a command to a device  # noqa: E501

        Force a device to Scan, Patch, or Reboot for immediate execution. **Note: The `installAllUpdates` option ignores any Policy Filters**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.issue_device_command(o, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID for the specified device (required)
        :param int id: Server ID for the specified device (required)
        :param IdQueuesBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.issue_device_command_with_http_info(o, id, **kwargs)  # noqa: E501
        else:
            (data) = self.issue_device_command_with_http_info(o, id, **kwargs)  # noqa: E501
            return data

    def issue_device_command_with_http_info(self, o, id, **kwargs):  # noqa: E501
        """Issue a command to a device  # noqa: E501

        Force a device to Scan, Patch, or Reboot for immediate execution. **Note: The `installAllUpdates` option ignores any Policy Filters**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.issue_device_command_with_http_info(o, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int o: Organization ID for the specified device (required)
        :param int id: Server ID for the specified device (required)
        :param IdQueuesBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['o', 'id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method issue_device_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o' is set
        if ('o' not in params or
                params['o'] is None):
            raise ValueError("Missing the required parameter `o` when calling `issue_device_command`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `issue_device_command`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/servers/{id}/queues', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_device(self, body, id, **kwargs):  # noqa: E501
        """Updates a device (server object).  # noqa: E501

        Updates a device (server object).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_device(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ServersIdBody body: Device update (required)
        :param int id: Server ID for the specified device (required)
        :param int o: Organization ID for the specified device
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_device_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_device_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def update_device_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Updates a device (server object).  # noqa: E501

        Updates a device (server object).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_device_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ServersIdBody body: Device update (required)
        :param int id: Server ID for the specified device (required)
        :param int o: Organization ID for the specified device
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'o']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_device`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_device`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'o' in params:
            query_params.append(('o', params['o']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/servers/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
