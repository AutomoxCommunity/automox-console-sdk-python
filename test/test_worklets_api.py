"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    The version of the OpenAPI document: 2021-08-10
    Contact: support@automox.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.worklets_api import WorkletsApi  # noqa: E501


class TestWorkletsApi(unittest.TestCase):
    """WorkletsApi unit test stubs"""

    def setUp(self):
        self.api = WorkletsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_community_worklet(self):
        """Test case for get_community_worklet

        Retrieve Community Worklet by ID  # noqa: E501
        """
        pass

    def test_get_community_worklets(self):
        """Test case for get_community_worklets

        Retrieve Community Worklets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
