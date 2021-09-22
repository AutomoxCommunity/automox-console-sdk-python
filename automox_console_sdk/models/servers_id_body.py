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

class ServersIdBody(object):
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
        'server_group_id': 'int',
        'ip_addrs': 'str',
        'exception': 'bool',
        'tags': 'list[str]',
        'custom_name': 'str'
    }

    attribute_map = {
        'server_group_id': 'server_group_id',
        'ip_addrs': 'ip_addrs',
        'exception': 'exception',
        'tags': 'tags',
        'custom_name': 'custom_name'
    }

    def __init__(self, server_group_id=None, ip_addrs=None, exception=None, tags=None, custom_name=None):  # noqa: E501
        """ServersIdBody - a model defined in Swagger"""  # noqa: E501
        self._server_group_id = None
        self._ip_addrs = None
        self._exception = None
        self._tags = None
        self._custom_name = None
        self.discriminator = None
        self.server_group_id = server_group_id
        if ip_addrs is not None:
            self.ip_addrs = ip_addrs
        self.exception = exception
        if tags is not None:
            self.tags = tags
        if custom_name is not None:
            self.custom_name = custom_name

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ServersIdBody.  # noqa: E501

        Server Group ID for the specified group.  # noqa: E501

        :return: The server_group_id of this ServersIdBody.  # noqa: E501
        :rtype: int
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ServersIdBody.

        Server Group ID for the specified group.  # noqa: E501

        :param server_group_id: The server_group_id of this ServersIdBody.  # noqa: E501
        :type: int
        """
        if server_group_id is None:
            raise ValueError("Invalid value for `server_group_id`, must not be `None`")  # noqa: E501

        self._server_group_id = server_group_id

    @property
    def ip_addrs(self):
        """Gets the ip_addrs of this ServersIdBody.  # noqa: E501

        Server IP address.  # noqa: E501

        :return: The ip_addrs of this ServersIdBody.  # noqa: E501
        :rtype: str
        """
        return self._ip_addrs

    @ip_addrs.setter
    def ip_addrs(self, ip_addrs):
        """Sets the ip_addrs of this ServersIdBody.

        Server IP address.  # noqa: E501

        :param ip_addrs: The ip_addrs of this ServersIdBody.  # noqa: E501
        :type: str
        """

        self._ip_addrs = ip_addrs

    @property
    def exception(self):
        """Gets the exception of this ServersIdBody.  # noqa: E501

        Use the exception property to exclude the device from reports and statistics.  # noqa: E501

        :return: The exception of this ServersIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._exception

    @exception.setter
    def exception(self, exception):
        """Sets the exception of this ServersIdBody.

        Use the exception property to exclude the device from reports and statistics.  # noqa: E501

        :param exception: The exception of this ServersIdBody.  # noqa: E501
        :type: bool
        """
        if exception is None:
            raise ValueError("Invalid value for `exception`, must not be `None`")  # noqa: E501

        self._exception = exception

    @property
    def tags(self):
        """Gets the tags of this ServersIdBody.  # noqa: E501

        List of tags.  # noqa: E501

        :return: The tags of this ServersIdBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ServersIdBody.

        List of tags.  # noqa: E501

        :param tags: The tags of this ServersIdBody.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def custom_name(self):
        """Gets the custom_name of this ServersIdBody.  # noqa: E501

        Custom name that will display in the console instead of the hostname.  # noqa: E501

        :return: The custom_name of this ServersIdBody.  # noqa: E501
        :rtype: str
        """
        return self._custom_name

    @custom_name.setter
    def custom_name(self, custom_name):
        """Sets the custom_name of this ServersIdBody.

        Custom name that will display in the console instead of the hostname.  # noqa: E501

        :param custom_name: The custom_name of this ServersIdBody.  # noqa: E501
        :type: str
        """

        self._custom_name = custom_name

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
        if issubclass(ServersIdBody, dict):
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
        if not isinstance(other, ServersIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
