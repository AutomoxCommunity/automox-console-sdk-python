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

class UserOrgs(object):
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
        'access_key': 'str',
        'trial_end_time': 'datetime',
        'trial_expired': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'access_key': 'access_key',
        'trial_end_time': 'trial_end_time',
        'trial_expired': 'trial_expired'
    }

    def __init__(self, id=None, name=None, access_key=None, trial_end_time=None, trial_expired=None):  # noqa: E501
        """UserOrgs - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._access_key = None
        self._trial_end_time = None
        self._trial_expired = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if access_key is not None:
            self.access_key = access_key
        if trial_end_time is not None:
            self.trial_end_time = trial_end_time
        if trial_expired is not None:
            self.trial_expired = trial_expired

    @property
    def id(self):
        """Gets the id of this UserOrgs.  # noqa: E501


        :return: The id of this UserOrgs.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserOrgs.


        :param id: The id of this UserOrgs.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UserOrgs.  # noqa: E501


        :return: The name of this UserOrgs.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserOrgs.


        :param name: The name of this UserOrgs.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def access_key(self):
        """Gets the access_key of this UserOrgs.  # noqa: E501


        :return: The access_key of this UserOrgs.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this UserOrgs.


        :param access_key: The access_key of this UserOrgs.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def trial_end_time(self):
        """Gets the trial_end_time of this UserOrgs.  # noqa: E501


        :return: The trial_end_time of this UserOrgs.  # noqa: E501
        :rtype: datetime
        """
        return self._trial_end_time

    @trial_end_time.setter
    def trial_end_time(self, trial_end_time):
        """Sets the trial_end_time of this UserOrgs.


        :param trial_end_time: The trial_end_time of this UserOrgs.  # noqa: E501
        :type: datetime
        """

        self._trial_end_time = trial_end_time

    @property
    def trial_expired(self):
        """Gets the trial_expired of this UserOrgs.  # noqa: E501


        :return: The trial_expired of this UserOrgs.  # noqa: E501
        :rtype: bool
        """
        return self._trial_expired

    @trial_expired.setter
    def trial_expired(self, trial_expired):
        """Sets the trial_expired of this UserOrgs.


        :param trial_expired: The trial_expired of this UserOrgs.  # noqa: E501
        :type: bool
        """

        self._trial_expired = trial_expired

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
        if issubclass(UserOrgs, dict):
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
        if not isinstance(other, UserOrgs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
