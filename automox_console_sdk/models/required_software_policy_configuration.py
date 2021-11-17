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

class RequiredSoftwarePolicyConfiguration(object):
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
        'device_filters_enabled': 'bool',
        'device_filters': 'DeviceFilters',
        'missed_patch_window': 'bool',
        'os_family': 'str',
        'package_name': 'str',
        'package_version': 'str',
        'installation_code': 'str'
    }

    attribute_map = {
        'device_filters_enabled': 'device_filters_enabled',
        'device_filters': 'device_filters',
        'missed_patch_window': 'missed_patch_window',
        'os_family': 'os_family',
        'package_name': 'package_name',
        'package_version': 'package_version',
        'installation_code': 'installation_code'
    }

    def __init__(self, device_filters_enabled=False, device_filters=None, missed_patch_window=None, os_family=None, package_name=None, package_version=None, installation_code=None):  # noqa: E501
        """RequiredSoftwarePolicyConfiguration - a model defined in Swagger"""  # noqa: E501
        self._device_filters_enabled = None
        self._device_filters = None
        self._missed_patch_window = None
        self._os_family = None
        self._package_name = None
        self._package_version = None
        self._installation_code = None
        self.discriminator = None
        if device_filters_enabled is not None:
            self.device_filters_enabled = device_filters_enabled
        if device_filters is not None:
            self.device_filters = device_filters
        if missed_patch_window is not None:
            self.missed_patch_window = missed_patch_window
        if os_family is not None:
            self.os_family = os_family
        self.package_name = package_name
        self.package_version = package_version
        self.installation_code = installation_code

    @property
    def device_filters_enabled(self):
        """Gets the device_filters_enabled of this RequiredSoftwarePolicyConfiguration.  # noqa: E501

        Enable or disable Device Filters.  # noqa: E501

        :return: The device_filters_enabled of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._device_filters_enabled

    @device_filters_enabled.setter
    def device_filters_enabled(self, device_filters_enabled):
        """Sets the device_filters_enabled of this RequiredSoftwarePolicyConfiguration.

        Enable or disable Device Filters.  # noqa: E501

        :param device_filters_enabled: The device_filters_enabled of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :type: bool
        """

        self._device_filters_enabled = device_filters_enabled

    @property
    def device_filters(self):
        """Gets the device_filters of this RequiredSoftwarePolicyConfiguration.  # noqa: E501


        :return: The device_filters of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :rtype: DeviceFilters
        """
        return self._device_filters

    @device_filters.setter
    def device_filters(self, device_filters):
        """Sets the device_filters of this RequiredSoftwarePolicyConfiguration.


        :param device_filters: The device_filters of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :type: DeviceFilters
        """

        self._device_filters = device_filters

    @property
    def missed_patch_window(self):
        """Gets the missed_patch_window of this RequiredSoftwarePolicyConfiguration.  # noqa: E501

        Enable or Disable Missed Patch Window setting  # noqa: E501

        :return: The missed_patch_window of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._missed_patch_window

    @missed_patch_window.setter
    def missed_patch_window(self, missed_patch_window):
        """Sets the missed_patch_window of this RequiredSoftwarePolicyConfiguration.

        Enable or Disable Missed Patch Window setting  # noqa: E501

        :param missed_patch_window: The missed_patch_window of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :type: bool
        """

        self._missed_patch_window = missed_patch_window

    @property
    def os_family(self):
        """Gets the os_family of this RequiredSoftwarePolicyConfiguration.  # noqa: E501


        :return: The os_family of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """Sets the os_family of this RequiredSoftwarePolicyConfiguration.


        :param os_family: The os_family of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :type: str
        """

        self._os_family = os_family

    @property
    def package_name(self):
        """Gets the package_name of this RequiredSoftwarePolicyConfiguration.  # noqa: E501


        :return: The package_name of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this RequiredSoftwarePolicyConfiguration.


        :param package_name: The package_name of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :type: str
        """
        if package_name is None:
            raise ValueError("Invalid value for `package_name`, must not be `None`")  # noqa: E501

        self._package_name = package_name

    @property
    def package_version(self):
        """Gets the package_version of this RequiredSoftwarePolicyConfiguration.  # noqa: E501


        :return: The package_version of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """Sets the package_version of this RequiredSoftwarePolicyConfiguration.


        :param package_version: The package_version of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :type: str
        """
        if package_version is None:
            raise ValueError("Invalid value for `package_version`, must not be `None`")  # noqa: E501

        self._package_version = package_version

    @property
    def installation_code(self):
        """Gets the installation_code of this RequiredSoftwarePolicyConfiguration.  # noqa: E501


        :return: The installation_code of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._installation_code

    @installation_code.setter
    def installation_code(self, installation_code):
        """Sets the installation_code of this RequiredSoftwarePolicyConfiguration.


        :param installation_code: The installation_code of this RequiredSoftwarePolicyConfiguration.  # noqa: E501
        :type: str
        """
        if installation_code is None:
            raise ValueError("Invalid value for `installation_code`, must not be `None`")  # noqa: E501

        self._installation_code = installation_code

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
        if issubclass(RequiredSoftwarePolicyConfiguration, dict):
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
        if not isinstance(other, RequiredSoftwarePolicyConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
