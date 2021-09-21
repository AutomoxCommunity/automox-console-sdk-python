# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-09-20
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NotificationResponseData(object):
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
        'response': 'str',
        'notification_id': 'str'
    }

    attribute_map = {
        'response': 'response',
        'notification_id': 'notification_id'
    }

    def __init__(self, response=None, notification_id=None):  # noqa: E501
        """NotificationResponseData - a model defined in Swagger"""  # noqa: E501
        self._response = None
        self._notification_id = None
        self.discriminator = None
        if response is not None:
            self.response = response
        if notification_id is not None:
            self.notification_id = notification_id

    @property
    def response(self):
        """Gets the response of this NotificationResponseData.  # noqa: E501


        :return: The response of this NotificationResponseData.  # noqa: E501
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this NotificationResponseData.


        :param response: The response of this NotificationResponseData.  # noqa: E501
        :type: str
        """

        self._response = response

    @property
    def notification_id(self):
        """Gets the notification_id of this NotificationResponseData.  # noqa: E501


        :return: The notification_id of this NotificationResponseData.  # noqa: E501
        :rtype: str
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this NotificationResponseData.


        :param notification_id: The notification_id of this NotificationResponseData.  # noqa: E501
        :type: str
        """

        self._notification_id = notification_id

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
        if issubclass(NotificationResponseData, dict):
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
        if not isinstance(other, NotificationResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
