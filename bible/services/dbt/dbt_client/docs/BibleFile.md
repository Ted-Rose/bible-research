# BibleFile

The Bible File Model communicates information about biblical files stored in S3
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id | [optional] 
**book_id** | **str** | The book_id | [optional] 
**chapter_start** | **str** | The chapter_start | [optional] 
**verse_sequence** | **int** | The starting verse for the bible file but with format &#x3D; integer | [optional] 
**chapter_end** | **str** | If the Bible File spans multiple chapters this field indicates the last chapter of the selection | [optional] 
**verse_start** | **str** | The starting verse at which the BibleFile reference begins | [optional] 
**verse_end** | **str** | If the Bible File spans multiple verses this value will indicate the last verse in that reference. This value is inclusive, so for the reference John 1:1-4. The value would be 4 and the reference would contain verse 4. | [optional] 
**verse_text** | **str** | If the BibleFile model returns text instead of a file_name this field will contain it. | [optional] 
**file_name** | **str** | The file_name | [optional] 
**file_size** | **int** | The file size | [optional] 
**duration** | **int** | If the file has a set length of time, this field indicates that time in milliseconds | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


