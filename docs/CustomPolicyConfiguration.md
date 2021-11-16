# CustomPolicyConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_reboot** | **bool** | Enable or Disable automatic reboots following policy execution. | 
**notify_reboot_user** | **bool** | Display modified notification 15 minutes before patching. This message should inform the user that a reboot will follow patching actions. | [optional] 
**device_filters_enabled** | **bool** | Enable or disable Device Filters. | [optional] 
**device_filters** | [**DeviceFilters**](DeviceFilters.md) |  | [optional] 
**missed_patch_window** | **bool** | Enable or Disable the Missed Patch Window setting | [optional] 
**os_family** | **str** | Define the OS family of the worklet policy | [optional] 
**evaluation_code** | **str** | The evaluation code of the worklet. | [optional] 
**remediation_code** | **str** | The remediation code of the worklet. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

