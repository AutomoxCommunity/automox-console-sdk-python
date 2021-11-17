# CustomPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Policy ID | [optional] 
**name** | **str** |  | 
**organization_id** | **int** | Organization ID for the specified policy | 
**policy_type_name** | **str** |  | [default to 'custom']
**configuration** | [**CustomPolicyConfiguration**](CustomPolicyConfiguration.md) |  | 
**schedule_days** | **int** | Decimal value of binary day schedule. See [Policy and Device Filters, and Scheduling - Example Days per Week](/developer-portal/policy_filters_schedule/#example-days-per-week). | 
**schedule_weeks_of_month** | **int** | Decimal value of binary week schedule. See [Policy and Device Filters, and Scheduling - Example Weeks per Month](/developer-portal/policy_filters_schedule/#example-weeks-per-month). | [optional] 
**schedule_months** | **int** | Decimal value of binary month schedule. See [Policy and Device Filters, and Scheduling - Example Months per Year](/developer-portal/policy_filters_schedule/#example-months-per-year). | [optional] 
**schedule_time** | **str** | Scheduled time for automatic policy execution. Format: &#x60;\&quot;hh:mm\&quot;&#x60; | 
**server_groups** | **list[int]** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

