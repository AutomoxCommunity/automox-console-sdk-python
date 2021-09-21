# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-09-20
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PolicyDeviceFiltersOutputServerGroup(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'organization_id': 'int',
        'name': 'str',
        'refresh_interval': 'int',
        'parent_server_group_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'organization_id': 'organization_id',
        'name': 'name',
        'refresh_interval': 'refresh_interval',
        'parent_server_group_id': 'parent_server_group_id'
    }

    def __init__(self, id=None, organization_id=None, name=None, refresh_interval=None, parent_server_group_id=None):  # noqa: E501
        """PolicyDeviceFiltersOutputServerGroup - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._organization_id = None
        self._name = None
        self._refresh_interval = None
        self._parent_server_group_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if organization_id is not None:
            self.organization_id = organization_id
        if name is not None:
            self.name = name
        if refresh_interval is not None:
            self.refresh_interval = refresh_interval
        if parent_server_group_id is not None:
            self.parent_server_group_id = parent_server_group_id

    @property
    def id(self):
        """Gets the id of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501


        :return: The id of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyDeviceFiltersOutputServerGroup.


        :param id: The id of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def organization_id(self):
        """Gets the organization_id of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501


        :return: The organization_id of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this PolicyDeviceFiltersOutputServerGroup.


        :param organization_id: The organization_id of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def name(self):
        """Gets the name of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501


        :return: The name of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyDeviceFiltersOutputServerGroup.


        :param name: The name of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def refresh_interval(self):
        """Gets the refresh_interval of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501


        :return: The refresh_interval of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501
        :rtype: int
        """
        return self._refresh_interval

    @refresh_interval.setter
    def refresh_interval(self, refresh_interval):
        """Sets the refresh_interval of this PolicyDeviceFiltersOutputServerGroup.


        :param refresh_interval: The refresh_interval of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501
        :type: int
        """

        self._refresh_interval = refresh_interval

    @property
    def parent_server_group_id(self):
        """Gets the parent_server_group_id of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501


        :return: The parent_server_group_id of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501
        :rtype: int
        """
        return self._parent_server_group_id

    @parent_server_group_id.setter
    def parent_server_group_id(self, parent_server_group_id):
        """Sets the parent_server_group_id of this PolicyDeviceFiltersOutputServerGroup.


        :param parent_server_group_id: The parent_server_group_id of this PolicyDeviceFiltersOutputServerGroup.  # noqa: E501
        :type: int
        """

        self._parent_server_group_id = parent_server_group_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PolicyDeviceFiltersOutputServerGroup, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolicyDeviceFiltersOutputServerGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
