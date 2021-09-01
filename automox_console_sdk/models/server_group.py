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

class ServerGroup(object):
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
        'organization_id': 'int',
        'name': 'str',
        'refresh_interval': 'int',
        'parent_server_group_id': 'int',
        'ui_color': 'str',
        'notes': 'str',
        'enable_os_auto_update': 'bool',
        'server_count': 'int',
        'wsus_config': 'WsusConfig',
        'policies': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'organization_id': 'organization_id',
        'name': 'name',
        'refresh_interval': 'refresh_interval',
        'parent_server_group_id': 'parent_server_group_id',
        'ui_color': 'ui_color',
        'notes': 'notes',
        'enable_os_auto_update': 'enable_os_auto_update',
        'server_count': 'server_count',
        'wsus_config': 'wsus_config',
        'policies': 'policies'
    }

    def __init__(self, id=None, organization_id=None, name=None, refresh_interval=None, parent_server_group_id=None, ui_color=None, notes=None, enable_os_auto_update=None, server_count=None, wsus_config=None, policies=None):  # noqa: E501
        """ServerGroup - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._organization_id = None
        self._name = None
        self._refresh_interval = None
        self._parent_server_group_id = None
        self._ui_color = None
        self._notes = None
        self._enable_os_auto_update = None
        self._server_count = None
        self._wsus_config = None
        self._policies = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if organization_id is not None:
            self.organization_id = organization_id
        if name is not None:
            self.name = name
        if refresh_interval is not None:
            self.refresh_interval = refresh_interval
        if parent_server_group_id is not None:
            self.parent_server_group_id = parent_server_group_id
        if ui_color is not None:
            self.ui_color = ui_color
        if notes is not None:
            self.notes = notes
        if enable_os_auto_update is not None:
            self.enable_os_auto_update = enable_os_auto_update
        if server_count is not None:
            self.server_count = server_count
        if wsus_config is not None:
            self.wsus_config = wsus_config
        if policies is not None:
            self.policies = policies

    @property
    def id(self):
        """Gets the id of this ServerGroup.  # noqa: E501


        :return: The id of this ServerGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServerGroup.


        :param id: The id of this ServerGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def organization_id(self):
        """Gets the organization_id of this ServerGroup.  # noqa: E501


        :return: The organization_id of this ServerGroup.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ServerGroup.


        :param organization_id: The organization_id of this ServerGroup.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def name(self):
        """Gets the name of this ServerGroup.  # noqa: E501


        :return: The name of this ServerGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServerGroup.


        :param name: The name of this ServerGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def refresh_interval(self):
        """Gets the refresh_interval of this ServerGroup.  # noqa: E501


        :return: The refresh_interval of this ServerGroup.  # noqa: E501
        :rtype: int
        """
        return self._refresh_interval

    @refresh_interval.setter
    def refresh_interval(self, refresh_interval):
        """Sets the refresh_interval of this ServerGroup.


        :param refresh_interval: The refresh_interval of this ServerGroup.  # noqa: E501
        :type: int
        """

        self._refresh_interval = refresh_interval

    @property
    def parent_server_group_id(self):
        """Gets the parent_server_group_id of this ServerGroup.  # noqa: E501


        :return: The parent_server_group_id of this ServerGroup.  # noqa: E501
        :rtype: int
        """
        return self._parent_server_group_id

    @parent_server_group_id.setter
    def parent_server_group_id(self, parent_server_group_id):
        """Sets the parent_server_group_id of this ServerGroup.


        :param parent_server_group_id: The parent_server_group_id of this ServerGroup.  # noqa: E501
        :type: int
        """

        self._parent_server_group_id = parent_server_group_id

    @property
    def ui_color(self):
        """Gets the ui_color of this ServerGroup.  # noqa: E501


        :return: The ui_color of this ServerGroup.  # noqa: E501
        :rtype: str
        """
        return self._ui_color

    @ui_color.setter
    def ui_color(self, ui_color):
        """Sets the ui_color of this ServerGroup.


        :param ui_color: The ui_color of this ServerGroup.  # noqa: E501
        :type: str
        """

        self._ui_color = ui_color

    @property
    def notes(self):
        """Gets the notes of this ServerGroup.  # noqa: E501


        :return: The notes of this ServerGroup.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ServerGroup.


        :param notes: The notes of this ServerGroup.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def enable_os_auto_update(self):
        """Gets the enable_os_auto_update of this ServerGroup.  # noqa: E501


        :return: The enable_os_auto_update of this ServerGroup.  # noqa: E501
        :rtype: bool
        """
        return self._enable_os_auto_update

    @enable_os_auto_update.setter
    def enable_os_auto_update(self, enable_os_auto_update):
        """Sets the enable_os_auto_update of this ServerGroup.


        :param enable_os_auto_update: The enable_os_auto_update of this ServerGroup.  # noqa: E501
        :type: bool
        """

        self._enable_os_auto_update = enable_os_auto_update

    @property
    def server_count(self):
        """Gets the server_count of this ServerGroup.  # noqa: E501


        :return: The server_count of this ServerGroup.  # noqa: E501
        :rtype: int
        """
        return self._server_count

    @server_count.setter
    def server_count(self, server_count):
        """Sets the server_count of this ServerGroup.


        :param server_count: The server_count of this ServerGroup.  # noqa: E501
        :type: int
        """

        self._server_count = server_count

    @property
    def wsus_config(self):
        """Gets the wsus_config of this ServerGroup.  # noqa: E501


        :return: The wsus_config of this ServerGroup.  # noqa: E501
        :rtype: WsusConfig
        """
        return self._wsus_config

    @wsus_config.setter
    def wsus_config(self, wsus_config):
        """Sets the wsus_config of this ServerGroup.


        :param wsus_config: The wsus_config of this ServerGroup.  # noqa: E501
        :type: WsusConfig
        """

        self._wsus_config = wsus_config

    @property
    def policies(self):
        """Gets the policies of this ServerGroup.  # noqa: E501


        :return: The policies of this ServerGroup.  # noqa: E501
        :rtype: list[int]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this ServerGroup.


        :param policies: The policies of this ServerGroup.  # noqa: E501
        :type: list[int]
        """

        self._policies = policies

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
        if issubclass(ServerGroup, dict):
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
        if not isinstance(other, ServerGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
