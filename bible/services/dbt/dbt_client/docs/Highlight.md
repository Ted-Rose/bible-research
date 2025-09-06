# Highlight

The Highlight model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The highlight id | [optional] 
**user_id** | **str** | The user that created the highlight | [optional] 
**bible_id** | [**Id**](Id.md) |  | [optional] 
**book_id** | [**Id**](Id.md) |  | [optional] 
**chapter** | [**ChapterStart**](ChapterStart.md) |  | [optional] 
**highlighted_color** | **str** | The highlight&#39;s highlighted color in either hex, rgb, or rgba notation. | [optional] 
**verse_start** | [**VerseStart**](VerseStart.md) |  | [optional] 
**verse_sequence** | [**VerseSequence**](VerseSequence.md) |  | [optional] 
**verse_end** | [**VerseEnd**](VerseEnd.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**project_id** | [**Id**](Id.md) |  | [optional] 
**highlight_start** | **int** | The number of words from the beginning of the verse to start the highlight at. For example, if the verse Genesis 1:1 had a &#x60;highlight_start&#x60; of 4 and a highlighted_words equal to 2. The result would be: In the beginning &#x60;[God created]&#x60; the heavens and the earth. | [optional] 
**highlighted_words** | **int** | The number of words being highlighted. For example, if the verse Genesis 1:1 had a &#x60;highlight_start&#x60; of 4 and a highlighted_words equal to 2. The result would be: In the beginning &#x60;[God created]&#x60; the heavens and the earth. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


