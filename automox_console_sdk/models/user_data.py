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

class UserData(object):
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
        'email': 'str',
        'orgname': 'str',
        'lastname': 'str',
        'trialend': 'datetime',
        'firstname': 'str',
        'trialstart': 'datetime'
    }

    attribute_map = {
        'email': 'email',
        'orgname': 'orgname',
        'lastname': 'lastname',
        'trialend': 'trialend',
        'firstname': 'firstname',
        'trialstart': 'trialstart'
    }

    def __init__(self, email=None, orgname=None, lastname=None, trialend=None, firstname=None, trialstart=None):  # noqa: E501
        """UserData - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._orgname = None
        self._lastname = None
        self._trialend = None
        self._firstname = None
        self._trialstart = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if orgname is not None:
            self.orgname = orgname
        if lastname is not None:
            self.lastname = lastname
        if trialend is not None:
            self.trialend = trialend
        if firstname is not None:
            self.firstname = firstname
        if trialstart is not None:
            self.trialstart = trialstart

    @property
    def email(self):
        """Gets the email of this UserData.  # noqa: E501


        :return: The email of this UserData.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserData.


        :param email: The email of this UserData.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def orgname(self):
        """Gets the orgname of this UserData.  # noqa: E501


        :return: The orgname of this UserData.  # noqa: E501
        :rtype: str
        """
        return self._orgname

    @orgname.setter
    def orgname(self, orgname):
        """Sets the orgname of this UserData.


        :param orgname: The orgname of this UserData.  # noqa: E501
        :type: str
        """

        self._orgname = orgname

    @property
    def lastname(self):
        """Gets the lastname of this UserData.  # noqa: E501


        :return: The lastname of this UserData.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this UserData.


        :param lastname: The lastname of this UserData.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def trialend(self):
        """Gets the trialend of this UserData.  # noqa: E501


        :return: The trialend of this UserData.  # noqa: E501
        :rtype: datetime
        """
        return self._trialend

    @trialend.setter
    def trialend(self, trialend):
        """Sets the trialend of this UserData.


        :param trialend: The trialend of this UserData.  # noqa: E501
        :type: datetime
        """

        self._trialend = trialend

    @property
    def firstname(self):
        """Gets the firstname of this UserData.  # noqa: E501


        :return: The firstname of this UserData.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserData.


        :param firstname: The firstname of this UserData.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def trialstart(self):
        """Gets the trialstart of this UserData.  # noqa: E501


        :return: The trialstart of this UserData.  # noqa: E501
        :rtype: datetime
        """
        return self._trialstart

    @trialstart.setter
    def trialstart(self, trialstart):
        """Sets the trialstart of this UserData.


        :param trialstart: The trialstart of this UserData.  # noqa: E501
        :type: datetime
        """

        self._trialstart = trialstart

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
        if issubclass(UserData, dict):
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
        if not isinstance(other, UserData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
