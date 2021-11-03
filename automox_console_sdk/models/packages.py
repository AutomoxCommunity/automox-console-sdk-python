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

class Packages(object):
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
        'package_id': 'int',
        'software_id': 'int',
        'installed': 'bool',
        'ignored': 'bool',
        'deferred_until': 'datetime',
        'name': 'str',
        'display_name': 'str',
        'version': 'str',
        'repo': 'str',
        'group_ignored': 'bool',
        'group_deferred_until': 'datetime',
        'cves': 'list[str]',
        'cve_score': 'str',
        'severity': 'str',
        'package_version_id': 'int',
        'os_name': 'str',
        'os_version': 'str',
        'os_version_id': 'int',
        'create_time': 'datetime',
        'requires_reboot': 'bool',
        'patch_classification_category_id': 'int',
        'patch_scope': 'str',
        'is_uninstallable': 'bool',
        'secondary_id': 'str',
        'is_managed': 'bool',
        'impact': 'int',
        'organization_id': 'int',
        'agent_severity': 'str'
    }

    attribute_map = {
        'id': 'id',
        'server_id': 'server_id',
        'package_id': 'package_id',
        'software_id': 'software_id',
        'installed': 'installed',
        'ignored': 'ignored',
        'deferred_until': 'deferred_until',
        'name': 'name',
        'display_name': 'display_name',
        'version': 'version',
        'repo': 'repo',
        'group_ignored': 'group_ignored',
        'group_deferred_until': 'group_deferred_until',
        'cves': 'cves',
        'cve_score': 'cve_score',
        'severity': 'severity',
        'package_version_id': 'package_version_id',
        'os_name': 'os_name',
        'os_version': 'os_version',
        'os_version_id': 'os_version_id',
        'create_time': 'create_time',
        'requires_reboot': 'requires_reboot',
        'patch_classification_category_id': 'patch_classification_category_id',
        'patch_scope': 'patch_scope',
        'is_uninstallable': 'is_uninstallable',
        'secondary_id': 'secondary_id',
        'is_managed': 'is_managed',
        'impact': 'impact',
        'organization_id': 'organization_id',
        'agent_severity': 'agent_severity'
    }

    def __init__(self, id=None, server_id=None, package_id=None, software_id=None, installed=None, ignored=None, deferred_until=None, name=None, display_name=None, version=None, repo=None, group_ignored=None, group_deferred_until=None, cves=None, cve_score=None, severity=None, package_version_id=None, os_name=None, os_version=None, os_version_id=None, create_time=None, requires_reboot=None, patch_classification_category_id=None, patch_scope=None, is_uninstallable=None, secondary_id=None, is_managed=None, impact=None, organization_id=None, agent_severity=None):  # noqa: E501
        """Packages - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._server_id = None
        self._package_id = None
        self._software_id = None
        self._installed = None
        self._ignored = None
        self._deferred_until = None
        self._name = None
        self._display_name = None
        self._version = None
        self._repo = None
        self._group_ignored = None
        self._group_deferred_until = None
        self._cves = None
        self._cve_score = None
        self._severity = None
        self._package_version_id = None
        self._os_name = None
        self._os_version = None
        self._os_version_id = None
        self._create_time = None
        self._requires_reboot = None
        self._patch_classification_category_id = None
        self._patch_scope = None
        self._is_uninstallable = None
        self._secondary_id = None
        self._is_managed = None
        self._impact = None
        self._organization_id = None
        self._agent_severity = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if server_id is not None:
            self.server_id = server_id
        if package_id is not None:
            self.package_id = package_id
        if software_id is not None:
            self.software_id = software_id
        if installed is not None:
            self.installed = installed
        if ignored is not None:
            self.ignored = ignored
        if deferred_until is not None:
            self.deferred_until = deferred_until
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if version is not None:
            self.version = version
        if repo is not None:
            self.repo = repo
        if group_ignored is not None:
            self.group_ignored = group_ignored
        if group_deferred_until is not None:
            self.group_deferred_until = group_deferred_until
        if cves is not None:
            self.cves = cves
        if cve_score is not None:
            self.cve_score = cve_score
        if severity is not None:
            self.severity = severity
        if package_version_id is not None:
            self.package_version_id = package_version_id
        if os_name is not None:
            self.os_name = os_name
        if os_version is not None:
            self.os_version = os_version
        if os_version_id is not None:
            self.os_version_id = os_version_id
        if create_time is not None:
            self.create_time = create_time
        if requires_reboot is not None:
            self.requires_reboot = requires_reboot
        if patch_classification_category_id is not None:
            self.patch_classification_category_id = patch_classification_category_id
        if patch_scope is not None:
            self.patch_scope = patch_scope
        if is_uninstallable is not None:
            self.is_uninstallable = is_uninstallable
        if secondary_id is not None:
            self.secondary_id = secondary_id
        if is_managed is not None:
            self.is_managed = is_managed
        if impact is not None:
            self.impact = impact
        if organization_id is not None:
            self.organization_id = organization_id
        if agent_severity is not None:
            self.agent_severity = agent_severity

    @property
    def id(self):
        """Gets the id of this Packages.  # noqa: E501


        :return: The id of this Packages.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Packages.


        :param id: The id of this Packages.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def server_id(self):
        """Gets the server_id of this Packages.  # noqa: E501


        :return: The server_id of this Packages.  # noqa: E501
        :rtype: int
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this Packages.


        :param server_id: The server_id of this Packages.  # noqa: E501
        :type: int
        """

        self._server_id = server_id

    @property
    def package_id(self):
        """Gets the package_id of this Packages.  # noqa: E501


        :return: The package_id of this Packages.  # noqa: E501
        :rtype: int
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this Packages.


        :param package_id: The package_id of this Packages.  # noqa: E501
        :type: int
        """

        self._package_id = package_id

    @property
    def software_id(self):
        """Gets the software_id of this Packages.  # noqa: E501


        :return: The software_id of this Packages.  # noqa: E501
        :rtype: int
        """
        return self._software_id

    @software_id.setter
    def software_id(self, software_id):
        """Sets the software_id of this Packages.


        :param software_id: The software_id of this Packages.  # noqa: E501
        :type: int
        """

        self._software_id = software_id

    @property
    def installed(self):
        """Gets the installed of this Packages.  # noqa: E501


        :return: The installed of this Packages.  # noqa: E501
        :rtype: bool
        """
        return self._installed

    @installed.setter
    def installed(self, installed):
        """Sets the installed of this Packages.


        :param installed: The installed of this Packages.  # noqa: E501
        :type: bool
        """

        self._installed = installed

    @property
    def ignored(self):
        """Gets the ignored of this Packages.  # noqa: E501


        :return: The ignored of this Packages.  # noqa: E501
        :rtype: bool
        """
        return self._ignored

    @ignored.setter
    def ignored(self, ignored):
        """Sets the ignored of this Packages.


        :param ignored: The ignored of this Packages.  # noqa: E501
        :type: bool
        """

        self._ignored = ignored

    @property
    def deferred_until(self):
        """Gets the deferred_until of this Packages.  # noqa: E501


        :return: The deferred_until of this Packages.  # noqa: E501
        :rtype: datetime
        """
        return self._deferred_until

    @deferred_until.setter
    def deferred_until(self, deferred_until):
        """Sets the deferred_until of this Packages.


        :param deferred_until: The deferred_until of this Packages.  # noqa: E501
        :type: datetime
        """

        self._deferred_until = deferred_until

    @property
    def name(self):
        """Gets the name of this Packages.  # noqa: E501


        :return: The name of this Packages.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Packages.


        :param name: The name of this Packages.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this Packages.  # noqa: E501


        :return: The display_name of this Packages.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Packages.


        :param display_name: The display_name of this Packages.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def version(self):
        """Gets the version of this Packages.  # noqa: E501


        :return: The version of this Packages.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Packages.


        :param version: The version of this Packages.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def repo(self):
        """Gets the repo of this Packages.  # noqa: E501


        :return: The repo of this Packages.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this Packages.


        :param repo: The repo of this Packages.  # noqa: E501
        :type: str
        """

        self._repo = repo

    @property
    def group_ignored(self):
        """Gets the group_ignored of this Packages.  # noqa: E501


        :return: The group_ignored of this Packages.  # noqa: E501
        :rtype: bool
        """
        return self._group_ignored

    @group_ignored.setter
    def group_ignored(self, group_ignored):
        """Sets the group_ignored of this Packages.


        :param group_ignored: The group_ignored of this Packages.  # noqa: E501
        :type: bool
        """

        self._group_ignored = group_ignored

    @property
    def group_deferred_until(self):
        """Gets the group_deferred_until of this Packages.  # noqa: E501


        :return: The group_deferred_until of this Packages.  # noqa: E501
        :rtype: datetime
        """
        return self._group_deferred_until

    @group_deferred_until.setter
    def group_deferred_until(self, group_deferred_until):
        """Sets the group_deferred_until of this Packages.


        :param group_deferred_until: The group_deferred_until of this Packages.  # noqa: E501
        :type: datetime
        """

        self._group_deferred_until = group_deferred_until

    @property
    def cves(self):
        """Gets the cves of this Packages.  # noqa: E501


        :return: The cves of this Packages.  # noqa: E501
        :rtype: list[str]
        """
        return self._cves

    @cves.setter
    def cves(self, cves):
        """Sets the cves of this Packages.


        :param cves: The cves of this Packages.  # noqa: E501
        :type: list[str]
        """

        self._cves = cves

    @property
    def cve_score(self):
        """Gets the cve_score of this Packages.  # noqa: E501


        :return: The cve_score of this Packages.  # noqa: E501
        :rtype: str
        """
        return self._cve_score

    @cve_score.setter
    def cve_score(self, cve_score):
        """Sets the cve_score of this Packages.


        :param cve_score: The cve_score of this Packages.  # noqa: E501
        :type: str
        """

        self._cve_score = cve_score

    @property
    def severity(self):
        """Gets the severity of this Packages.  # noqa: E501


        :return: The severity of this Packages.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Packages.


        :param severity: The severity of this Packages.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def package_version_id(self):
        """Gets the package_version_id of this Packages.  # noqa: E501


        :return: The package_version_id of this Packages.  # noqa: E501
        :rtype: int
        """
        return self._package_version_id

    @package_version_id.setter
    def package_version_id(self, package_version_id):
        """Sets the package_version_id of this Packages.


        :param package_version_id: The package_version_id of this Packages.  # noqa: E501
        :type: int
        """

        self._package_version_id = package_version_id

    @property
    def os_name(self):
        """Gets the os_name of this Packages.  # noqa: E501


        :return: The os_name of this Packages.  # noqa: E501
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this Packages.


        :param os_name: The os_name of this Packages.  # noqa: E501
        :type: str
        """

        self._os_name = os_name

    @property
    def os_version(self):
        """Gets the os_version of this Packages.  # noqa: E501


        :return: The os_version of this Packages.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this Packages.


        :param os_version: The os_version of this Packages.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

    @property
    def os_version_id(self):
        """Gets the os_version_id of this Packages.  # noqa: E501


        :return: The os_version_id of this Packages.  # noqa: E501
        :rtype: int
        """
        return self._os_version_id

    @os_version_id.setter
    def os_version_id(self, os_version_id):
        """Sets the os_version_id of this Packages.


        :param os_version_id: The os_version_id of this Packages.  # noqa: E501
        :type: int
        """

        self._os_version_id = os_version_id

    @property
    def create_time(self):
        """Gets the create_time of this Packages.  # noqa: E501


        :return: The create_time of this Packages.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Packages.


        :param create_time: The create_time of this Packages.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def requires_reboot(self):
        """Gets the requires_reboot of this Packages.  # noqa: E501


        :return: The requires_reboot of this Packages.  # noqa: E501
        :rtype: bool
        """
        return self._requires_reboot

    @requires_reboot.setter
    def requires_reboot(self, requires_reboot):
        """Sets the requires_reboot of this Packages.


        :param requires_reboot: The requires_reboot of this Packages.  # noqa: E501
        :type: bool
        """

        self._requires_reboot = requires_reboot

    @property
    def patch_classification_category_id(self):
        """Gets the patch_classification_category_id of this Packages.  # noqa: E501


        :return: The patch_classification_category_id of this Packages.  # noqa: E501
        :rtype: int
        """
        return self._patch_classification_category_id

    @patch_classification_category_id.setter
    def patch_classification_category_id(self, patch_classification_category_id):
        """Sets the patch_classification_category_id of this Packages.


        :param patch_classification_category_id: The patch_classification_category_id of this Packages.  # noqa: E501
        :type: int
        """

        self._patch_classification_category_id = patch_classification_category_id

    @property
    def patch_scope(self):
        """Gets the patch_scope of this Packages.  # noqa: E501


        :return: The patch_scope of this Packages.  # noqa: E501
        :rtype: str
        """
        return self._patch_scope

    @patch_scope.setter
    def patch_scope(self, patch_scope):
        """Sets the patch_scope of this Packages.


        :param patch_scope: The patch_scope of this Packages.  # noqa: E501
        :type: str
        """

        self._patch_scope = patch_scope

    @property
    def is_uninstallable(self):
        """Gets the is_uninstallable of this Packages.  # noqa: E501


        :return: The is_uninstallable of this Packages.  # noqa: E501
        :rtype: bool
        """
        return self._is_uninstallable

    @is_uninstallable.setter
    def is_uninstallable(self, is_uninstallable):
        """Sets the is_uninstallable of this Packages.


        :param is_uninstallable: The is_uninstallable of this Packages.  # noqa: E501
        :type: bool
        """

        self._is_uninstallable = is_uninstallable

    @property
    def secondary_id(self):
        """Gets the secondary_id of this Packages.  # noqa: E501


        :return: The secondary_id of this Packages.  # noqa: E501
        :rtype: str
        """
        return self._secondary_id

    @secondary_id.setter
    def secondary_id(self, secondary_id):
        """Sets the secondary_id of this Packages.


        :param secondary_id: The secondary_id of this Packages.  # noqa: E501
        :type: str
        """

        self._secondary_id = secondary_id

    @property
    def is_managed(self):
        """Gets the is_managed of this Packages.  # noqa: E501


        :return: The is_managed of this Packages.  # noqa: E501
        :rtype: bool
        """
        return self._is_managed

    @is_managed.setter
    def is_managed(self, is_managed):
        """Sets the is_managed of this Packages.


        :param is_managed: The is_managed of this Packages.  # noqa: E501
        :type: bool
        """

        self._is_managed = is_managed

    @property
    def impact(self):
        """Gets the impact of this Packages.  # noqa: E501


        :return: The impact of this Packages.  # noqa: E501
        :rtype: int
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """Sets the impact of this Packages.


        :param impact: The impact of this Packages.  # noqa: E501
        :type: int
        """

        self._impact = impact

    @property
    def organization_id(self):
        """Gets the organization_id of this Packages.  # noqa: E501


        :return: The organization_id of this Packages.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Packages.


        :param organization_id: The organization_id of this Packages.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def agent_severity(self):
        """Gets the agent_severity of this Packages.  # noqa: E501


        :return: The agent_severity of this Packages.  # noqa: E501
        :rtype: str
        """
        return self._agent_severity

    @agent_severity.setter
    def agent_severity(self, agent_severity):
        """Sets the agent_severity of this Packages.


        :param agent_severity: The agent_severity of this Packages.  # noqa: E501
        :type: str
        """

        self._agent_severity = agent_severity

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
        if issubclass(Packages, dict):
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
        if not isinstance(other, Packages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
