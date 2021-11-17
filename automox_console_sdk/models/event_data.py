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

class EventData(object):
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
        'firstname': 'str',
        'lastname': 'str',
        'email': 'str',
        'orgname': 'str',
        'ip': 'str',
        'os': 'str',
        'systemname': 'str',
        'text': 'str',
        'status': 'int',
        'patches': 'str'
    }

    attribute_map = {
        'firstname': 'firstname',
        'lastname': 'lastname',
        'email': 'email',
        'orgname': 'orgname',
        'ip': 'ip',
        'os': 'os',
        'systemname': 'systemname',
        'text': 'text',
        'status': 'status',
        'patches': 'patches'
    }

    def __init__(self, firstname=None, lastname=None, email=None, orgname=None, ip=None, os=None, systemname=None, text=None, status=None, patches=None):  # noqa: E501
        """EventData - a model defined in Swagger"""  # noqa: E501
        self._firstname = None
        self._lastname = None
        self._email = None
        self._orgname = None
        self._ip = None
        self._os = None
        self._systemname = None
        self._text = None
        self._status = None
        self._patches = None
        self.discriminator = None
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if email is not None:
            self.email = email
        if orgname is not None:
            self.orgname = orgname
        if ip is not None:
            self.ip = ip
        if os is not None:
            self.os = os
        if systemname is not None:
            self.systemname = systemname
        if text is not None:
            self.text = text
        if status is not None:
            self.status = status
        if patches is not None:
            self.patches = patches

    @property
    def firstname(self):
        """Gets the firstname of this EventData.  # noqa: E501


        :return: The firstname of this EventData.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this EventData.


        :param firstname: The firstname of this EventData.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this EventData.  # noqa: E501


        :return: The lastname of this EventData.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this EventData.


        :param lastname: The lastname of this EventData.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """Gets the email of this EventData.  # noqa: E501


        :return: The email of this EventData.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EventData.


        :param email: The email of this EventData.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def orgname(self):
        """Gets the orgname of this EventData.  # noqa: E501


        :return: The orgname of this EventData.  # noqa: E501
        :rtype: str
        """
        return self._orgname

    @orgname.setter
    def orgname(self, orgname):
        """Sets the orgname of this EventData.


        :param orgname: The orgname of this EventData.  # noqa: E501
        :type: str
        """

        self._orgname = orgname

    @property
    def ip(self):
        """Gets the ip of this EventData.  # noqa: E501


        :return: The ip of this EventData.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this EventData.


        :param ip: The ip of this EventData.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def os(self):
        """Gets the os of this EventData.  # noqa: E501


        :return: The os of this EventData.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this EventData.


        :param os: The os of this EventData.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def systemname(self):
        """Gets the systemname of this EventData.  # noqa: E501


        :return: The systemname of this EventData.  # noqa: E501
        :rtype: str
        """
        return self._systemname

    @systemname.setter
    def systemname(self, systemname):
        """Sets the systemname of this EventData.


        :param systemname: The systemname of this EventData.  # noqa: E501
        :type: str
        """

        self._systemname = systemname

    @property
    def text(self):
        """Gets the text of this EventData.  # noqa: E501


        :return: The text of this EventData.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this EventData.


        :param text: The text of this EventData.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def status(self):
        """Gets the status of this EventData.  # noqa: E501


        :return: The status of this EventData.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EventData.


        :param status: The status of this EventData.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def patches(self):
        """Gets the patches of this EventData.  # noqa: E501


        :return: The patches of this EventData.  # noqa: E501
        :rtype: str
        """
        return self._patches

    @patches.setter
    def patches(self, patches):
        """Sets the patches of this EventData.


        :param patches: The patches of this EventData.  # noqa: E501
        :type: str
        """

        self._patches = patches

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
        if issubclass(EventData, dict):
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
        if not isinstance(other, EventData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
