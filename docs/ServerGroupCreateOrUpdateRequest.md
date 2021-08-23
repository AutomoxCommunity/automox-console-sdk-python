# ServerGroupCreateOrUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the group | 
**refresh_interval** | **int** | Frequency of device refreshes (scans) in minutes. Minimum: 360 Maximum: 1440 | 
**parent_server_group_id** | **int** | ID of the parent group Use the organization&#39;s Default Group ID to make this a top-level group. See Note: Default Group ID | 
**ui_color** | **str** | The highlight color for the group. Primarily used on the System Management view. Format: #059F1D See Note UI Color | [optional] 
**notes** | **str** | Use to define notes that are displayed while editing the policy | [optional] 
**enable_os_auto_update** | **bool** | Enforce automatic update settings Options: null: Keep Device&#39;s Setting true: Enable OS automatic updates false: Disable OS automatic updates | [optional] 
**enable_wsus** | **bool, none_type** | Enforce WSUS settings for Windows devices Options: null: Keep Device&#39;s Setting true: force WSUS false: force Windows Update | [optional] 
**wsus_server** | **str** | WSUS server address. Use with enable_wsus. Format: \&quot;https://myserver.com:8530\&quot; | [optional] 
**policies** | **[int]** | List of Policies to link to this group. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


