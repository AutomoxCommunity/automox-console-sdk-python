# Policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**PolicyConfiguration**](PolicyConfiguration.md) |  | 
**id** | **int** | The ID of the relevant policy. | [optional] 
**name** | **str** | Name of the policy | 
**notes** | **str** | Policy notes | 
**organization_id** | **int** | Organization ID for the specified policy | 
**policy_type_name** | **str** | Name for the policy type | 
**schedule_days** | **int** | Decimal value of binary day schedule. See [Policy and Device Filters, and Scheduling - Example Days per Week](/developer-portal/policy_filters_schedule/#example-days-per-week). | 
**schedule_weeks_of_month** | **int** | Decimal value of binary week schedule. See [Policy and Device Filters, and Scheduling - Example Weeks per Month](/developer-portal/policy_filters_schedule/#example-weeks-per-month). | [optional] 
**schedule_months** | **int** | Decimal value of binary month schedule. See [Policy and Device Filters, and Scheduling - Example Months per Year](/developer-portal/policy_filters_schedule/#example-months-per-year). | [optional] 
**schedule_time** | **str** | Scheduled time for automatic policy execution. Format: &#x60;\&quot;hh:mm\&quot;&#x60; | 
**next_remediation** | **datetime** |  | [optional] 
**server_groups** | **list[int]** | Integer array. Server groups to link with the policy | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

