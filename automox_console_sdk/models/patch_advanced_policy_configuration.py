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

class PatchAdvancedPolicyConfiguration(object):
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
        'auto_patch': 'bool',
        'missed_patch_window': 'bool',
        'patch_rule': 'str',
        'auto_reboot': 'bool',
        'device_filters_enabled': 'bool',
        'device_filters': 'DeviceFilters',
        'advanced_filter': 'list[PatchAdvancedPolicyConfigurationAdvancedFilter]',
        'include_optional': 'bool',
        'notify_reboot_user': 'bool',
        'notify_deferred_reboot_user': 'bool',
        'custom_notification_patch_message': 'str',
        'custom_notification_patch_message_mac': 'str',
        'custom_notification_reboot_message': 'str',
        'custom_notification_reboot_message_mac': 'str',
        'custom_notification_max_delays': 'int',
        'custom_notification_deferment_periods': 'list[int]',
        'custom_pending_reboot_notification_message': 'str',
        'custom_pending_reboot_notification_message_mac': 'str',
        'custom_pending_reboot_notification_max_delays': 'int',
        'custom_pending_reboot_notification_deferment_periods': 'list[int]',
        'notify_user_message_timeout': 'int',
        'notify_deferred_reboot_user_message_timeout': 'int',
        'notify_user_auto_deferral_enabled': 'bool',
        'notify_deferred_reboot_user_auto_deferral_enabled': 'bool'
    }

    attribute_map = {
        'auto_patch': 'auto_patch',
        'missed_patch_window': 'missed_patch_window',
        'patch_rule': 'patch_rule',
        'auto_reboot': 'auto_reboot',
        'device_filters_enabled': 'device_filters_enabled',
        'device_filters': 'device_filters',
        'advanced_filter': 'advanced_filter',
        'include_optional': 'include_optional',
        'notify_reboot_user': 'notify_reboot_user',
        'notify_deferred_reboot_user': 'notify_deferred_reboot_user',
        'custom_notification_patch_message': 'custom_notification_patch_message',
        'custom_notification_patch_message_mac': 'custom_notification_patch_message_mac',
        'custom_notification_reboot_message': 'custom_notification_reboot_message',
        'custom_notification_reboot_message_mac': 'custom_notification_reboot_message_mac',
        'custom_notification_max_delays': 'custom_notification_max_delays',
        'custom_notification_deferment_periods': 'custom_notification_deferment_periods',
        'custom_pending_reboot_notification_message': 'custom_pending_reboot_notification_message',
        'custom_pending_reboot_notification_message_mac': 'custom_pending_reboot_notification_message_mac',
        'custom_pending_reboot_notification_max_delays': 'custom_pending_reboot_notification_max_delays',
        'custom_pending_reboot_notification_deferment_periods': 'custom_pending_reboot_notification_deferment_periods',
        'notify_user_message_timeout': 'notify_user_message_timeout',
        'notify_deferred_reboot_user_message_timeout': 'notify_deferred_reboot_user_message_timeout',
        'notify_user_auto_deferral_enabled': 'notify_user_auto_deferral_enabled',
        'notify_deferred_reboot_user_auto_deferral_enabled': 'notify_deferred_reboot_user_auto_deferral_enabled'
    }

    def __init__(self, auto_patch=None, missed_patch_window=None, patch_rule='advanced', auto_reboot=None, device_filters_enabled=False, device_filters=None, advanced_filter=None, include_optional=False, notify_reboot_user=None, notify_deferred_reboot_user=None, custom_notification_patch_message=None, custom_notification_patch_message_mac=None, custom_notification_reboot_message=None, custom_notification_reboot_message_mac=None, custom_notification_max_delays=0, custom_notification_deferment_periods=None, custom_pending_reboot_notification_message=None, custom_pending_reboot_notification_message_mac=None, custom_pending_reboot_notification_max_delays=0, custom_pending_reboot_notification_deferment_periods=None, notify_user_message_timeout=15, notify_deferred_reboot_user_message_timeout=15, notify_user_auto_deferral_enabled=False, notify_deferred_reboot_user_auto_deferral_enabled=False):  # noqa: E501
        """PatchAdvancedPolicyConfiguration - a model defined in Swagger"""  # noqa: E501
        self._auto_patch = None
        self._missed_patch_window = None
        self._patch_rule = None
        self._auto_reboot = None
        self._device_filters_enabled = None
        self._device_filters = None
        self._advanced_filter = None
        self._include_optional = None
        self._notify_reboot_user = None
        self._notify_deferred_reboot_user = None
        self._custom_notification_patch_message = None
        self._custom_notification_patch_message_mac = None
        self._custom_notification_reboot_message = None
        self._custom_notification_reboot_message_mac = None
        self._custom_notification_max_delays = None
        self._custom_notification_deferment_periods = None
        self._custom_pending_reboot_notification_message = None
        self._custom_pending_reboot_notification_message_mac = None
        self._custom_pending_reboot_notification_max_delays = None
        self._custom_pending_reboot_notification_deferment_periods = None
        self._notify_user_message_timeout = None
        self._notify_deferred_reboot_user_message_timeout = None
        self._notify_user_auto_deferral_enabled = None
        self._notify_deferred_reboot_user_auto_deferral_enabled = None
        self.discriminator = None
        self.auto_patch = auto_patch
        if missed_patch_window is not None:
            self.missed_patch_window = missed_patch_window
        if patch_rule is not None:
            self.patch_rule = patch_rule
        self.auto_reboot = auto_reboot
        if device_filters_enabled is not None:
            self.device_filters_enabled = device_filters_enabled
        if device_filters is not None:
            self.device_filters = device_filters
        if advanced_filter is not None:
            self.advanced_filter = advanced_filter
        if include_optional is not None:
            self.include_optional = include_optional
        if notify_reboot_user is not None:
            self.notify_reboot_user = notify_reboot_user
        if notify_deferred_reboot_user is not None:
            self.notify_deferred_reboot_user = notify_deferred_reboot_user
        if custom_notification_patch_message is not None:
            self.custom_notification_patch_message = custom_notification_patch_message
        if custom_notification_patch_message_mac is not None:
            self.custom_notification_patch_message_mac = custom_notification_patch_message_mac
        if custom_notification_reboot_message is not None:
            self.custom_notification_reboot_message = custom_notification_reboot_message
        if custom_notification_reboot_message_mac is not None:
            self.custom_notification_reboot_message_mac = custom_notification_reboot_message_mac
        if custom_notification_max_delays is not None:
            self.custom_notification_max_delays = custom_notification_max_delays
        if custom_notification_deferment_periods is not None:
            self.custom_notification_deferment_periods = custom_notification_deferment_periods
        if custom_pending_reboot_notification_message is not None:
            self.custom_pending_reboot_notification_message = custom_pending_reboot_notification_message
        if custom_pending_reboot_notification_message_mac is not None:
            self.custom_pending_reboot_notification_message_mac = custom_pending_reboot_notification_message_mac
        if custom_pending_reboot_notification_max_delays is not None:
            self.custom_pending_reboot_notification_max_delays = custom_pending_reboot_notification_max_delays
        if custom_pending_reboot_notification_deferment_periods is not None:
            self.custom_pending_reboot_notification_deferment_periods = custom_pending_reboot_notification_deferment_periods
        if notify_user_message_timeout is not None:
            self.notify_user_message_timeout = notify_user_message_timeout
        if notify_deferred_reboot_user_message_timeout is not None:
            self.notify_deferred_reboot_user_message_timeout = notify_deferred_reboot_user_message_timeout
        if notify_user_auto_deferral_enabled is not None:
            self.notify_user_auto_deferral_enabled = notify_user_auto_deferral_enabled
        if notify_deferred_reboot_user_auto_deferral_enabled is not None:
            self.notify_deferred_reboot_user_auto_deferral_enabled = notify_deferred_reboot_user_auto_deferral_enabled

    @property
    def auto_patch(self):
        """Gets the auto_patch of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Enable or Disable automatic execution of the policy.  # noqa: E501

        :return: The auto_patch of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._auto_patch

    @auto_patch.setter
    def auto_patch(self, auto_patch):
        """Sets the auto_patch of this PatchAdvancedPolicyConfiguration.

        Enable or Disable automatic execution of the policy.  # noqa: E501

        :param auto_patch: The auto_patch of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: bool
        """
        if auto_patch is None:
            raise ValueError("Invalid value for `auto_patch`, must not be `None`")  # noqa: E501

        self._auto_patch = auto_patch

    @property
    def missed_patch_window(self):
        """Gets the missed_patch_window of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Enable or Disable the Missed Patch Window setting.  # noqa: E501

        :return: The missed_patch_window of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._missed_patch_window

    @missed_patch_window.setter
    def missed_patch_window(self, missed_patch_window):
        """Sets the missed_patch_window of this PatchAdvancedPolicyConfiguration.

        Enable or Disable the Missed Patch Window setting.  # noqa: E501

        :param missed_patch_window: The missed_patch_window of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: bool
        """

        self._missed_patch_window = missed_patch_window

    @property
    def patch_rule(self):
        """Gets the patch_rule of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Use only with the `patch` policy type.  # noqa: E501

        :return: The patch_rule of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._patch_rule

    @patch_rule.setter
    def patch_rule(self, patch_rule):
        """Sets the patch_rule of this PatchAdvancedPolicyConfiguration.

        Use only with the `patch` policy type.  # noqa: E501

        :param patch_rule: The patch_rule of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["all", "filter", "manual", "advanced"]  # noqa: E501
        if patch_rule not in allowed_values:
            raise ValueError(
                "Invalid value for `patch_rule` ({0}), must be one of {1}"  # noqa: E501
                .format(patch_rule, allowed_values)
            )

        self._patch_rule = patch_rule

    @property
    def auto_reboot(self):
        """Gets the auto_reboot of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Enable or Disable automatic reboots following policy execution.  # noqa: E501

        :return: The auto_reboot of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._auto_reboot

    @auto_reboot.setter
    def auto_reboot(self, auto_reboot):
        """Sets the auto_reboot of this PatchAdvancedPolicyConfiguration.

        Enable or Disable automatic reboots following policy execution.  # noqa: E501

        :param auto_reboot: The auto_reboot of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: bool
        """
        if auto_reboot is None:
            raise ValueError("Invalid value for `auto_reboot`, must not be `None`")  # noqa: E501

        self._auto_reboot = auto_reboot

    @property
    def device_filters_enabled(self):
        """Gets the device_filters_enabled of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Enable or disable Device Filters.  # noqa: E501

        :return: The device_filters_enabled of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._device_filters_enabled

    @device_filters_enabled.setter
    def device_filters_enabled(self, device_filters_enabled):
        """Sets the device_filters_enabled of this PatchAdvancedPolicyConfiguration.

        Enable or disable Device Filters.  # noqa: E501

        :param device_filters_enabled: The device_filters_enabled of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: bool
        """

        self._device_filters_enabled = device_filters_enabled

    @property
    def device_filters(self):
        """Gets the device_filters of this PatchAdvancedPolicyConfiguration.  # noqa: E501


        :return: The device_filters of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: DeviceFilters
        """
        return self._device_filters

    @device_filters.setter
    def device_filters(self, device_filters):
        """Sets the device_filters of this PatchAdvancedPolicyConfiguration.


        :param device_filters: The device_filters of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: DeviceFilters
        """

        self._device_filters = device_filters

    @property
    def advanced_filter(self):
        """Gets the advanced_filter of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Object array. Include one object per advanced filter line. See [Policy and Device Filters, and Scheduling - Advanced Filters](/developer-portal/policy_filters_schedule/#advanced-filters)  # noqa: E501

        :return: The advanced_filter of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: list[PatchAdvancedPolicyConfigurationAdvancedFilter]
        """
        return self._advanced_filter

    @advanced_filter.setter
    def advanced_filter(self, advanced_filter):
        """Sets the advanced_filter of this PatchAdvancedPolicyConfiguration.

        Object array. Include one object per advanced filter line. See [Policy and Device Filters, and Scheduling - Advanced Filters](/developer-portal/policy_filters_schedule/#advanced-filters)  # noqa: E501

        :param advanced_filter: The advanced_filter of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: list[PatchAdvancedPolicyConfigurationAdvancedFilter]
        """

        self._advanced_filter = advanced_filter

    @property
    def include_optional(self):
        """Gets the include_optional of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Enable or disable inclusion of optional Windows patches for this policy **NOTE:** Will default to false if not included.  # noqa: E501

        :return: The include_optional of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._include_optional

    @include_optional.setter
    def include_optional(self, include_optional):
        """Sets the include_optional of this PatchAdvancedPolicyConfiguration.

        Enable or disable inclusion of optional Windows patches for this policy **NOTE:** Will default to false if not included.  # noqa: E501

        :param include_optional: The include_optional of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: bool
        """

        self._include_optional = include_optional

    @property
    def notify_reboot_user(self):
        """Gets the notify_reboot_user of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Display modified notification 15 minutes before patching. This message should inform the user that a reboot will follow patching actions.  # noqa: E501

        :return: The notify_reboot_user of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._notify_reboot_user

    @notify_reboot_user.setter
    def notify_reboot_user(self, notify_reboot_user):
        """Sets the notify_reboot_user of this PatchAdvancedPolicyConfiguration.

        Display modified notification 15 minutes before patching. This message should inform the user that a reboot will follow patching actions.  # noqa: E501

        :param notify_reboot_user: The notify_reboot_user of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: bool
        """

        self._notify_reboot_user = notify_reboot_user

    @property
    def notify_deferred_reboot_user(self):
        """Gets the notify_deferred_reboot_user of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        If `true`, this shows a post-install reboot notification message, if `notify_reboot_deferred` is also `true`. If `notify_reboot_deferred` is `false` or `null`, this will sync with the existing `notify_reboot_user` parameter.  # noqa: E501

        :return: The notify_deferred_reboot_user of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._notify_deferred_reboot_user

    @notify_deferred_reboot_user.setter
    def notify_deferred_reboot_user(self, notify_deferred_reboot_user):
        """Sets the notify_deferred_reboot_user of this PatchAdvancedPolicyConfiguration.

        If `true`, this shows a post-install reboot notification message, if `notify_reboot_deferred` is also `true`. If `notify_reboot_deferred` is `false` or `null`, this will sync with the existing `notify_reboot_user` parameter.  # noqa: E501

        :param notify_deferred_reboot_user: The notify_deferred_reboot_user of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: bool
        """

        self._notify_deferred_reboot_user = notify_deferred_reboot_user

    @property
    def custom_notification_patch_message(self):
        """Gets the custom_notification_patch_message of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Message to display before a non-rebooting patch policy executes on a Windows device. Maximum 125 characters  # noqa: E501

        :return: The custom_notification_patch_message of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._custom_notification_patch_message

    @custom_notification_patch_message.setter
    def custom_notification_patch_message(self, custom_notification_patch_message):
        """Sets the custom_notification_patch_message of this PatchAdvancedPolicyConfiguration.

        Message to display before a non-rebooting patch policy executes on a Windows device. Maximum 125 characters  # noqa: E501

        :param custom_notification_patch_message: The custom_notification_patch_message of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: str
        """

        self._custom_notification_patch_message = custom_notification_patch_message

    @property
    def custom_notification_patch_message_mac(self):
        """Gets the custom_notification_patch_message_mac of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Message to display before a non-rebooting patch policy executes on a macOS device. Maximum 70 characters  # noqa: E501

        :return: The custom_notification_patch_message_mac of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._custom_notification_patch_message_mac

    @custom_notification_patch_message_mac.setter
    def custom_notification_patch_message_mac(self, custom_notification_patch_message_mac):
        """Sets the custom_notification_patch_message_mac of this PatchAdvancedPolicyConfiguration.

        Message to display before a non-rebooting patch policy executes on a macOS device. Maximum 70 characters  # noqa: E501

        :param custom_notification_patch_message_mac: The custom_notification_patch_message_mac of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: str
        """

        self._custom_notification_patch_message_mac = custom_notification_patch_message_mac

    @property
    def custom_notification_reboot_message(self):
        """Gets the custom_notification_reboot_message of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Message to display before a rebooting patch policy executes on a Windows device. Reboot will follow patching actions. Maximum 125 characters  # noqa: E501

        :return: The custom_notification_reboot_message of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._custom_notification_reboot_message

    @custom_notification_reboot_message.setter
    def custom_notification_reboot_message(self, custom_notification_reboot_message):
        """Sets the custom_notification_reboot_message of this PatchAdvancedPolicyConfiguration.

        Message to display before a rebooting patch policy executes on a Windows device. Reboot will follow patching actions. Maximum 125 characters  # noqa: E501

        :param custom_notification_reboot_message: The custom_notification_reboot_message of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: str
        """

        self._custom_notification_reboot_message = custom_notification_reboot_message

    @property
    def custom_notification_reboot_message_mac(self):
        """Gets the custom_notification_reboot_message_mac of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Message to display before a rebooting patch policy executes on a macOS device. Reboot will follow patching actions. Maximum 70 characters  # noqa: E501

        :return: The custom_notification_reboot_message_mac of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._custom_notification_reboot_message_mac

    @custom_notification_reboot_message_mac.setter
    def custom_notification_reboot_message_mac(self, custom_notification_reboot_message_mac):
        """Sets the custom_notification_reboot_message_mac of this PatchAdvancedPolicyConfiguration.

        Message to display before a rebooting patch policy executes on a macOS device. Reboot will follow patching actions. Maximum 70 characters  # noqa: E501

        :param custom_notification_reboot_message_mac: The custom_notification_reboot_message_mac of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: str
        """

        self._custom_notification_reboot_message_mac = custom_notification_reboot_message_mac

    @property
    def custom_notification_max_delays(self):
        """Gets the custom_notification_max_delays of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Maximum number of times a user is allowed to defer the reboot. The default is 0.  # noqa: E501

        :return: The custom_notification_max_delays of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._custom_notification_max_delays

    @custom_notification_max_delays.setter
    def custom_notification_max_delays(self, custom_notification_max_delays):
        """Sets the custom_notification_max_delays of this PatchAdvancedPolicyConfiguration.

        Maximum number of times a user is allowed to defer the reboot. The default is 0.  # noqa: E501

        :param custom_notification_max_delays: The custom_notification_max_delays of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: int
        """

        self._custom_notification_max_delays = custom_notification_max_delays

    @property
    def custom_notification_deferment_periods(self):
        """Gets the custom_notification_deferment_periods of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Integer array: Deferral time periods (hours) that users can choose from. Include up to 3. All 3 must be distinct with a maximum of 24. Default values: 1, 4, 8  # noqa: E501

        :return: The custom_notification_deferment_periods of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: list[int]
        """
        return self._custom_notification_deferment_periods

    @custom_notification_deferment_periods.setter
    def custom_notification_deferment_periods(self, custom_notification_deferment_periods):
        """Sets the custom_notification_deferment_periods of this PatchAdvancedPolicyConfiguration.

        Integer array: Deferral time periods (hours) that users can choose from. Include up to 3. All 3 must be distinct with a maximum of 24. Default values: 1, 4, 8  # noqa: E501

        :param custom_notification_deferment_periods: The custom_notification_deferment_periods of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: list[int]
        """

        self._custom_notification_deferment_periods = custom_notification_deferment_periods

    @property
    def custom_pending_reboot_notification_message(self):
        """Gets the custom_pending_reboot_notification_message of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Custom reboot message.  # noqa: E501

        :return: The custom_pending_reboot_notification_message of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._custom_pending_reboot_notification_message

    @custom_pending_reboot_notification_message.setter
    def custom_pending_reboot_notification_message(self, custom_pending_reboot_notification_message):
        """Sets the custom_pending_reboot_notification_message of this PatchAdvancedPolicyConfiguration.

        Custom reboot message.  # noqa: E501

        :param custom_pending_reboot_notification_message: The custom_pending_reboot_notification_message of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: str
        """

        self._custom_pending_reboot_notification_message = custom_pending_reboot_notification_message

    @property
    def custom_pending_reboot_notification_message_mac(self):
        """Gets the custom_pending_reboot_notification_message_mac of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        The custom reboot message for macOS, which overrides `custom_pending_reboot_notification_message` string, if provided.  # noqa: E501

        :return: The custom_pending_reboot_notification_message_mac of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._custom_pending_reboot_notification_message_mac

    @custom_pending_reboot_notification_message_mac.setter
    def custom_pending_reboot_notification_message_mac(self, custom_pending_reboot_notification_message_mac):
        """Sets the custom_pending_reboot_notification_message_mac of this PatchAdvancedPolicyConfiguration.

        The custom reboot message for macOS, which overrides `custom_pending_reboot_notification_message` string, if provided.  # noqa: E501

        :param custom_pending_reboot_notification_message_mac: The custom_pending_reboot_notification_message_mac of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: str
        """

        self._custom_pending_reboot_notification_message_mac = custom_pending_reboot_notification_message_mac

    @property
    def custom_pending_reboot_notification_max_delays(self):
        """Gets the custom_pending_reboot_notification_max_delays of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        Maximum number of times a user is allowed to defer the reboot. The default is 0.  # noqa: E501

        :return: The custom_pending_reboot_notification_max_delays of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._custom_pending_reboot_notification_max_delays

    @custom_pending_reboot_notification_max_delays.setter
    def custom_pending_reboot_notification_max_delays(self, custom_pending_reboot_notification_max_delays):
        """Sets the custom_pending_reboot_notification_max_delays of this PatchAdvancedPolicyConfiguration.

        Maximum number of times a user is allowed to defer the reboot. The default is 0.  # noqa: E501

        :param custom_pending_reboot_notification_max_delays: The custom_pending_reboot_notification_max_delays of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: int
        """

        self._custom_pending_reboot_notification_max_delays = custom_pending_reboot_notification_max_delays

    @property
    def custom_pending_reboot_notification_deferment_periods(self):
        """Gets the custom_pending_reboot_notification_deferment_periods of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        The time period options available to defer a reboot for each deferral selection. Default values: 1, 4, 8  # noqa: E501

        :return: The custom_pending_reboot_notification_deferment_periods of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: list[int]
        """
        return self._custom_pending_reboot_notification_deferment_periods

    @custom_pending_reboot_notification_deferment_periods.setter
    def custom_pending_reboot_notification_deferment_periods(self, custom_pending_reboot_notification_deferment_periods):
        """Sets the custom_pending_reboot_notification_deferment_periods of this PatchAdvancedPolicyConfiguration.

        The time period options available to defer a reboot for each deferral selection. Default values: 1, 4, 8  # noqa: E501

        :param custom_pending_reboot_notification_deferment_periods: The custom_pending_reboot_notification_deferment_periods of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: list[int]
        """

        self._custom_pending_reboot_notification_deferment_periods = custom_pending_reboot_notification_deferment_periods

    @property
    def notify_user_message_timeout(self):
        """Gets the notify_user_message_timeout of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        The amount of time a patch notification appears before timing out and closing. Min: 15 min. Max: 480 min. Default is 15 minutes.  # noqa: E501

        :return: The notify_user_message_timeout of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._notify_user_message_timeout

    @notify_user_message_timeout.setter
    def notify_user_message_timeout(self, notify_user_message_timeout):
        """Sets the notify_user_message_timeout of this PatchAdvancedPolicyConfiguration.

        The amount of time a patch notification appears before timing out and closing. Min: 15 min. Max: 480 min. Default is 15 minutes.  # noqa: E501

        :param notify_user_message_timeout: The notify_user_message_timeout of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: int
        """

        self._notify_user_message_timeout = notify_user_message_timeout

    @property
    def notify_deferred_reboot_user_message_timeout(self):
        """Gets the notify_deferred_reboot_user_message_timeout of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        The amount of time a deferrable reboot notification message appears before timing out and closing. Min: 15 min. Max: 480 min. Default is 15 minutes.  # noqa: E501

        :return: The notify_deferred_reboot_user_message_timeout of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._notify_deferred_reboot_user_message_timeout

    @notify_deferred_reboot_user_message_timeout.setter
    def notify_deferred_reboot_user_message_timeout(self, notify_deferred_reboot_user_message_timeout):
        """Sets the notify_deferred_reboot_user_message_timeout of this PatchAdvancedPolicyConfiguration.

        The amount of time a deferrable reboot notification message appears before timing out and closing. Min: 15 min. Max: 480 min. Default is 15 minutes.  # noqa: E501

        :param notify_deferred_reboot_user_message_timeout: The notify_deferred_reboot_user_message_timeout of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: int
        """

        self._notify_deferred_reboot_user_message_timeout = notify_deferred_reboot_user_message_timeout

    @property
    def notify_user_auto_deferral_enabled(self):
        """Gets the notify_user_auto_deferral_enabled of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        If a patch notification times out, apply the highest configured patch deferral.  # noqa: E501

        :return: The notify_user_auto_deferral_enabled of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._notify_user_auto_deferral_enabled

    @notify_user_auto_deferral_enabled.setter
    def notify_user_auto_deferral_enabled(self, notify_user_auto_deferral_enabled):
        """Sets the notify_user_auto_deferral_enabled of this PatchAdvancedPolicyConfiguration.

        If a patch notification times out, apply the highest configured patch deferral.  # noqa: E501

        :param notify_user_auto_deferral_enabled: The notify_user_auto_deferral_enabled of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: bool
        """

        self._notify_user_auto_deferral_enabled = notify_user_auto_deferral_enabled

    @property
    def notify_deferred_reboot_user_auto_deferral_enabled(self):
        """Gets the notify_deferred_reboot_user_auto_deferral_enabled of this PatchAdvancedPolicyConfiguration.  # noqa: E501

        If a reboot notification times out, apply the highest configured reboot deferral.  # noqa: E501

        :return: The notify_deferred_reboot_user_auto_deferral_enabled of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._notify_deferred_reboot_user_auto_deferral_enabled

    @notify_deferred_reboot_user_auto_deferral_enabled.setter
    def notify_deferred_reboot_user_auto_deferral_enabled(self, notify_deferred_reboot_user_auto_deferral_enabled):
        """Sets the notify_deferred_reboot_user_auto_deferral_enabled of this PatchAdvancedPolicyConfiguration.

        If a reboot notification times out, apply the highest configured reboot deferral.  # noqa: E501

        :param notify_deferred_reboot_user_auto_deferral_enabled: The notify_deferred_reboot_user_auto_deferral_enabled of this PatchAdvancedPolicyConfiguration.  # noqa: E501
        :type: bool
        """

        self._notify_deferred_reboot_user_auto_deferral_enabled = notify_deferred_reboot_user_auto_deferral_enabled

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
        if issubclass(PatchAdvancedPolicyConfiguration, dict):
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
        if not isinstance(other, PatchAdvancedPolicyConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other