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

class Organization(object):
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
        'addr1': 'str',
        'addr2': 'str',
        'city': 'str',
        'state': 'str',
        'zipcode': 'str',
        'country': 'str',
        'create_time': 'datetime',
        'access_key': 'str',
        'server_limit': 'int',
        'stripe_cust': 'str',
        'cc_last': 'str',
        'cc_exp': 'str',
        'cc_brand': 'str',
        'cc_name': 'str',
        'billing_interval': 'int',
        'billing_interval_count': 'int',
        'trial_end_time': 'datetime',
        'trial_expired': 'bool',
        'sub_plan': 'str',
        'sub_systems': 'str',
        'sub_create_time': 'str',
        'sub_end_time': 'str',
        'next_bill_time': 'str',
        'rate_id': 'int',
        'parent_id': 'int',
        'bill_overages': 'bool',
        'metadata': 'object',
        'legacy_billing': 'bool',
        'billing_name': 'str',
        'billing_email': 'str',
        'billing_phone': 'str',
        'device_limit': 'float',
        'device_count': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'addr1': 'addr1',
        'addr2': 'addr2',
        'city': 'city',
        'state': 'state',
        'zipcode': 'zipcode',
        'country': 'country',
        'create_time': 'create_time',
        'access_key': 'access_key',
        'server_limit': 'server_limit',
        'stripe_cust': 'stripe_cust',
        'cc_last': 'cc_last',
        'cc_exp': 'cc_exp',
        'cc_brand': 'cc_brand',
        'cc_name': 'cc_name',
        'billing_interval': 'billing_interval',
        'billing_interval_count': 'billing_interval_count',
        'trial_end_time': 'trial_end_time',
        'trial_expired': 'trial_expired',
        'sub_plan': 'sub_plan',
        'sub_systems': 'sub_systems',
        'sub_create_time': 'sub_create_time',
        'sub_end_time': 'sub_end_time',
        'next_bill_time': 'next_bill_time',
        'rate_id': 'rate_id',
        'parent_id': 'parent_id',
        'bill_overages': 'bill_overages',
        'metadata': 'metadata',
        'legacy_billing': 'legacy_billing',
        'billing_name': 'billing_name',
        'billing_email': 'billing_email',
        'billing_phone': 'billing_phone',
        'device_limit': 'device_limit',
        'device_count': 'device_count'
    }

    def __init__(self, id=None, name=None, addr1=None, addr2=None, city=None, state=None, zipcode=None, country=None, create_time=None, access_key=None, server_limit=None, stripe_cust=None, cc_last=None, cc_exp=None, cc_brand=None, cc_name=None, billing_interval=None, billing_interval_count=None, trial_end_time=None, trial_expired=None, sub_plan=None, sub_systems=None, sub_create_time=None, sub_end_time=None, next_bill_time=None, rate_id=None, parent_id=None, bill_overages=None, metadata=None, legacy_billing=None, billing_name=None, billing_email=None, billing_phone=None, device_limit=None, device_count=None):  # noqa: E501
        """Organization - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._addr1 = None
        self._addr2 = None
        self._city = None
        self._state = None
        self._zipcode = None
        self._country = None
        self._create_time = None
        self._access_key = None
        self._server_limit = None
        self._stripe_cust = None
        self._cc_last = None
        self._cc_exp = None
        self._cc_brand = None
        self._cc_name = None
        self._billing_interval = None
        self._billing_interval_count = None
        self._trial_end_time = None
        self._trial_expired = None
        self._sub_plan = None
        self._sub_systems = None
        self._sub_create_time = None
        self._sub_end_time = None
        self._next_bill_time = None
        self._rate_id = None
        self._parent_id = None
        self._bill_overages = None
        self._metadata = None
        self._legacy_billing = None
        self._billing_name = None
        self._billing_email = None
        self._billing_phone = None
        self._device_limit = None
        self._device_count = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if addr1 is not None:
            self.addr1 = addr1
        if addr2 is not None:
            self.addr2 = addr2
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if zipcode is not None:
            self.zipcode = zipcode
        if country is not None:
            self.country = country
        if create_time is not None:
            self.create_time = create_time
        if access_key is not None:
            self.access_key = access_key
        if server_limit is not None:
            self.server_limit = server_limit
        if stripe_cust is not None:
            self.stripe_cust = stripe_cust
        if cc_last is not None:
            self.cc_last = cc_last
        if cc_exp is not None:
            self.cc_exp = cc_exp
        if cc_brand is not None:
            self.cc_brand = cc_brand
        if cc_name is not None:
            self.cc_name = cc_name
        if billing_interval is not None:
            self.billing_interval = billing_interval
        if billing_interval_count is not None:
            self.billing_interval_count = billing_interval_count
        if trial_end_time is not None:
            self.trial_end_time = trial_end_time
        if trial_expired is not None:
            self.trial_expired = trial_expired
        if sub_plan is not None:
            self.sub_plan = sub_plan
        if sub_systems is not None:
            self.sub_systems = sub_systems
        if sub_create_time is not None:
            self.sub_create_time = sub_create_time
        if sub_end_time is not None:
            self.sub_end_time = sub_end_time
        if next_bill_time is not None:
            self.next_bill_time = next_bill_time
        if rate_id is not None:
            self.rate_id = rate_id
        if parent_id is not None:
            self.parent_id = parent_id
        if bill_overages is not None:
            self.bill_overages = bill_overages
        if metadata is not None:
            self.metadata = metadata
        if legacy_billing is not None:
            self.legacy_billing = legacy_billing
        if billing_name is not None:
            self.billing_name = billing_name
        if billing_email is not None:
            self.billing_email = billing_email
        if billing_phone is not None:
            self.billing_phone = billing_phone
        if device_limit is not None:
            self.device_limit = device_limit
        if device_count is not None:
            self.device_count = device_count

    @property
    def id(self):
        """Gets the id of this Organization.  # noqa: E501


        :return: The id of this Organization.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.


        :param id: The id of this Organization.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Organization.  # noqa: E501


        :return: The name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organization.


        :param name: The name of this Organization.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def addr1(self):
        """Gets the addr1 of this Organization.  # noqa: E501


        :return: The addr1 of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._addr1

    @addr1.setter
    def addr1(self, addr1):
        """Sets the addr1 of this Organization.


        :param addr1: The addr1 of this Organization.  # noqa: E501
        :type: str
        """

        self._addr1 = addr1

    @property
    def addr2(self):
        """Gets the addr2 of this Organization.  # noqa: E501


        :return: The addr2 of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._addr2

    @addr2.setter
    def addr2(self, addr2):
        """Sets the addr2 of this Organization.


        :param addr2: The addr2 of this Organization.  # noqa: E501
        :type: str
        """

        self._addr2 = addr2

    @property
    def city(self):
        """Gets the city of this Organization.  # noqa: E501


        :return: The city of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Organization.


        :param city: The city of this Organization.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this Organization.  # noqa: E501


        :return: The state of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Organization.


        :param state: The state of this Organization.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zipcode(self):
        """Gets the zipcode of this Organization.  # noqa: E501


        :return: The zipcode of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this Organization.


        :param zipcode: The zipcode of this Organization.  # noqa: E501
        :type: str
        """

        self._zipcode = zipcode

    @property
    def country(self):
        """Gets the country of this Organization.  # noqa: E501


        :return: The country of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Organization.


        :param country: The country of this Organization.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def create_time(self):
        """Gets the create_time of this Organization.  # noqa: E501


        :return: The create_time of this Organization.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Organization.


        :param create_time: The create_time of this Organization.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def access_key(self):
        """Gets the access_key of this Organization.  # noqa: E501


        :return: The access_key of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this Organization.


        :param access_key: The access_key of this Organization.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def server_limit(self):
        """Gets the server_limit of this Organization.  # noqa: E501


        :return: The server_limit of this Organization.  # noqa: E501
        :rtype: int
        """
        return self._server_limit

    @server_limit.setter
    def server_limit(self, server_limit):
        """Sets the server_limit of this Organization.


        :param server_limit: The server_limit of this Organization.  # noqa: E501
        :type: int
        """

        self._server_limit = server_limit

    @property
    def stripe_cust(self):
        """Gets the stripe_cust of this Organization.  # noqa: E501


        :return: The stripe_cust of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._stripe_cust

    @stripe_cust.setter
    def stripe_cust(self, stripe_cust):
        """Sets the stripe_cust of this Organization.


        :param stripe_cust: The stripe_cust of this Organization.  # noqa: E501
        :type: str
        """

        self._stripe_cust = stripe_cust

    @property
    def cc_last(self):
        """Gets the cc_last of this Organization.  # noqa: E501


        :return: The cc_last of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._cc_last

    @cc_last.setter
    def cc_last(self, cc_last):
        """Sets the cc_last of this Organization.


        :param cc_last: The cc_last of this Organization.  # noqa: E501
        :type: str
        """

        self._cc_last = cc_last

    @property
    def cc_exp(self):
        """Gets the cc_exp of this Organization.  # noqa: E501


        :return: The cc_exp of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._cc_exp

    @cc_exp.setter
    def cc_exp(self, cc_exp):
        """Sets the cc_exp of this Organization.


        :param cc_exp: The cc_exp of this Organization.  # noqa: E501
        :type: str
        """

        self._cc_exp = cc_exp

    @property
    def cc_brand(self):
        """Gets the cc_brand of this Organization.  # noqa: E501


        :return: The cc_brand of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._cc_brand

    @cc_brand.setter
    def cc_brand(self, cc_brand):
        """Sets the cc_brand of this Organization.


        :param cc_brand: The cc_brand of this Organization.  # noqa: E501
        :type: str
        """

        self._cc_brand = cc_brand

    @property
    def cc_name(self):
        """Gets the cc_name of this Organization.  # noqa: E501


        :return: The cc_name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._cc_name

    @cc_name.setter
    def cc_name(self, cc_name):
        """Sets the cc_name of this Organization.


        :param cc_name: The cc_name of this Organization.  # noqa: E501
        :type: str
        """

        self._cc_name = cc_name

    @property
    def billing_interval(self):
        """Gets the billing_interval of this Organization.  # noqa: E501


        :return: The billing_interval of this Organization.  # noqa: E501
        :rtype: int
        """
        return self._billing_interval

    @billing_interval.setter
    def billing_interval(self, billing_interval):
        """Sets the billing_interval of this Organization.


        :param billing_interval: The billing_interval of this Organization.  # noqa: E501
        :type: int
        """

        self._billing_interval = billing_interval

    @property
    def billing_interval_count(self):
        """Gets the billing_interval_count of this Organization.  # noqa: E501


        :return: The billing_interval_count of this Organization.  # noqa: E501
        :rtype: int
        """
        return self._billing_interval_count

    @billing_interval_count.setter
    def billing_interval_count(self, billing_interval_count):
        """Sets the billing_interval_count of this Organization.


        :param billing_interval_count: The billing_interval_count of this Organization.  # noqa: E501
        :type: int
        """

        self._billing_interval_count = billing_interval_count

    @property
    def trial_end_time(self):
        """Gets the trial_end_time of this Organization.  # noqa: E501


        :return: The trial_end_time of this Organization.  # noqa: E501
        :rtype: datetime
        """
        return self._trial_end_time

    @trial_end_time.setter
    def trial_end_time(self, trial_end_time):
        """Sets the trial_end_time of this Organization.


        :param trial_end_time: The trial_end_time of this Organization.  # noqa: E501
        :type: datetime
        """

        self._trial_end_time = trial_end_time

    @property
    def trial_expired(self):
        """Gets the trial_expired of this Organization.  # noqa: E501


        :return: The trial_expired of this Organization.  # noqa: E501
        :rtype: bool
        """
        return self._trial_expired

    @trial_expired.setter
    def trial_expired(self, trial_expired):
        """Sets the trial_expired of this Organization.


        :param trial_expired: The trial_expired of this Organization.  # noqa: E501
        :type: bool
        """

        self._trial_expired = trial_expired

    @property
    def sub_plan(self):
        """Gets the sub_plan of this Organization.  # noqa: E501


        :return: The sub_plan of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._sub_plan

    @sub_plan.setter
    def sub_plan(self, sub_plan):
        """Sets the sub_plan of this Organization.


        :param sub_plan: The sub_plan of this Organization.  # noqa: E501
        :type: str
        """

        self._sub_plan = sub_plan

    @property
    def sub_systems(self):
        """Gets the sub_systems of this Organization.  # noqa: E501


        :return: The sub_systems of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._sub_systems

    @sub_systems.setter
    def sub_systems(self, sub_systems):
        """Sets the sub_systems of this Organization.


        :param sub_systems: The sub_systems of this Organization.  # noqa: E501
        :type: str
        """

        self._sub_systems = sub_systems

    @property
    def sub_create_time(self):
        """Gets the sub_create_time of this Organization.  # noqa: E501


        :return: The sub_create_time of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._sub_create_time

    @sub_create_time.setter
    def sub_create_time(self, sub_create_time):
        """Sets the sub_create_time of this Organization.


        :param sub_create_time: The sub_create_time of this Organization.  # noqa: E501
        :type: str
        """

        self._sub_create_time = sub_create_time

    @property
    def sub_end_time(self):
        """Gets the sub_end_time of this Organization.  # noqa: E501


        :return: The sub_end_time of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._sub_end_time

    @sub_end_time.setter
    def sub_end_time(self, sub_end_time):
        """Sets the sub_end_time of this Organization.


        :param sub_end_time: The sub_end_time of this Organization.  # noqa: E501
        :type: str
        """

        self._sub_end_time = sub_end_time

    @property
    def next_bill_time(self):
        """Gets the next_bill_time of this Organization.  # noqa: E501


        :return: The next_bill_time of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._next_bill_time

    @next_bill_time.setter
    def next_bill_time(self, next_bill_time):
        """Sets the next_bill_time of this Organization.


        :param next_bill_time: The next_bill_time of this Organization.  # noqa: E501
        :type: str
        """

        self._next_bill_time = next_bill_time

    @property
    def rate_id(self):
        """Gets the rate_id of this Organization.  # noqa: E501


        :return: The rate_id of this Organization.  # noqa: E501
        :rtype: int
        """
        return self._rate_id

    @rate_id.setter
    def rate_id(self, rate_id):
        """Sets the rate_id of this Organization.


        :param rate_id: The rate_id of this Organization.  # noqa: E501
        :type: int
        """

        self._rate_id = rate_id

    @property
    def parent_id(self):
        """Gets the parent_id of this Organization.  # noqa: E501


        :return: The parent_id of this Organization.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Organization.


        :param parent_id: The parent_id of this Organization.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def bill_overages(self):
        """Gets the bill_overages of this Organization.  # noqa: E501


        :return: The bill_overages of this Organization.  # noqa: E501
        :rtype: bool
        """
        return self._bill_overages

    @bill_overages.setter
    def bill_overages(self, bill_overages):
        """Sets the bill_overages of this Organization.


        :param bill_overages: The bill_overages of this Organization.  # noqa: E501
        :type: bool
        """

        self._bill_overages = bill_overages

    @property
    def metadata(self):
        """Gets the metadata of this Organization.  # noqa: E501


        :return: The metadata of this Organization.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Organization.


        :param metadata: The metadata of this Organization.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def legacy_billing(self):
        """Gets the legacy_billing of this Organization.  # noqa: E501


        :return: The legacy_billing of this Organization.  # noqa: E501
        :rtype: bool
        """
        return self._legacy_billing

    @legacy_billing.setter
    def legacy_billing(self, legacy_billing):
        """Sets the legacy_billing of this Organization.


        :param legacy_billing: The legacy_billing of this Organization.  # noqa: E501
        :type: bool
        """

        self._legacy_billing = legacy_billing

    @property
    def billing_name(self):
        """Gets the billing_name of this Organization.  # noqa: E501


        :return: The billing_name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._billing_name

    @billing_name.setter
    def billing_name(self, billing_name):
        """Sets the billing_name of this Organization.


        :param billing_name: The billing_name of this Organization.  # noqa: E501
        :type: str
        """

        self._billing_name = billing_name

    @property
    def billing_email(self):
        """Gets the billing_email of this Organization.  # noqa: E501


        :return: The billing_email of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._billing_email

    @billing_email.setter
    def billing_email(self, billing_email):
        """Sets the billing_email of this Organization.


        :param billing_email: The billing_email of this Organization.  # noqa: E501
        :type: str
        """

        self._billing_email = billing_email

    @property
    def billing_phone(self):
        """Gets the billing_phone of this Organization.  # noqa: E501


        :return: The billing_phone of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._billing_phone

    @billing_phone.setter
    def billing_phone(self, billing_phone):
        """Sets the billing_phone of this Organization.


        :param billing_phone: The billing_phone of this Organization.  # noqa: E501
        :type: str
        """

        self._billing_phone = billing_phone

    @property
    def device_limit(self):
        """Gets the device_limit of this Organization.  # noqa: E501

        If your organization has a server limit (you will have contacted support for this), then this is the value for your organization. Otherwise, null.  # noqa: E501

        :return: The device_limit of this Organization.  # noqa: E501
        :rtype: float
        """
        return self._device_limit

    @device_limit.setter
    def device_limit(self, device_limit):
        """Sets the device_limit of this Organization.

        If your organization has a server limit (you will have contacted support for this), then this is the value for your organization. Otherwise, null.  # noqa: E501

        :param device_limit: The device_limit of this Organization.  # noqa: E501
        :type: float
        """

        self._device_limit = device_limit

    @property
    def device_count(self):
        """Gets the device_count of this Organization.  # noqa: E501

        The current number of installed devices for your organization  # noqa: E501

        :return: The device_count of this Organization.  # noqa: E501
        :rtype: float
        """
        return self._device_count

    @device_count.setter
    def device_count(self, device_count):
        """Sets the device_count of this Organization.

        The current number of installed devices for your organization  # noqa: E501

        :param device_count: The device_count of this Organization.  # noqa: E501
        :type: float
        """

        self._device_count = device_count

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
        if issubclass(Organization, dict):
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
        if not isinstance(other, Organization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
