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

class PrePatchPrepatch(object):
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
        'total': 'int',
        'needs_attention': 'int',
        '_none': 'int',
        'low': 'int',
        'medium': 'int',
        'high': 'int',
        'critical': 'int',
        'other': 'int',
        'devices': 'list[PrePatchPrepatchDevices]'
    }

    attribute_map = {
        'total': 'total',
        'needs_attention': 'needsAttention',
        '_none': 'none',
        'low': 'low',
        'medium': 'medium',
        'high': 'high',
        'critical': 'critical',
        'other': 'other',
        'devices': 'devices'
    }

    def __init__(self, total=None, needs_attention=None, _none=None, low=None, medium=None, high=None, critical=None, other=None, devices=None):  # noqa: E501
        """PrePatchPrepatch - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._needs_attention = None
        self.__none = None
        self._low = None
        self._medium = None
        self._high = None
        self._critical = None
        self._other = None
        self._devices = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if needs_attention is not None:
            self.needs_attention = needs_attention
        if _none is not None:
            self._none = _none
        if low is not None:
            self.low = low
        if medium is not None:
            self.medium = medium
        if high is not None:
            self.high = high
        if critical is not None:
            self.critical = critical
        if other is not None:
            self.other = other
        if devices is not None:
            self.devices = devices

    @property
    def total(self):
        """Gets the total of this PrePatchPrepatch.  # noqa: E501


        :return: The total of this PrePatchPrepatch.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PrePatchPrepatch.


        :param total: The total of this PrePatchPrepatch.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def needs_attention(self):
        """Gets the needs_attention of this PrePatchPrepatch.  # noqa: E501


        :return: The needs_attention of this PrePatchPrepatch.  # noqa: E501
        :rtype: int
        """
        return self._needs_attention

    @needs_attention.setter
    def needs_attention(self, needs_attention):
        """Sets the needs_attention of this PrePatchPrepatch.


        :param needs_attention: The needs_attention of this PrePatchPrepatch.  # noqa: E501
        :type: int
        """

        self._needs_attention = needs_attention

    @property
    def _none(self):
        """Gets the _none of this PrePatchPrepatch.  # noqa: E501


        :return: The _none of this PrePatchPrepatch.  # noqa: E501
        :rtype: int
        """
        return self.__none

    @_none.setter
    def _none(self, _none):
        """Sets the _none of this PrePatchPrepatch.


        :param _none: The _none of this PrePatchPrepatch.  # noqa: E501
        :type: int
        """

        self.__none = _none

    @property
    def low(self):
        """Gets the low of this PrePatchPrepatch.  # noqa: E501


        :return: The low of this PrePatchPrepatch.  # noqa: E501
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this PrePatchPrepatch.


        :param low: The low of this PrePatchPrepatch.  # noqa: E501
        :type: int
        """

        self._low = low

    @property
    def medium(self):
        """Gets the medium of this PrePatchPrepatch.  # noqa: E501


        :return: The medium of this PrePatchPrepatch.  # noqa: E501
        :rtype: int
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """Sets the medium of this PrePatchPrepatch.


        :param medium: The medium of this PrePatchPrepatch.  # noqa: E501
        :type: int
        """

        self._medium = medium

    @property
    def high(self):
        """Gets the high of this PrePatchPrepatch.  # noqa: E501


        :return: The high of this PrePatchPrepatch.  # noqa: E501
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this PrePatchPrepatch.


        :param high: The high of this PrePatchPrepatch.  # noqa: E501
        :type: int
        """

        self._high = high

    @property
    def critical(self):
        """Gets the critical of this PrePatchPrepatch.  # noqa: E501


        :return: The critical of this PrePatchPrepatch.  # noqa: E501
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this PrePatchPrepatch.


        :param critical: The critical of this PrePatchPrepatch.  # noqa: E501
        :type: int
        """

        self._critical = critical

    @property
    def other(self):
        """Gets the other of this PrePatchPrepatch.  # noqa: E501


        :return: The other of this PrePatchPrepatch.  # noqa: E501
        :rtype: int
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this PrePatchPrepatch.


        :param other: The other of this PrePatchPrepatch.  # noqa: E501
        :type: int
        """

        self._other = other

    @property
    def devices(self):
        """Gets the devices of this PrePatchPrepatch.  # noqa: E501


        :return: The devices of this PrePatchPrepatch.  # noqa: E501
        :rtype: list[PrePatchPrepatchDevices]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this PrePatchPrepatch.


        :param devices: The devices of this PrePatchPrepatch.  # noqa: E501
        :type: list[PrePatchPrepatchDevices]
        """

        self._devices = devices

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
        if issubclass(PrePatchPrepatch, dict):
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
        if not isinstance(other, PrePatchPrepatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
