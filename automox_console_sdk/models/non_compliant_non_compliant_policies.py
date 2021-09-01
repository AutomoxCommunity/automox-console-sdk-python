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

class NonCompliantNonCompliantPolicies(object):
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
        'name': 'str',
        'type': 'str',
        'reason_for_fail': 'str',
        'policy_create_time': 'datetime',
        'severity': 'str',
        'packages': 'list[NonCompliantNonCompliantPackages]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'reason_for_fail': 'reasonForFail',
        'policy_create_time': 'policyCreateTime',
        'severity': 'severity',
        'packages': 'packages'
    }

    def __init__(self, id=None, name=None, type=None, reason_for_fail=None, policy_create_time=None, severity=None, packages=None):  # noqa: E501
        """NonCompliantNonCompliantPolicies - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._type = None
        self._reason_for_fail = None
        self._policy_create_time = None
        self._severity = None
        self._packages = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if reason_for_fail is not None:
            self.reason_for_fail = reason_for_fail
        if policy_create_time is not None:
            self.policy_create_time = policy_create_time
        if severity is not None:
            self.severity = severity
        if packages is not None:
            self.packages = packages

    @property
    def id(self):
        """Gets the id of this NonCompliantNonCompliantPolicies.  # noqa: E501


        :return: The id of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NonCompliantNonCompliantPolicies.


        :param id: The id of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NonCompliantNonCompliantPolicies.  # noqa: E501


        :return: The name of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NonCompliantNonCompliantPolicies.


        :param name: The name of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this NonCompliantNonCompliantPolicies.  # noqa: E501


        :return: The type of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NonCompliantNonCompliantPolicies.


        :param type: The type of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def reason_for_fail(self):
        """Gets the reason_for_fail of this NonCompliantNonCompliantPolicies.  # noqa: E501


        :return: The reason_for_fail of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :rtype: str
        """
        return self._reason_for_fail

    @reason_for_fail.setter
    def reason_for_fail(self, reason_for_fail):
        """Sets the reason_for_fail of this NonCompliantNonCompliantPolicies.


        :param reason_for_fail: The reason_for_fail of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :type: str
        """

        self._reason_for_fail = reason_for_fail

    @property
    def policy_create_time(self):
        """Gets the policy_create_time of this NonCompliantNonCompliantPolicies.  # noqa: E501


        :return: The policy_create_time of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :rtype: datetime
        """
        return self._policy_create_time

    @policy_create_time.setter
    def policy_create_time(self, policy_create_time):
        """Sets the policy_create_time of this NonCompliantNonCompliantPolicies.


        :param policy_create_time: The policy_create_time of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :type: datetime
        """

        self._policy_create_time = policy_create_time

    @property
    def severity(self):
        """Gets the severity of this NonCompliantNonCompliantPolicies.  # noqa: E501


        :return: The severity of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this NonCompliantNonCompliantPolicies.


        :param severity: The severity of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def packages(self):
        """Gets the packages of this NonCompliantNonCompliantPolicies.  # noqa: E501


        :return: The packages of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :rtype: list[NonCompliantNonCompliantPackages]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this NonCompliantNonCompliantPolicies.


        :param packages: The packages of this NonCompliantNonCompliantPolicies.  # noqa: E501
        :type: list[NonCompliantNonCompliantPackages]
        """

        self._packages = packages

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
        if issubclass(NonCompliantNonCompliantPolicies, dict):
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
        if not isinstance(other, NonCompliantNonCompliantPolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
