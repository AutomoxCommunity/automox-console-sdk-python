# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-09-01
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PatchPolicyConfigurationAdvancedFilter(object):
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
        'left': 'str',
        'right': 'str',
        'condition': 'str'
    }

    attribute_map = {
        'left': 'left',
        'right': 'right',
        'condition': 'condition'
    }

    def __init__(self, left=None, right=None, condition=None):  # noqa: E501
        """PatchPolicyConfigurationAdvancedFilter - a model defined in Swagger"""  # noqa: E501
        self._left = None
        self._right = None
        self._condition = None
        self.discriminator = None
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        if condition is not None:
            self.condition = condition

    @property
    def left(self):
        """Gets the left of this PatchPolicyConfigurationAdvancedFilter.  # noqa: E501


        :return: The left of this PatchPolicyConfigurationAdvancedFilter.  # noqa: E501
        :rtype: str
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this PatchPolicyConfigurationAdvancedFilter.


        :param left: The left of this PatchPolicyConfigurationAdvancedFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["display-name", "severity", "patch-source", "patch-os", "type"]  # noqa: E501
        if left not in allowed_values:
            raise ValueError(
                "Invalid value for `left` ({0}), must be one of {1}"  # noqa: E501
                .format(left, allowed_values)
            )

        self._left = left

    @property
    def right(self):
        """Gets the right of this PatchPolicyConfigurationAdvancedFilter.  # noqa: E501


        :return: The right of this PatchPolicyConfigurationAdvancedFilter.  # noqa: E501
        :rtype: str
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this PatchPolicyConfigurationAdvancedFilter.


        :param right: The right of this PatchPolicyConfigurationAdvancedFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["text string", "other", "none", "low", "medium", "high", "critical", "windowsupdate", "opera", "mozilla", "adobe", "oracle", "apple", "microsoft", "windows", "mac", "linux", "upgrades", "updates", "update-rollups", "service-packs", "security-updates", "tools", "guidance", "feature-packs", "developer-kits", "definition-updates", "critical-updates", "connectors", "application"]  # noqa: E501
        if right not in allowed_values:
            raise ValueError(
                "Invalid value for `right` ({0}), must be one of {1}"  # noqa: E501
                .format(right, allowed_values)
            )

        self._right = right

    @property
    def condition(self):
        """Gets the condition of this PatchPolicyConfigurationAdvancedFilter.  # noqa: E501


        :return: The condition of this PatchPolicyConfigurationAdvancedFilter.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this PatchPolicyConfigurationAdvancedFilter.


        :param condition: The condition of this PatchPolicyConfigurationAdvancedFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["contains", "does-not-contain", "is", "is-not", "less-than-or-equal-to", "greater-than-or-equal-to"]  # noqa: E501
        if condition not in allowed_values:
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

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
        if issubclass(PatchPolicyConfigurationAdvancedFilter, dict):
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
        if not isinstance(other, PatchPolicyConfigurationAdvancedFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
