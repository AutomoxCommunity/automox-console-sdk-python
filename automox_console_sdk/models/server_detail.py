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

class ServerDetail(object):
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
        'cpu': 'str',
        'disks': 'list[ServerDetailDISKS]',
        'model': 'str',
        'nics': 'list[ServerDetailNICS]',
        'ram': 'str',
        'serial': 'str',
        'servicetag': 'str',
        'vendor': 'str',
        'version': 'str'
    }

    attribute_map = {
        'cpu': 'CPU',
        'disks': 'DISKS',
        'model': 'MODEL',
        'nics': 'NICS',
        'ram': 'RAM',
        'serial': 'SERIAL',
        'servicetag': 'SERVICETAG',
        'vendor': 'VENDOR',
        'version': 'VERSION'
    }

    def __init__(self, cpu=None, disks=None, model=None, nics=None, ram=None, serial=None, servicetag=None, vendor=None, version=None):  # noqa: E501
        """ServerDetail - a model defined in Swagger"""  # noqa: E501
        self._cpu = None
        self._disks = None
        self._model = None
        self._nics = None
        self._ram = None
        self._serial = None
        self._servicetag = None
        self._vendor = None
        self._version = None
        self.discriminator = None
        if cpu is not None:
            self.cpu = cpu
        if disks is not None:
            self.disks = disks
        if model is not None:
            self.model = model
        if nics is not None:
            self.nics = nics
        if ram is not None:
            self.ram = ram
        if serial is not None:
            self.serial = serial
        if servicetag is not None:
            self.servicetag = servicetag
        if vendor is not None:
            self.vendor = vendor
        if version is not None:
            self.version = version

    @property
    def cpu(self):
        """Gets the cpu of this ServerDetail.  # noqa: E501


        :return: The cpu of this ServerDetail.  # noqa: E501
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ServerDetail.


        :param cpu: The cpu of this ServerDetail.  # noqa: E501
        :type: str
        """

        self._cpu = cpu

    @property
    def disks(self):
        """Gets the disks of this ServerDetail.  # noqa: E501


        :return: The disks of this ServerDetail.  # noqa: E501
        :rtype: list[ServerDetailDISKS]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this ServerDetail.


        :param disks: The disks of this ServerDetail.  # noqa: E501
        :type: list[ServerDetailDISKS]
        """

        self._disks = disks

    @property
    def model(self):
        """Gets the model of this ServerDetail.  # noqa: E501


        :return: The model of this ServerDetail.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ServerDetail.


        :param model: The model of this ServerDetail.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def nics(self):
        """Gets the nics of this ServerDetail.  # noqa: E501


        :return: The nics of this ServerDetail.  # noqa: E501
        :rtype: list[ServerDetailNICS]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this ServerDetail.


        :param nics: The nics of this ServerDetail.  # noqa: E501
        :type: list[ServerDetailNICS]
        """

        self._nics = nics

    @property
    def ram(self):
        """Gets the ram of this ServerDetail.  # noqa: E501


        :return: The ram of this ServerDetail.  # noqa: E501
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this ServerDetail.


        :param ram: The ram of this ServerDetail.  # noqa: E501
        :type: str
        """

        self._ram = ram

    @property
    def serial(self):
        """Gets the serial of this ServerDetail.  # noqa: E501


        :return: The serial of this ServerDetail.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this ServerDetail.


        :param serial: The serial of this ServerDetail.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def servicetag(self):
        """Gets the servicetag of this ServerDetail.  # noqa: E501


        :return: The servicetag of this ServerDetail.  # noqa: E501
        :rtype: str
        """
        return self._servicetag

    @servicetag.setter
    def servicetag(self, servicetag):
        """Sets the servicetag of this ServerDetail.


        :param servicetag: The servicetag of this ServerDetail.  # noqa: E501
        :type: str
        """

        self._servicetag = servicetag

    @property
    def vendor(self):
        """Gets the vendor of this ServerDetail.  # noqa: E501


        :return: The vendor of this ServerDetail.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this ServerDetail.


        :param vendor: The vendor of this ServerDetail.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def version(self):
        """Gets the version of this ServerDetail.  # noqa: E501


        :return: The version of this ServerDetail.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ServerDetail.


        :param version: The version of this ServerDetail.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(ServerDetail, dict):
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
        if not isinstance(other, ServerDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
