# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-11-16
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserIdApiKeysBody(object):
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
        'name': 'str',
        'expires_at': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'expires_at': 'expires_at'
    }

    def __init__(self, name=None, expires_at=None):  # noqa: E501
        """UserIdApiKeysBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._expires_at = None
        self.discriminator = None
        self.name = name
        if expires_at is not None:
            self.expires_at = expires_at

    @property
    def name(self):
        """Gets the name of this UserIdApiKeysBody.  # noqa: E501

        A unique name for this key. Users are not allowed to have two keys with the same name under a given organization.  # noqa: E501

        :return: The name of this UserIdApiKeysBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserIdApiKeysBody.

        A unique name for this key. Users are not allowed to have two keys with the same name under a given organization.  # noqa: E501

        :param name: The name of this UserIdApiKeysBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def expires_at(self):
        """Gets the expires_at of this UserIdApiKeysBody.  # noqa: E501

        The time at which (in UTC) the key should automatically expire. Format is ISO8601. Example: 2020-08-05T18:21:47+0000  # noqa: E501

        :return: The expires_at of this UserIdApiKeysBody.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this UserIdApiKeysBody.

        The time at which (in UTC) the key should automatically expire. Format is ISO8601. Example: 2020-08-05T18:21:47+0000  # noqa: E501

        :param expires_at: The expires_at of this UserIdApiKeysBody.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

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
        if issubclass(UserIdApiKeysBody, dict):
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
        if not isinstance(other, UserIdApiKeysBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
