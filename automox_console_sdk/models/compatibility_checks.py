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

class CompatibilityChecks(object):
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
        'low_diskspace': 'bool',
        'missing_secure_token': 'bool',
        'app_store_disconnected': 'bool',
        'missing_powershell': 'bool',
        'missing_wmi_integrity_check': 'bool',
        'wsus_disconnected': 'bool',
        'windows_update_server_disconnected': 'bool'
    }

    attribute_map = {
        'low_diskspace': 'low_diskspace',
        'missing_secure_token': 'missing_secure_token',
        'app_store_disconnected': 'app_store_disconnected',
        'missing_powershell': 'missing_powershell',
        'missing_wmi_integrity_check': 'missing_wmi_integrity_check',
        'wsus_disconnected': 'wsus_disconnected',
        'windows_update_server_disconnected': 'windows_update_server_disconnected'
    }

    def __init__(self, low_diskspace=None, missing_secure_token=None, app_store_disconnected=None, missing_powershell=None, missing_wmi_integrity_check=None, wsus_disconnected=None, windows_update_server_disconnected=None):  # noqa: E501
        """CompatibilityChecks - a model defined in Swagger"""  # noqa: E501
        self._low_diskspace = None
        self._missing_secure_token = None
        self._app_store_disconnected = None
        self._missing_powershell = None
        self._missing_wmi_integrity_check = None
        self._wsus_disconnected = None
        self._windows_update_server_disconnected = None
        self.discriminator = None
        if low_diskspace is not None:
            self.low_diskspace = low_diskspace
        if missing_secure_token is not None:
            self.missing_secure_token = missing_secure_token
        if app_store_disconnected is not None:
            self.app_store_disconnected = app_store_disconnected
        if missing_powershell is not None:
            self.missing_powershell = missing_powershell
        if missing_wmi_integrity_check is not None:
            self.missing_wmi_integrity_check = missing_wmi_integrity_check
        if wsus_disconnected is not None:
            self.wsus_disconnected = wsus_disconnected
        if windows_update_server_disconnected is not None:
            self.windows_update_server_disconnected = windows_update_server_disconnected

    @property
    def low_diskspace(self):
        """Gets the low_diskspace of this CompatibilityChecks.  # noqa: E501


        :return: The low_diskspace of this CompatibilityChecks.  # noqa: E501
        :rtype: bool
        """
        return self._low_diskspace

    @low_diskspace.setter
    def low_diskspace(self, low_diskspace):
        """Sets the low_diskspace of this CompatibilityChecks.


        :param low_diskspace: The low_diskspace of this CompatibilityChecks.  # noqa: E501
        :type: bool
        """

        self._low_diskspace = low_diskspace

    @property
    def missing_secure_token(self):
        """Gets the missing_secure_token of this CompatibilityChecks.  # noqa: E501


        :return: The missing_secure_token of this CompatibilityChecks.  # noqa: E501
        :rtype: bool
        """
        return self._missing_secure_token

    @missing_secure_token.setter
    def missing_secure_token(self, missing_secure_token):
        """Sets the missing_secure_token of this CompatibilityChecks.


        :param missing_secure_token: The missing_secure_token of this CompatibilityChecks.  # noqa: E501
        :type: bool
        """

        self._missing_secure_token = missing_secure_token

    @property
    def app_store_disconnected(self):
        """Gets the app_store_disconnected of this CompatibilityChecks.  # noqa: E501


        :return: The app_store_disconnected of this CompatibilityChecks.  # noqa: E501
        :rtype: bool
        """
        return self._app_store_disconnected

    @app_store_disconnected.setter
    def app_store_disconnected(self, app_store_disconnected):
        """Sets the app_store_disconnected of this CompatibilityChecks.


        :param app_store_disconnected: The app_store_disconnected of this CompatibilityChecks.  # noqa: E501
        :type: bool
        """

        self._app_store_disconnected = app_store_disconnected

    @property
    def missing_powershell(self):
        """Gets the missing_powershell of this CompatibilityChecks.  # noqa: E501


        :return: The missing_powershell of this CompatibilityChecks.  # noqa: E501
        :rtype: bool
        """
        return self._missing_powershell

    @missing_powershell.setter
    def missing_powershell(self, missing_powershell):
        """Sets the missing_powershell of this CompatibilityChecks.


        :param missing_powershell: The missing_powershell of this CompatibilityChecks.  # noqa: E501
        :type: bool
        """

        self._missing_powershell = missing_powershell

    @property
    def missing_wmi_integrity_check(self):
        """Gets the missing_wmi_integrity_check of this CompatibilityChecks.  # noqa: E501


        :return: The missing_wmi_integrity_check of this CompatibilityChecks.  # noqa: E501
        :rtype: bool
        """
        return self._missing_wmi_integrity_check

    @missing_wmi_integrity_check.setter
    def missing_wmi_integrity_check(self, missing_wmi_integrity_check):
        """Sets the missing_wmi_integrity_check of this CompatibilityChecks.


        :param missing_wmi_integrity_check: The missing_wmi_integrity_check of this CompatibilityChecks.  # noqa: E501
        :type: bool
        """

        self._missing_wmi_integrity_check = missing_wmi_integrity_check

    @property
    def wsus_disconnected(self):
        """Gets the wsus_disconnected of this CompatibilityChecks.  # noqa: E501


        :return: The wsus_disconnected of this CompatibilityChecks.  # noqa: E501
        :rtype: bool
        """
        return self._wsus_disconnected

    @wsus_disconnected.setter
    def wsus_disconnected(self, wsus_disconnected):
        """Sets the wsus_disconnected of this CompatibilityChecks.


        :param wsus_disconnected: The wsus_disconnected of this CompatibilityChecks.  # noqa: E501
        :type: bool
        """

        self._wsus_disconnected = wsus_disconnected

    @property
    def windows_update_server_disconnected(self):
        """Gets the windows_update_server_disconnected of this CompatibilityChecks.  # noqa: E501


        :return: The windows_update_server_disconnected of this CompatibilityChecks.  # noqa: E501
        :rtype: bool
        """
        return self._windows_update_server_disconnected

    @windows_update_server_disconnected.setter
    def windows_update_server_disconnected(self, windows_update_server_disconnected):
        """Sets the windows_update_server_disconnected of this CompatibilityChecks.


        :param windows_update_server_disconnected: The windows_update_server_disconnected of this CompatibilityChecks.  # noqa: E501
        :type: bool
        """

        self._windows_update_server_disconnected = windows_update_server_disconnected

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
        if issubclass(CompatibilityChecks, dict):
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
        if not isinstance(other, CompatibilityChecks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
