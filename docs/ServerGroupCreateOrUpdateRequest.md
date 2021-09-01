# ServerGroupCreateOrUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the group | 
**refresh_interval** | **int** | Frequency of device refreshes (scans) in minutes. Minimum: 360 Maximum: 1440 | 
**parent_server_group_id** | **int** | ID of the parent group Use the organization&#x27;s Default Group ID to make this a top-level group. See Note: Default Group ID | 
**ui_color** | **str** | The highlight color for the group. Primarily used on the System Management view. Format: #059F1D See Note UI Color | [optional] 
**notes** | **str** | Use to define notes that are displayed while editing the policy | [optional] 
**enable_os_auto_update** | **bool** | Enforce automatic update settings Options: null: Keep Device&#x27;s Setting true: Enable OS automatic updates false: Disable OS automatic updates | [optional] 
**enable_wsus** | **bool** | Enforce WSUS settings for Windows devices Options: null: Keep Device&#x27;s Setting true: force WSUS false: force Windows Update | [optional] 
**wsus_server** | **str** | WSUS server address. Use with enable_wsus. Format: \&quot;https://myserver.com:8530\&quot; | [optional] 
**policies** | **list[int]** | List of Policies to link to this group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

