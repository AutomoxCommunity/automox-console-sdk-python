# PatchPolicyConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_patch** | **bool** | Enable or disable Auto Patch. | 
**auto_reboot** | **bool** | Enable or disable Auto Reboot. | 
**notify_user** | **bool** |  | 
**missed_patch_window** | **bool** |  | [optional] 
**patch_rule** | **str** | Use only with Patch policy. | 
**filter_type** | **str** | The type of filter being used. Use only with &#x60;patch_rule&#x60; &#x3D; &#x60;filter&#x60; | [optional] 
**device_filters_enabled** | **bool** | Enable or disable Device Targeting Filters. | [optional] [default to False]
**device_filters** | [**DeviceFilters**](DeviceFilters.md) |  | [optional] 
**include_optional** | **bool** | Enable or disable inclusion of optional Windows patches for this policy **NOTE:** Will default to false if not included. | [optional] [default to False]
**notify_reboot_user** | **bool** | Display modified notification 15 minutes before patching. This message should inform the user that a reboot will follow patching actions. | [optional] 
**notify_deferred_reboot_user** | **bool** | If &#x60;true&#x60;, this shows a post-install reboot notification message, if &#x60;notify_reboot_deferred&#x60; is also &#x60;true&#x60;. If &#x60;notify_reboot_deferred&#x60; is &#x60;false&#x60; or &#x60;null&#x60;, this will sync with the existing &#x60;notify_reboot_user&#x60; parameter. | [optional] 
**custom_notification_patch_message** | **str** | Message to display before a non-rebooting patch policy executes on a Windows device. Maximum 125 characters | [optional] 
**custom_notification_patch_message_mac** | **str** | Message to display before a non-rebooting patch policy executes on a macOS device. Maximum 70 characters | [optional] 
**custom_notification_reboot_message** | **str** | Message to display before a rebooting patch policy executes on a Windows device. Reboot will follow patching actions. Maximum 125 characters | [optional] 
**custom_notification_reboot_message_mac** | **str** | Message to display before a rebooting patch policy executes on a macOS device. Reboot will follow patching actions. Maximum 70 characters | [optional] 
**custom_notification_max_delays** | **int** | Maximum number of times a user is allowed to defer the reboot. The default is 0. | [optional] [default to 0]
**custom_notification_deferment_periods** | **list[int]** | Integer array: Deferral time periods (hours) that users can choose from. Include up to 3. All 3 must be distinct with a maximum of 24. Default values: 1, 4, 8 | [optional] 
**custom_pending_reboot_notification_message** | **str** | Custom reboot message. | [optional] 
**custom_pending_reboot_notification_message_mac** | **str** | The custom reboot message for macOS, which overrides &#x60;custom_pending_reboot_notification_message&#x60; string, if provided. | [optional] 
**custom_pending_reboot_notification_max_delays** | **int** | Maximum number of times a user is allowed to defer the reboot. The default is 0. | [optional] [default to 0]
**custom_pending_reboot_notification_deferment_periods** | **list[int]** | The time period options available to defer a reboot for each deferral selection. Default values: 1, 4, 8 | [optional] 
**notify_user_message_timeout** | **int** | The amount of time a patch notification appears before timing out and closing. Min: 15 min. Max: 480 min. Default is 15 minutes. | [optional] [default to 15]
**notify_deferred_reboot_user_message_timeout** | **int** | The amount of time a deferrable reboot notification message appears before timing out and closing. Min: 15 min. Max: 480 min. Default is 15 minutes. | [optional] [default to 15]
**notify_user_auto_deferral_enabled** | **bool** | If a patch notification times out, apply the highest configured patch deferral. | [optional] [default to False]
**notify_deferred_reboot_user_auto_deferral_enabled** | **bool** | If a reboot notification times out, apply the highest configured reboot deferral. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

