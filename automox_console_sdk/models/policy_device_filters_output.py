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

class PolicyDeviceFiltersOutput(object):
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
        'results': 'list[PolicyDeviceFiltersOutputResults]',
        'size': 'int'
    }

    attribute_map = {
        'results': 'results',
        'size': 'size'
    }

    def __init__(self, results=None, size=None):  # noqa: E501
        """PolicyDeviceFiltersOutput - a model defined in Swagger"""  # noqa: E501
        self._results = None
        self._size = None
        self.discriminator = None
        if results is not None:
            self.results = results
        if size is not None:
            self.size = size

    @property
    def results(self):
        """Gets the results of this PolicyDeviceFiltersOutput.  # noqa: E501


        :return: The results of this PolicyDeviceFiltersOutput.  # noqa: E501
        :rtype: list[PolicyDeviceFiltersOutputResults]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PolicyDeviceFiltersOutput.


        :param results: The results of this PolicyDeviceFiltersOutput.  # noqa: E501
        :type: list[PolicyDeviceFiltersOutputResults]
        """

        self._results = results

    @property
    def size(self):
        """Gets the size of this PolicyDeviceFiltersOutput.  # noqa: E501


        :return: The size of this PolicyDeviceFiltersOutput.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PolicyDeviceFiltersOutput.


        :param size: The size of this PolicyDeviceFiltersOutput.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if issubclass(PolicyDeviceFiltersOutput, dict):
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
        if not isinstance(other, PolicyDeviceFiltersOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
