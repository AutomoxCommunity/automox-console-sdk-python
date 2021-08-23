# PolicyConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missed_patch_window** | **bool** |  | [optional] 
**filters** | **[str]** |  | [optional] 
**filter_type** | **str** |  | [optional] 
**advanced_filter** | **[str]** |  | [optional] 
**severity_filter** | **[str]** |  | [optional] 
**include_optional** | **bool** |  | [optional] 
**notify_reboot_user** | **bool** |  | [optional] 
**notify_deferred_reboot_user** | **bool** |  | [optional] 
**custom_notification_patch_message** | **str** |  | [optional] 
**custom_notification_patch_message_mac** | **str** |  | [optional] 
**custom_notification_reboot_message** | **str** |  | [optional] 
**custom_notification_reboot_message_mac** | **str** |  | [optional] 
**custom_notification_max_delays** | **int** |  | [optional] 
**custom_notification_deferment_periods** | **[int]** |  | [optional] 
**custom_pending_reboot_notification_message** | **str** |  | [optional] 
**custom_pending_reboot_notification_message_mac** | **str** |  | [optional] 
**custom_pending_reboot_notification_max_delays** | **int** |  | [optional] 
**custom_pending_reboot_notification_deferment_periods** | **[int]** |  | [optional] 
**notify_user_message_timeout** | **int** |  | [optional]  if omitted the server will use the default value of 15
**notify_deferred_reboot_user_message_timeout** | **int** |  | [optional]  if omitted the server will use the default value of 15
**notify_user_auto_deferral_enabled** | **bool** |  | [optional] 
**notify_deferred_reboot_user_auto_deferral_enabled** | **bool** |  | [optional] 
**os_family** | **str** |  | [optional] 
**package_name** | **str** |  | [optional] 
**package_version** | **str** |  | [optional] 
**installation_code** | **str, none_type** |  | [optional] 
**test_code** | **str** |  | [optional] 
**evaluation_code** | **str, none_type** |  | [optional] 
**remediation_code** | **str, none_type** |  | [optional] 
**auto_patch** | **bool** |  | [optional] 
**notify_user** | **bool** |  | [optional] 
**auto_reboot** | **bool** |  | [optional] 
**patch_rule** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


