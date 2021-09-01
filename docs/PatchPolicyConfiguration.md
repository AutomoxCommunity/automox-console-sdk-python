# PatchPolicyConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_patch** | **bool** |  | 
**notify_user** | **bool** |  | 
**missed_patch_window** | **bool** |  | [optional] 
**auto_reboot** | **bool** |  | 
**filters** | **list[str]** |  | [optional] 
**device_filters** | [**DeviceFilters**](DeviceFilters.md) |  | [optional] 
**filter_type** | **str** |  | [optional] 
**advanced_filter** | **list[str]** |  | [optional] 
**severity_filter** | **list[str]** |  | [optional] 
**include_optional** | **bool** |  | [optional] 
**notify_reboot_user** | **bool** |  | [optional] 
**notify_deferred_reboot_user** | **bool** |  | [optional] 
**custom_notification_patch_message** | **str** |  | [optional] 
**custom_notification_patch_message_mac** | **str** |  | [optional] 
**custom_notification_reboot_message** | **str** |  | [optional] 
**custom_notification_reboot_message_mac** | **str** |  | [optional] 
**custom_notification_max_delays** | **int** |  | [optional] 
**custom_notification_deferment_periods** | **list[int]** |  | [optional] 
**custom_pending_reboot_notification_message** | **str** |  | [optional] 
**custom_pending_reboot_notification_message_mac** | **str** |  | [optional] 
**custom_pending_reboot_notification_max_delays** | **int** |  | [optional] 
**custom_pending_reboot_notification_deferment_periods** | **list[int]** |  | [optional] 
**notify_user_message_timeout** | **int** |  | [optional] [default to 15]
**notify_deferred_reboot_user_message_timeout** | **int** |  | [optional] [default to 15]
**notify_user_auto_deferral_enabled** | **bool** |  | [optional] [default to False]
**notify_deferred_reboot_user_auto_deferral_enabled** | **bool** |  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

