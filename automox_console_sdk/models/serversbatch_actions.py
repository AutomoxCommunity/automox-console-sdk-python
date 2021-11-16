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

class ServersbatchActions(object):
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
        'attribute': 'str',
        'action': 'str',
        'value': 'list[str]'
    }

    attribute_map = {
        'attribute': 'attribute',
        'action': 'action',
        'value': 'value'
    }

    def __init__(self, attribute=None, action=None, value=None):  # noqa: E501
        """ServersbatchActions - a model defined in Swagger"""  # noqa: E501
        self._attribute = None
        self._action = None
        self._value = None
        self.discriminator = None
        if attribute is not None:
            self.attribute = attribute
        if action is not None:
            self.action = action
        if value is not None:
            self.value = value

    @property
    def attribute(self):
        """Gets the attribute of this ServersbatchActions.  # noqa: E501

        Name of the attribute  # noqa: E501

        :return: The attribute of this ServersbatchActions.  # noqa: E501
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this ServersbatchActions.

        Name of the attribute  # noqa: E501

        :param attribute: The attribute of this ServersbatchActions.  # noqa: E501
        :type: str
        """
        allowed_values = ["tags"]  # noqa: E501
        if attribute not in allowed_values:
            raise ValueError(
                "Invalid value for `attribute` ({0}), must be one of {1}"  # noqa: E501
                .format(attribute, allowed_values)
            )

        self._attribute = attribute

    @property
    def action(self):
        """Gets the action of this ServersbatchActions.  # noqa: E501

        What action should be taken  # noqa: E501

        :return: The action of this ServersbatchActions.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ServersbatchActions.

        What action should be taken  # noqa: E501

        :param action: The action of this ServersbatchActions.  # noqa: E501
        :type: str
        """
        allowed_values = ["apply", "remove"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def value(self):
        """Gets the value of this ServersbatchActions.  # noqa: E501

        The value to use for the action  # noqa: E501

        :return: The value of this ServersbatchActions.  # noqa: E501
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ServersbatchActions.

        The value to use for the action  # noqa: E501

        :param value: The value of this ServersbatchActions.  # noqa: E501
        :type: list[str]
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
        if issubclass(ServersbatchActions, dict):
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
        if not isinstance(other, ServersbatchActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
