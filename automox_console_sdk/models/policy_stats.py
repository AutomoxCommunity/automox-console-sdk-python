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

class PolicyStats(object):
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
        'compliant': 'int',
        'noncompliant': 'int',
        'organization_id': 'int',
        'pending': 'int',
        'policy_id': 'int',
        'policy_name': 'str',
        'policy_type_name': 'str'
    }

    attribute_map = {
        'compliant': 'compliant',
        'noncompliant': 'noncompliant',
        'organization_id': 'organization_id',
        'pending': 'pending',
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'policy_type_name': 'policy_type_name'
    }

    def __init__(self, compliant=None, noncompliant=None, organization_id=None, pending=None, policy_id=None, policy_name=None, policy_type_name=None):  # noqa: E501
        """PolicyStats - a model defined in Swagger"""  # noqa: E501
        self._compliant = None
        self._noncompliant = None
        self._organization_id = None
        self._pending = None
        self._policy_id = None
        self._policy_name = None
        self._policy_type_name = None
        self.discriminator = None
        if compliant is not None:
            self.compliant = compliant
        if noncompliant is not None:
            self.noncompliant = noncompliant
        if organization_id is not None:
            self.organization_id = organization_id
        if pending is not None:
            self.pending = pending
        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_type_name is not None:
            self.policy_type_name = policy_type_name

    @property
    def compliant(self):
        """Gets the compliant of this PolicyStats.  # noqa: E501


        :return: The compliant of this PolicyStats.  # noqa: E501
        :rtype: int
        """
        return self._compliant

    @compliant.setter
    def compliant(self, compliant):
        """Sets the compliant of this PolicyStats.


        :param compliant: The compliant of this PolicyStats.  # noqa: E501
        :type: int
        """

        self._compliant = compliant

    @property
    def noncompliant(self):
        """Gets the noncompliant of this PolicyStats.  # noqa: E501


        :return: The noncompliant of this PolicyStats.  # noqa: E501
        :rtype: int
        """
        return self._noncompliant

    @noncompliant.setter
    def noncompliant(self, noncompliant):
        """Sets the noncompliant of this PolicyStats.


        :param noncompliant: The noncompliant of this PolicyStats.  # noqa: E501
        :type: int
        """

        self._noncompliant = noncompliant

    @property
    def organization_id(self):
        """Gets the organization_id of this PolicyStats.  # noqa: E501


        :return: The organization_id of this PolicyStats.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this PolicyStats.


        :param organization_id: The organization_id of this PolicyStats.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def pending(self):
        """Gets the pending of this PolicyStats.  # noqa: E501


        :return: The pending of this PolicyStats.  # noqa: E501
        :rtype: int
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this PolicyStats.


        :param pending: The pending of this PolicyStats.  # noqa: E501
        :type: int
        """

        self._pending = pending

    @property
    def policy_id(self):
        """Gets the policy_id of this PolicyStats.  # noqa: E501


        :return: The policy_id of this PolicyStats.  # noqa: E501
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this PolicyStats.


        :param policy_id: The policy_id of this PolicyStats.  # noqa: E501
        :type: int
        """

        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this PolicyStats.  # noqa: E501


        :return: The policy_name of this PolicyStats.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this PolicyStats.


        :param policy_name: The policy_name of this PolicyStats.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def policy_type_name(self):
        """Gets the policy_type_name of this PolicyStats.  # noqa: E501


        :return: The policy_type_name of this PolicyStats.  # noqa: E501
        :rtype: str
        """
        return self._policy_type_name

    @policy_type_name.setter
    def policy_type_name(self, policy_type_name):
        """Sets the policy_type_name of this PolicyStats.


        :param policy_type_name: The policy_type_name of this PolicyStats.  # noqa: E501
        :type: str
        """
        allowed_values = ["patch", "custom", "required_software"]  # noqa: E501
        if policy_type_name not in allowed_values:
            raise ValueError(
                "Invalid value for `policy_type_name` ({0}), must be one of {1}"  # noqa: E501
                .format(policy_type_name, allowed_values)
            )

        self._policy_type_name = policy_type_name

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
        if issubclass(PolicyStats, dict):
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
        if not isinstance(other, PolicyStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
