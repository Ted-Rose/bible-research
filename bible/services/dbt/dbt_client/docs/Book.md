# Book

The Book model communicates information about the canonical books of the Bible
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The USFM 2.4 id for the books of the Bible | [optional] 
**id_usfx** | **str** | The usfx id for the books of the Bible | [optional] 
**id_osis** | **str** | The OSIS id for the books of the Bible | [optional] 
**protestant_order** | **int** | The standard book order for the &#x60;protestant_order&#x60; in ascending order from Genesis onwards | [optional] 
**testament_order** | **int** | The standard book order within a testament in ascending order from Genesis to Malachi, and Matthew to Revelations | [optional] 
**book_testament** | **str** | A short code identifying the testament containing the book | [optional] 
**book_group** | **str** | An english name for the section of books that current book can be categorized in | [optional] 
**chapters** | **list[int]** | The book&#39;s number of chapters | [optional] 
**verses** | **int** | The book&#39;s number of verses | [optional] 
**name** | **str** | The English name of the book | [optional] 
**notes** | **str** | Any archivist notes about the book | [optional] 
**description** | **str** | The book&#39;s description | [optional] 
**created_at** | **str** | The timestamp for the books creation | [optional] 
**updated_at** | **str** | The timestamp for the last update of the book | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


