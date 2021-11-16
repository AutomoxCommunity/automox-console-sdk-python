# PatchPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** | Organization ID for the specified policy | 
**name** | **str** | The name of the policy. | 
**policy_type_name** | **str** | The name of the type of policy you are creating. Optional when updating an existing policy. | 
**configuration** | **OneOfPatchPolicyConfiguration** | The policy configuration. This varies depending on the type of policy being used. | 
**schedule_days** | **int** | Decimal value of binary day schedule. See [Policy and Device Filters, and Scheduling - Example Days per Week](/developer-portal/policy_filters_schedule/#example-days-per-week). | 
**schedule_weeks_of_month** | **int** | Decimal value of binary week schedule. See [Policy and Device Filters, and Scheduling - Example Weeks per Month](/developer-portal/policy_filters_schedule/#example-weeks-per-month). | [optional] 
**schedule_months** | **int** | Decimal value of binary month schedule. See [Policy and Device Filters, and Scheduling - Example Months per Year](/developer-portal/policy_filters_schedule/#example-months-per-year). | [optional] 
**schedule_time** | **str** | Scheduled time for automatic policy execution. Format: &#x60;\&quot;hh:mm\&quot;&#x60; | 
**next_remediation** | **datetime** | The date and time the next remediation will be executed for the policy. | [optional] 
**server_groups** | **list[int]** | An array containing a list of the server group IDs to be affected by the policy. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
