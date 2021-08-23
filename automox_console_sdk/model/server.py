"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    The version of the OpenAPI document: 2021-08-10
    Contact: support@automox.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from automox_console_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from automox_console_sdk.exceptions import ApiAttributeError


def lazy_import():
    from automox_console_sdk.model.command import Command
    from automox_console_sdk.model.device_status import DeviceStatus
    from automox_console_sdk.model.server_detail import ServerDetail
    from automox_console_sdk.model.server_policy_status import ServerPolicyStatus
    globals()['Command'] = Command
    globals()['DeviceStatus'] = DeviceStatus
    globals()['ServerDetail'] = ServerDetail
    globals()['ServerPolicyStatus'] = ServerPolicyStatus


class Server(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (int,),  # noqa: E501
            'os_version_id': (int,),  # noqa: E501
            'server_group_id': (int,),  # noqa: E501
            'organization_id': (int,),  # noqa: E501
            'uuid': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'instance_id': (str,),  # noqa: E501
            'refresh_interval': (int,),  # noqa: E501
            'last_update_time': (str,),  # noqa: E501
            'last_refresh_time': (str,),  # noqa: E501
            'uptime': (int,),  # noqa: E501
            'needs_reboot': (bool,),  # noqa: E501
            'timezone': (str,),  # noqa: E501
            'tags': ([str],),  # noqa: E501
            'deleted': (bool,),  # noqa: E501
            'create_time': (datetime,),  # noqa: E501
            'os_version': (str,),  # noqa: E501
            'os_name': (str,),  # noqa: E501
            'os_family': (str,),  # noqa: E501
            'ip_addrs': ([str],),  # noqa: E501
            'ip_addrs_private': ([str],),  # noqa: E501
            'patches': (int,),  # noqa: E501
            'details': (ServerDetail,),  # noqa: E501
            'agent_version': (str,),  # noqa: E501
            'custom_name': (str,),  # noqa: E501
            'exception': (bool,),  # noqa: E501
            'total_count': (int,),  # noqa: E501
            'policy_status': ([ServerPolicyStatus],),  # noqa: E501
            'last_scan_failed': (bool,),  # noqa: E501
            'pending': (bool,),  # noqa: E501
            'compliant': (bool,),  # noqa: E501
            'display_name': (str,),  # noqa: E501
            'commands': ([Command],),  # noqa: E501
            'pending_patches': (int,),  # noqa: E501
            'connected': (bool,),  # noqa: E501
            'last_process_time': (str,),  # noqa: E501
            'next_patch_time': (str,),  # noqa: E501
            'notification_count': (int,),  # noqa: E501
            'reboot_notification_count': (int,),  # noqa: E501
            'patch_deferral_count': (int,),  # noqa: E501
            'is_delayed_by_notification': (bool,),  # noqa: E501
            'reboot_is_delayed_by_notification': (bool,),  # noqa: E501
            'is_delayed_by_user': (bool,),  # noqa: E501
            'reboot_is_delayed_by_user': (bool,),  # noqa: E501
            'last_disconnect_time': (datetime,),  # noqa: E501
            'needs_attention': (bool,),  # noqa: E501
            'serial_number': (str,),  # noqa: E501
            'status': (DeviceStatus,),  # noqa: E501
            'last_logged_in_user': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'os_version_id': 'os_version_id',  # noqa: E501
        'server_group_id': 'server_group_id',  # noqa: E501
        'organization_id': 'organization_id',  # noqa: E501
        'uuid': 'uuid',  # noqa: E501
        'name': 'name',  # noqa: E501
        'instance_id': 'instance_id',  # noqa: E501
        'refresh_interval': 'refresh_interval',  # noqa: E501
        'last_update_time': 'last_update_time',  # noqa: E501
        'last_refresh_time': 'last_refresh_time',  # noqa: E501
        'uptime': 'uptime',  # noqa: E501
        'needs_reboot': 'needs_reboot',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'create_time': 'create_time',  # noqa: E501
        'os_version': 'os_version',  # noqa: E501
        'os_name': 'os_name',  # noqa: E501
        'os_family': 'os_family',  # noqa: E501
        'ip_addrs': 'ip_addrs',  # noqa: E501
        'ip_addrs_private': 'ip_addrs_private',  # noqa: E501
        'patches': 'patches',  # noqa: E501
        'details': 'details',  # noqa: E501
        'agent_version': 'agent_version',  # noqa: E501
        'custom_name': 'custom_name',  # noqa: E501
        'exception': 'exception',  # noqa: E501
        'total_count': 'total_count',  # noqa: E501
        'policy_status': 'policy_status',  # noqa: E501
        'last_scan_failed': 'last_scan_failed',  # noqa: E501
        'pending': 'pending',  # noqa: E501
        'compliant': 'compliant',  # noqa: E501
        'display_name': 'display_name',  # noqa: E501
        'commands': 'commands',  # noqa: E501
        'pending_patches': 'pending_patches',  # noqa: E501
        'connected': 'connected',  # noqa: E501
        'last_process_time': 'last_process_time',  # noqa: E501
        'next_patch_time': 'next_patch_time',  # noqa: E501
        'notification_count': 'notification_count',  # noqa: E501
        'reboot_notification_count': 'reboot_notification_count',  # noqa: E501
        'patch_deferral_count': 'patch_deferral_count',  # noqa: E501
        'is_delayed_by_notification': 'is_delayed_by_notification',  # noqa: E501
        'reboot_is_delayed_by_notification': 'reboot_is_delayed_by_notification',  # noqa: E501
        'is_delayed_by_user': 'is_delayed_by_user',  # noqa: E501
        'reboot_is_delayed_by_user': 'reboot_is_delayed_by_user',  # noqa: E501
        'last_disconnect_time': 'last_disconnect_time',  # noqa: E501
        'needs_attention': 'needs_attention',  # noqa: E501
        'serial_number': 'serial_number',  # noqa: E501
        'status': 'status',  # noqa: E501
        'last_logged_in_user': 'last_logged_in_user',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Server - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): [optional]  # noqa: E501
            os_version_id (int): [optional]  # noqa: E501
            server_group_id (int): [optional]  # noqa: E501
            organization_id (int): [optional]  # noqa: E501
            uuid (str): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            instance_id (str): [optional]  # noqa: E501
            refresh_interval (int): [optional]  # noqa: E501
            last_update_time (str): [optional]  # noqa: E501
            last_refresh_time (str): [optional]  # noqa: E501
            uptime (int): [optional]  # noqa: E501
            needs_reboot (bool): [optional]  # noqa: E501
            timezone (str): [optional]  # noqa: E501
            tags ([str]): [optional]  # noqa: E501
            deleted (bool): [optional]  # noqa: E501
            create_time (datetime): [optional]  # noqa: E501
            os_version (str): [optional]  # noqa: E501
            os_name (str): [optional]  # noqa: E501
            os_family (str): [optional]  # noqa: E501
            ip_addrs ([str]): [optional]  # noqa: E501
            ip_addrs_private ([str]): [optional]  # noqa: E501
            patches (int): [optional]  # noqa: E501
            details (ServerDetail): [optional]  # noqa: E501
            agent_version (str): [optional]  # noqa: E501
            custom_name (str): [optional]  # noqa: E501
            exception (bool): [optional]  # noqa: E501
            total_count (int): [optional]  # noqa: E501
            policy_status ([ServerPolicyStatus]): [optional]  # noqa: E501
            last_scan_failed (bool): [optional]  # noqa: E501
            pending (bool): [optional]  # noqa: E501
            compliant (bool): [optional]  # noqa: E501
            display_name (str): [optional]  # noqa: E501
            commands ([Command]): [optional]  # noqa: E501
            pending_patches (int): [optional]  # noqa: E501
            connected (bool): [optional]  # noqa: E501
            last_process_time (str): [optional]  # noqa: E501
            next_patch_time (str): [optional]  # noqa: E501
            notification_count (int): [optional]  # noqa: E501
            reboot_notification_count (int): [optional]  # noqa: E501
            patch_deferral_count (int): [optional]  # noqa: E501
            is_delayed_by_notification (bool): [optional]  # noqa: E501
            reboot_is_delayed_by_notification (bool): [optional]  # noqa: E501
            is_delayed_by_user (bool): [optional]  # noqa: E501
            reboot_is_delayed_by_user (bool): [optional]  # noqa: E501
            last_disconnect_time (datetime): [optional]  # noqa: E501
            needs_attention (bool): [optional]  # noqa: E501
            serial_number (str): [optional]  # noqa: E501
            status (DeviceStatus): [optional]  # noqa: E501
            last_logged_in_user (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Server - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): [optional]  # noqa: E501
            os_version_id (int): [optional]  # noqa: E501
            server_group_id (int): [optional]  # noqa: E501
            organization_id (int): [optional]  # noqa: E501
            uuid (str): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            instance_id (str): [optional]  # noqa: E501
            refresh_interval (int): [optional]  # noqa: E501
            last_update_time (str): [optional]  # noqa: E501
            last_refresh_time (str): [optional]  # noqa: E501
            uptime (int): [optional]  # noqa: E501
            needs_reboot (bool): [optional]  # noqa: E501
            timezone (str): [optional]  # noqa: E501
            tags ([str]): [optional]  # noqa: E501
            deleted (bool): [optional]  # noqa: E501
            create_time (datetime): [optional]  # noqa: E501
            os_version (str): [optional]  # noqa: E501
            os_name (str): [optional]  # noqa: E501
            os_family (str): [optional]  # noqa: E501
            ip_addrs ([str]): [optional]  # noqa: E501
            ip_addrs_private ([str]): [optional]  # noqa: E501
            patches (int): [optional]  # noqa: E501
            details (ServerDetail): [optional]  # noqa: E501
            agent_version (str): [optional]  # noqa: E501
            custom_name (str): [optional]  # noqa: E501
            exception (bool): [optional]  # noqa: E501
            total_count (int): [optional]  # noqa: E501
            policy_status ([ServerPolicyStatus]): [optional]  # noqa: E501
            last_scan_failed (bool): [optional]  # noqa: E501
            pending (bool): [optional]  # noqa: E501
            compliant (bool): [optional]  # noqa: E501
            display_name (str): [optional]  # noqa: E501
            commands ([Command]): [optional]  # noqa: E501
            pending_patches (int): [optional]  # noqa: E501
            connected (bool): [optional]  # noqa: E501
            last_process_time (str): [optional]  # noqa: E501
            next_patch_time (str): [optional]  # noqa: E501
            notification_count (int): [optional]  # noqa: E501
            reboot_notification_count (int): [optional]  # noqa: E501
            patch_deferral_count (int): [optional]  # noqa: E501
            is_delayed_by_notification (bool): [optional]  # noqa: E501
            reboot_is_delayed_by_notification (bool): [optional]  # noqa: E501
            is_delayed_by_user (bool): [optional]  # noqa: E501
            reboot_is_delayed_by_user (bool): [optional]  # noqa: E501
            last_disconnect_time (datetime): [optional]  # noqa: E501
            needs_attention (bool): [optional]  # noqa: E501
            serial_number (str): [optional]  # noqa: E501
            status (DeviceStatus): [optional]  # noqa: E501
            last_logged_in_user (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
