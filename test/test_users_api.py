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
from automox_console_sdk.api.users_api import UsersApi  # noqa: E501
from automox_console_sdk.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_decrypt_user_api_key(self):
        """Test case for decrypt_user_api_key

        Retrieves the API Key secret by ID  # noqa: E501
        """
        pass

    def test_get_user_by_id(self):
        """Test case for get_user_by_id

        Retrieves a user by user ID  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        List All Users With Access to a Given Organization  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
