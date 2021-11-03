# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-10-04
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DataextractsParameters(object):
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
        'start_time': 'datetime',
        'end_time': 'datetime'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, start_time=None, end_time=None):  # noqa: E501
        """DataextractsParameters - a model defined in Swagger"""  # noqa: E501
        self._start_time = None
        self._end_time = None
        self.discriminator = None
        self.start_time = start_time
        self.end_time = end_time

    @property
    def start_time(self):
        """Gets the start_time of this DataextractsParameters.  # noqa: E501

        The start date and time for the report. Validation: Previous 90 days, starting yesterday.  # noqa: E501

        :return: The start_time of this DataextractsParameters.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DataextractsParameters.

        The start date and time for the report. Validation: Previous 90 days, starting yesterday.  # noqa: E501

        :param start_time: The start_time of this DataextractsParameters.  # noqa: E501
        :type: datetime
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this DataextractsParameters.  # noqa: E501

        The end date and time for the report. Validation: Previous 90 days, starting yesterday and must be after start_time.  # noqa: E501

        :return: The end_time of this DataextractsParameters.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DataextractsParameters.

        The end date and time for the report. Validation: Previous 90 days, starting yesterday and must be after start_time.  # noqa: E501

        :param end_time: The end_time of this DataextractsParameters.  # noqa: E501
        :type: datetime
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

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
        if issubclass(DataextractsParameters, dict):
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
        if not isinstance(other, DataextractsParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
