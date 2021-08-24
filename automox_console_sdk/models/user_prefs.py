# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-08-10
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserPrefs(object):
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
        'user_id': 'int',
        'pref_name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'pref_name': 'pref_name',
        'value': 'value'
    }

    def __init__(self, user_id=None, pref_name=None, value=None):  # noqa: E501
        """UserPrefs - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._pref_name = None
        self._value = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if pref_name is not None:
            self.pref_name = pref_name
        if value is not None:
            self.value = value

    @property
    def user_id(self):
        """Gets the user_id of this UserPrefs.  # noqa: E501


        :return: The user_id of this UserPrefs.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserPrefs.


        :param user_id: The user_id of this UserPrefs.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def pref_name(self):
        """Gets the pref_name of this UserPrefs.  # noqa: E501


        :return: The pref_name of this UserPrefs.  # noqa: E501
        :rtype: str
        """
        return self._pref_name

    @pref_name.setter
    def pref_name(self, pref_name):
        """Sets the pref_name of this UserPrefs.


        :param pref_name: The pref_name of this UserPrefs.  # noqa: E501
        :type: str
        """

        self._pref_name = pref_name

    @property
    def value(self):
        """Gets the value of this UserPrefs.  # noqa: E501


        :return: The value of this UserPrefs.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UserPrefs.


        :param value: The value of this UserPrefs.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(UserPrefs, dict):
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
        if not isinstance(other, UserPrefs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
