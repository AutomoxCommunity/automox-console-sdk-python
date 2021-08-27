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

class SystemEventData(object):
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
        'ip': 'str',
        'os': 'str',
        'systemname': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'os': 'os',
        'systemname': 'systemname'
    }

    def __init__(self, ip=None, os=None, systemname=None):  # noqa: E501
        """SystemEventData - a model defined in Swagger"""  # noqa: E501
        self._ip = None
        self._os = None
        self._systemname = None
        self.discriminator = None
        if ip is not None:
            self.ip = ip
        if os is not None:
            self.os = os
        if systemname is not None:
            self.systemname = systemname

    @property
    def ip(self):
        """Gets the ip of this SystemEventData.  # noqa: E501


        :return: The ip of this SystemEventData.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SystemEventData.


        :param ip: The ip of this SystemEventData.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def os(self):
        """Gets the os of this SystemEventData.  # noqa: E501


        :return: The os of this SystemEventData.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this SystemEventData.


        :param os: The os of this SystemEventData.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def systemname(self):
        """Gets the systemname of this SystemEventData.  # noqa: E501


        :return: The systemname of this SystemEventData.  # noqa: E501
        :rtype: str
        """
        return self._systemname

    @systemname.setter
    def systemname(self, systemname):
        """Sets the systemname of this SystemEventData.


        :param systemname: The systemname of this SystemEventData.  # noqa: E501
        :type: str
        """

        self._systemname = systemname

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
        if issubclass(SystemEventData, dict):
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
        if not isinstance(other, SystemEventData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
