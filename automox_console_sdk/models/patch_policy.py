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

class PatchPolicy(object):
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
        'policy_type_name': 'str',
        'configuration': 'OneOfPatchPolicyConfiguration',
        'schedule_days': 'int',
        'schedule_weeks_of_month': 'int',
        'schedule_months': 'int',
        'schedule_time': 'str',
        'server_groups': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'organization_id': 'organization_id',
        'name': 'name',
        'policy_type_name': 'policy_type_name',
        'configuration': 'configuration',
        'schedule_days': 'schedule_days',
        'schedule_weeks_of_month': 'schedule_weeks_of_month',
        'schedule_months': 'schedule_months',
        'schedule_time': 'schedule_time',
        'server_groups': 'server_groups'
    }

    def __init__(self, id=None, organization_id=None, name=None, policy_type_name=None, configuration=None, schedule_days=None, schedule_weeks_of_month=None, schedule_months=None, schedule_time=None, server_groups=None):  # noqa: E501
        """PatchPolicy - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._organization_id = None
        self._name = None
        self._policy_type_name = None
        self._configuration = None
        self._schedule_days = None
        self._schedule_weeks_of_month = None
        self._schedule_months = None
        self._schedule_time = None
        self._server_groups = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.organization_id = organization_id
        self.name = name
        self.policy_type_name = policy_type_name
        self.configuration = configuration
        self.schedule_days = schedule_days
        if schedule_weeks_of_month is not None:
            self.schedule_weeks_of_month = schedule_weeks_of_month
        if schedule_months is not None:
            self.schedule_months = schedule_months
        self.schedule_time = schedule_time
        self.server_groups = server_groups

    @property
    def id(self):
        """Gets the id of this PatchPolicy.  # noqa: E501

        Policy ID  # noqa: E501

        :return: The id of this PatchPolicy.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PatchPolicy.

        Policy ID  # noqa: E501

        :param id: The id of this PatchPolicy.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def organization_id(self):
        """Gets the organization_id of this PatchPolicy.  # noqa: E501

        Organization ID for the specified policy  # noqa: E501

        :return: The organization_id of this PatchPolicy.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this PatchPolicy.

        Organization ID for the specified policy  # noqa: E501

        :param organization_id: The organization_id of this PatchPolicy.  # noqa: E501
        :type: int
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def name(self):
        """Gets the name of this PatchPolicy.  # noqa: E501

        The name of the policy  # noqa: E501

        :return: The name of this PatchPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchPolicy.

        The name of the policy  # noqa: E501

        :param name: The name of this PatchPolicy.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def policy_type_name(self):
        """Gets the policy_type_name of this PatchPolicy.  # noqa: E501

        The name of the type of policy you are creating. Optional when updating an existing policy.  # noqa: E501

        :return: The policy_type_name of this PatchPolicy.  # noqa: E501
        :rtype: str
        """
        return self._policy_type_name

    @policy_type_name.setter
    def policy_type_name(self, policy_type_name):
        """Sets the policy_type_name of this PatchPolicy.

        The name of the type of policy you are creating. Optional when updating an existing policy.  # noqa: E501

        :param policy_type_name: The policy_type_name of this PatchPolicy.  # noqa: E501
        :type: str
        """
        if policy_type_name is None:
            raise ValueError("Invalid value for `policy_type_name`, must not be `None`")  # noqa: E501
        allowed_values = ["patch", "custom", "required_software"]  # noqa: E501
        if policy_type_name not in allowed_values:
            raise ValueError(
                "Invalid value for `policy_type_name` ({0}), must be one of {1}"  # noqa: E501
                .format(policy_type_name, allowed_values)
            )

        self._policy_type_name = policy_type_name

    @property
    def configuration(self):
        """Gets the configuration of this PatchPolicy.  # noqa: E501

        The policy configuration. This varies depending on the type of policy being used.  # noqa: E501

        :return: The configuration of this PatchPolicy.  # noqa: E501
        :rtype: OneOfPatchPolicyConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this PatchPolicy.

        The policy configuration. This varies depending on the type of policy being used.  # noqa: E501

        :param configuration: The configuration of this PatchPolicy.  # noqa: E501
        :type: OneOfPatchPolicyConfiguration
        """
        if configuration is None:
            raise ValueError("Invalid value for `configuration`, must not be `None`")  # noqa: E501

        self._configuration = configuration

    @property
    def schedule_days(self):
        """Gets the schedule_days of this PatchPolicy.  # noqa: E501

        Decimal value of binary day schedule. See [Policy and Device Filters, and Scheduling - Example Days per Week](/developer-portal/policy_filters_schedule/#example-days-per-week).  # noqa: E501

        :return: The schedule_days of this PatchPolicy.  # noqa: E501
        :rtype: int
        """
        return self._schedule_days

    @schedule_days.setter
    def schedule_days(self, schedule_days):
        """Sets the schedule_days of this PatchPolicy.

        Decimal value of binary day schedule. See [Policy and Device Filters, and Scheduling - Example Days per Week](/developer-portal/policy_filters_schedule/#example-days-per-week).  # noqa: E501

        :param schedule_days: The schedule_days of this PatchPolicy.  # noqa: E501
        :type: int
        """
        if schedule_days is None:
            raise ValueError("Invalid value for `schedule_days`, must not be `None`")  # noqa: E501

        self._schedule_days = schedule_days

    @property
    def schedule_weeks_of_month(self):
        """Gets the schedule_weeks_of_month of this PatchPolicy.  # noqa: E501

        Decimal value of binary week schedule. See [Policy and Device Filters, and Scheduling - Example Weeks per Month](/developer-portal/policy_filters_schedule/#example-weeks-per-month).  # noqa: E501

        :return: The schedule_weeks_of_month of this PatchPolicy.  # noqa: E501
        :rtype: int
        """
        return self._schedule_weeks_of_month

    @schedule_weeks_of_month.setter
    def schedule_weeks_of_month(self, schedule_weeks_of_month):
        """Sets the schedule_weeks_of_month of this PatchPolicy.

        Decimal value of binary week schedule. See [Policy and Device Filters, and Scheduling - Example Weeks per Month](/developer-portal/policy_filters_schedule/#example-weeks-per-month).  # noqa: E501

        :param schedule_weeks_of_month: The schedule_weeks_of_month of this PatchPolicy.  # noqa: E501
        :type: int
        """

        self._schedule_weeks_of_month = schedule_weeks_of_month

    @property
    def schedule_months(self):
        """Gets the schedule_months of this PatchPolicy.  # noqa: E501

        Decimal value of binary month schedule. See [Policy and Device Filters, and Scheduling - Example Months per Year](/developer-portal/policy_filters_schedule/#example-months-per-year).  # noqa: E501

        :return: The schedule_months of this PatchPolicy.  # noqa: E501
        :rtype: int
        """
        return self._schedule_months

    @schedule_months.setter
    def schedule_months(self, schedule_months):
        """Sets the schedule_months of this PatchPolicy.

        Decimal value of binary month schedule. See [Policy and Device Filters, and Scheduling - Example Months per Year](/developer-portal/policy_filters_schedule/#example-months-per-year).  # noqa: E501

        :param schedule_months: The schedule_months of this PatchPolicy.  # noqa: E501
        :type: int
        """

        self._schedule_months = schedule_months

    @property
    def schedule_time(self):
        """Gets the schedule_time of this PatchPolicy.  # noqa: E501

        Scheduled time for automatic policy execution. Format: `\"hh:mm\"`  # noqa: E501

        :return: The schedule_time of this PatchPolicy.  # noqa: E501
        :rtype: str
        """
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, schedule_time):
        """Sets the schedule_time of this PatchPolicy.

        Scheduled time for automatic policy execution. Format: `\"hh:mm\"`  # noqa: E501

        :param schedule_time: The schedule_time of this PatchPolicy.  # noqa: E501
        :type: str
        """
        if schedule_time is None:
            raise ValueError("Invalid value for `schedule_time`, must not be `None`")  # noqa: E501

        self._schedule_time = schedule_time

    @property
    def server_groups(self):
        """Gets the server_groups of this PatchPolicy.  # noqa: E501

        An array containing a list of the server group IDs to be affected by the policy.  # noqa: E501

        :return: The server_groups of this PatchPolicy.  # noqa: E501
        :rtype: list[int]
        """
        return self._server_groups

    @server_groups.setter
    def server_groups(self, server_groups):
        """Sets the server_groups of this PatchPolicy.

        An array containing a list of the server group IDs to be affected by the policy.  # noqa: E501

        :param server_groups: The server_groups of this PatchPolicy.  # noqa: E501
        :type: list[int]
        """
        if server_groups is None:
            raise ValueError("Invalid value for `server_groups`, must not be `None`")  # noqa: E501

        self._server_groups = server_groups

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
        if issubclass(PatchPolicy, dict):
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
        if not isinstance(other, PatchPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
