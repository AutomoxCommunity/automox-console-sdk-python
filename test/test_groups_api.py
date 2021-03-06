# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-08-10
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import automox_console_sdk
from automox_console_sdk.api.groups_api import GroupsApi  # noqa: E501
from automox_console_sdk.rest import ApiException


class TestGroupsApi(unittest.TestCase):
    """GroupsApi unit test stubs"""

    def setUp(self):
        self.api = GroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_server_group(self):
        """Test case for create_server_group

        Creates a new server group.  # noqa: E501
        """
        pass

    def test_delete_server_group(self):
        """Test case for delete_server_group

        Deletes a server group.  # noqa: E501
        """
        pass

    def test_get_server_group(self):
        """Test case for get_server_group

        List Specific Group Object  # noqa: E501
        """
        pass

    def test_get_server_groups(self):
        """Test case for get_server_groups

        List All Group Objects  # noqa: E501
        """
        pass

    def test_update_server_group(self):
        """Test case for update_server_group

        Updates a new server group.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
