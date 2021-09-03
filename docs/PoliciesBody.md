# PoliciesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the policy. | 
**policy_type_name** | **str** |  | 
**organization_id** | **int** | Organization ID for the specified policy | 
**schedule_days** | **int** | Decimal value of binary day schedule. See [Policy and Device Filters, and Scheduling - Example Days per Week](/developer-portal/policy_filters_schedule/#example-days-per-week). | 
**schedule_weeks_of_month** | **int** | Decimal value of binary week schedule. See [Policy and Device Filters, and Scheduling - Example Weeks per Month](/developer-portal/policy_filters_schedule/#example-weeks-per-month). | 
**schedule_months** | **int** | Decimal value of binary month schedule. See [Policy and Device Filters, and Scheduling - Example Months per Year](/developer-portal/policy_filters_schedule/#example-months-per-year). | 
**schedule_time** | **str** | Scheduled time for automatic policy execution. Format: &#x60;\&quot;hh:mm\&quot;&#x60; | 
**configuration** | [**PolicyConfiguration**](PolicyConfiguration.md) |  | 
**notify_user** | **bool** | Display notification 15 minutes before patching. | 
**notes** | **str** | Policy notes | [optional] 
**server_groups** | **list[int]** | Integer array. Server groups to link with the policy | [optional] 
**auto_patch** | **bool** | Enable or Disable automatic execution of the policy. | [optional] 
**auto_reboot** | **bool** | Enable or Disable automatic reboots following policy execution. | [optional] 
**notify_reboot_user** | **bool** | Display modified notification 15 minutes before patching. This message should inform the user that a reboot will follow patching actions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

