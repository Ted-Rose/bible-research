# openapi_client.AnnotationsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_users_download**](AnnotationsApi.md#v4_users_download) | **GET** /users/{user_id}/annotations/{bible_id}/{book_id}/{chapter} | Download annotations for specific user and bible fileset


# **v4_users_download**
> object v4_users_download(user_id, bible_id, book_id, chapter, v, notes_sort_by=notes_sort_by, bookmarks_sort_by=bookmarks_sort_by, highlights_sort_by=highlights_sort_by, sort_dir=sort_dir)

Download annotations for specific user and bible fileset

For a given fileset return content (text, audio or video)

### Example

* Api Key Authentication (dbp_key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: dbp_key
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/api",
    api_key = {
        'key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AnnotationsApi(api_client)
    user_id = openapi_client.Id() # Id | The User ID
bible_id = openapi_client.Id() # Id | Will filter the results by the given bible
book_id = openapi_client.Id() # Id | Will filter the results by the given book. For a complete list see the `book_id` field in the `/bibles/books` route.
chapter = openapi_client.ChapterStart() # ChapterStart | Will filter the results by the given chapter
v = 4 # int | The Version Number
notes_sort_by = 'notes_sort_by_example' # str | The field to sort by for the notes (optional)
bookmarks_sort_by = 'bookmarks_sort_by_example' # str | The field to sort by for the bookmarks (optional)
highlights_sort_by = 'highlights_sort_by_example' # str | The field to sort by for the highlights (optional)
sort_dir = 'sort_dir_example' # str | The direction to sort by (optional)

    try:
        # Download annotations for specific user and bible fileset
        api_response = api_instance.v4_users_download(user_id, bible_id, book_id, chapter, v, notes_sort_by=notes_sort_by, bookmarks_sort_by=bookmarks_sort_by, highlights_sort_by=highlights_sort_by, sort_dir=sort_dir)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationsApi->v4_users_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**Id**](.md)| The User ID | 
 **bible_id** | [**Id**](.md)| Will filter the results by the given bible | 
 **book_id** | [**Id**](.md)| Will filter the results by the given book. For a complete list see the &#x60;book_id&#x60; field in the &#x60;/bibles/books&#x60; route. | 
 **chapter** | [**ChapterStart**](.md)| Will filter the results by the given chapter | 
 **v** | **int**| The Version Number | 
 **notes_sort_by** | **str**| The field to sort by for the notes | [optional] 
 **bookmarks_sort_by** | **str**| The field to sort by for the bookmarks | [optional] 
 **highlights_sort_by** | **str**| The field to sort by for the highlights | [optional] 
 **sort_dir** | **str**| The direction to sort by | [optional] 

### Return type

**object**

### Authorization

[dbp_key](../README.md#dbp_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

