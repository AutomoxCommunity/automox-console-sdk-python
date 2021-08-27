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

class NotificationSentData(object):
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
        'scheduled_time': 'datetime',
        'notification_id': 'str',
        'last_process_time': 'datetime'
    }

    attribute_map = {
        'scheduled_time': 'scheduled_time',
        'notification_id': 'notification_id',
        'last_process_time': 'last_process_time'
    }

    def __init__(self, scheduled_time=None, notification_id=None, last_process_time=None):  # noqa: E501
        """NotificationSentData - a model defined in Swagger"""  # noqa: E501
        self._scheduled_time = None
        self._notification_id = None
        self._last_process_time = None
        self.discriminator = None
        if scheduled_time is not None:
            self.scheduled_time = scheduled_time
        if notification_id is not None:
            self.notification_id = notification_id
        if last_process_time is not None:
            self.last_process_time = last_process_time

    @property
    def scheduled_time(self):
        """Gets the scheduled_time of this NotificationSentData.  # noqa: E501


        :return: The scheduled_time of this NotificationSentData.  # noqa: E501
        :rtype: datetime
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        """Sets the scheduled_time of this NotificationSentData.


        :param scheduled_time: The scheduled_time of this NotificationSentData.  # noqa: E501
        :type: datetime
        """

        self._scheduled_time = scheduled_time

    @property
    def notification_id(self):
        """Gets the notification_id of this NotificationSentData.  # noqa: E501


        :return: The notification_id of this NotificationSentData.  # noqa: E501
        :rtype: str
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this NotificationSentData.


        :param notification_id: The notification_id of this NotificationSentData.  # noqa: E501
        :type: str
        """

        self._notification_id = notification_id

    @property
    def last_process_time(self):
        """Gets the last_process_time of this NotificationSentData.  # noqa: E501


        :return: The last_process_time of this NotificationSentData.  # noqa: E501
        :rtype: datetime
        """
        return self._last_process_time

    @last_process_time.setter
    def last_process_time(self, last_process_time):
        """Sets the last_process_time of this NotificationSentData.


        :param last_process_time: The last_process_time of this NotificationSentData.  # noqa: E501
        :type: datetime
        """

        self._last_process_time = last_process_time

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
        if issubclass(NotificationSentData, dict):
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
        if not isinstance(other, NotificationSentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
