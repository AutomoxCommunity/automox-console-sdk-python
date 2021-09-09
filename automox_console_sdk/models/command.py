# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-09-01
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Command(object):
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
        'server_id': 'int',
        'policy_id': 'int',
        'command_id': 'int',
        'command_type_name': 'str',
        'args': 'str',
        'response': 'str',
        'response_time': 'datetime',
        'create_time': 'datetime',
        'exec_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'server_id': 'server_id',
        'policy_id': 'policy_id',
        'command_id': 'command_id',
        'command_type_name': 'command_type_name',
        'args': 'args',
        'response': 'response',
        'response_time': 'response_time',
        'create_time': 'create_time',
        'exec_time': 'exec_time'
    }

    def __init__(self, id=None, server_id=None, policy_id=None, command_id=None, command_type_name=None, args=None, response=None, response_time=None, create_time=None, exec_time=None):  # noqa: E501
        """Command - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._server_id = None
        self._policy_id = None
        self._command_id = None
        self._command_type_name = None
        self._args = None
        self._response = None
        self._response_time = None
        self._create_time = None
        self._exec_time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if server_id is not None:
            self.server_id = server_id
        if policy_id is not None:
            self.policy_id = policy_id
        if command_id is not None:
            self.command_id = command_id
        self.command_type_name = command_type_name
        self.args = args
        if response is not None:
            self.response = response
        if response_time is not None:
            self.response_time = response_time
        if create_time is not None:
            self.create_time = create_time
        self.exec_time = exec_time

    @property
    def id(self):
        """Gets the id of this Command.  # noqa: E501


        :return: The id of this Command.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Command.


        :param id: The id of this Command.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def server_id(self):
        """Gets the server_id of this Command.  # noqa: E501


        :return: The server_id of this Command.  # noqa: E501
        :rtype: int
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this Command.


        :param server_id: The server_id of this Command.  # noqa: E501
        :type: int
        """

        self._server_id = server_id

    @property
    def policy_id(self):
        """Gets the policy_id of this Command.  # noqa: E501


        :return: The policy_id of this Command.  # noqa: E501
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this Command.


        :param policy_id: The policy_id of this Command.  # noqa: E501
        :type: int
        """

        self._policy_id = policy_id

    @property
    def command_id(self):
        """Gets the command_id of this Command.  # noqa: E501


        :return: The command_id of this Command.  # noqa: E501
        :rtype: int
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this Command.


        :param command_id: The command_id of this Command.  # noqa: E501
        :type: int
        """

        self._command_id = command_id

    @property
    def command_type_name(self):
        """Gets the command_type_name of this Command.  # noqa: E501

        Type of command being issued  # noqa: E501

        :return: The command_type_name of this Command.  # noqa: E501
        :rtype: str
        """
        return self._command_type_name

    @command_type_name.setter
    def command_type_name(self, command_type_name):
        """Sets the command_type_name of this Command.

        Type of command being issued  # noqa: E501

        :param command_type_name: The command_type_name of this Command.  # noqa: E501
        :type: str
        """
        if command_type_name is None:
            raise ValueError("Invalid value for `command_type_name`, must not be `None`")  # noqa: E501
        allowed_values = ["InstallUpdate", "Reboot"]  # noqa: E501
        if command_type_name not in allowed_values:
            raise ValueError(
                "Invalid value for `command_type_name` ({0}), must be one of {1}"  # noqa: E501
                .format(command_type_name, allowed_values)
            )

        self._command_type_name = command_type_name

    @property
    def args(self):
        """Gets the args of this Command.  # noqa: E501

        List of patches to apply, or NULL if issuing a Reboot  # noqa: E501

        :return: The args of this Command.  # noqa: E501
        :rtype: str
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this Command.

        List of patches to apply, or NULL if issuing a Reboot  # noqa: E501

        :param args: The args of this Command.  # noqa: E501
        :type: str
        """
        if args is None:
            raise ValueError("Invalid value for `args`, must not be `None`")  # noqa: E501

        self._args = args

    @property
    def response(self):
        """Gets the response of this Command.  # noqa: E501


        :return: The response of this Command.  # noqa: E501
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this Command.


        :param response: The response of this Command.  # noqa: E501
        :type: str
        """

        self._response = response

    @property
    def response_time(self):
        """Gets the response_time of this Command.  # noqa: E501


        :return: The response_time of this Command.  # noqa: E501
        :rtype: datetime
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """Sets the response_time of this Command.


        :param response_time: The response_time of this Command.  # noqa: E501
        :type: datetime
        """

        self._response_time = response_time

    @property
    def create_time(self):
        """Gets the create_time of this Command.  # noqa: E501


        :return: The create_time of this Command.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Command.


        :param create_time: The create_time of this Command.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def exec_time(self):
        """Gets the exec_time of this Command.  # noqa: E501

        Time to execute the command, or NULL if issuing a Reboot  # noqa: E501

        :return: The exec_time of this Command.  # noqa: E501
        :rtype: datetime
        """
        return self._exec_time

    @exec_time.setter
    def exec_time(self, exec_time):
        """Sets the exec_time of this Command.

        Time to execute the command, or NULL if issuing a Reboot  # noqa: E501

        :param exec_time: The exec_time of this Command.  # noqa: E501
        :type: datetime
        """
        if exec_time is None:
            raise ValueError("Invalid value for `exec_time`, must not be `None`")  # noqa: E501

        self._exec_time = exec_time

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
        if issubclass(Command, dict):
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
        if not isinstance(other, Command):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
