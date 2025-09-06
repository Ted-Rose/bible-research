# PlaylistItems

The Playlist Item
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** | If the playlist item is completed | [optional] 
**full_chapter** | **bool** | If the playlist item is a full chapter item | [optional] 
**path** | **str** | Hls path of the playlist item | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**id** | **int** | The playlist item id | [optional] 
**playlist_id** | **int** | The playlist id | [optional] 
**fileset_id** | **str** | The fileset id | [optional] 
**book_id** | **str** | The book_id | [optional] 
**chapter_start** | **int** | The chapter_start | [optional] 
**chapter_end** | **int** | If the Bible File spans multiple chapters this field indicates the last chapter of the selection | [optional] 
**verse_start** | **str** | The starting verse at which the BibleFile reference begins | [optional] 
**verse_sequence** | **int** | The starting verse at which the BibleFile reference begins | [optional] 
**verse_end** | **int** | If the Bible File spans multiple verses this value will indicate the last verse in that reference. This value is inclusive, so for the reference John 1:1-4. The value would be 4 and the reference would contain verse 4. | [optional] 
**duration** | **int** | The playlist item calculated duration | [optional] 
**verses** | **int** | The playlist item verses count | [optional] 
**updated_at** | **str** | The timestamp the playlist item was last updated at | [optional] 
**created_at** | **str** | The timestamp the playlist item was created at | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


