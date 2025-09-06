# openapi_client.LibraryTextApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_bible_verseinfo**](LibraryTextApi.md#v4_bible_verseinfo) | **GET** /bibles/{fileset_id}/{book}/{chapter} | Returns Signed URLs or Text


# **v4_bible_verseinfo**
> list[object] v4_bible_verseinfo(fileset_id, book, chapter, v)

Returns Signed URLs or Text

V4's base fileset route

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
    api_instance = openapi_client.LibraryTextApi(api_client)
    fileset_id = openapi_client.Id() # Id | The Bible fileset ID
book = openapi_client.Id() # Id | The Book ID. For a complete list see the `book_id` field in the `/bibles/books` route.
chapter = openapi_client.ChapterStart() # ChapterStart | The chapter number
v = 4 # int | The Version Number

    try:
        # Returns Signed URLs or Text
        api_response = api_instance.v4_bible_verseinfo(fileset_id, book, chapter, v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LibraryTextApi->v4_bible_verseinfo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileset_id** | [**Id**](.md)| The Bible fileset ID | 
 **book** | [**Id**](.md)| The Book ID. For a complete list see the &#x60;book_id&#x60; field in the &#x60;/bibles/books&#x60; route. | 
 **chapter** | [**ChapterStart**](.md)| The chapter number | 
 **v** | **int**| The Version Number | 

### Return type

**list[object]**

### Authorization

[dbp_key](../README.md#dbp_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

