# Account

The Account Model describes the connections between Users and their social accounts
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The incrementing ID for the account | [optional] 
**user_id** | **str** | The user id for the user who has the account being described | [optional] 
**provider_id** | **str** | The social account provider that the user has logged in with | [optional] 
**provider_user_id** | **str** | The key of the provider for the account being described | [optional] 
**created_at** | **str** | The time the social account was originally connected to the user | [optional] 
**updated_at** | **str** | The time the social account was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


