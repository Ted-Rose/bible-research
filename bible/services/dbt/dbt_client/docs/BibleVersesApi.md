# openapi_client.BibleVersesApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_bible_verses_verse_by_bible**](BibleVersesApi.md#v4_bible_verses_verse_by_bible) | **GET** /bible/{bible_id}/verses/{book_id}/{chapter_id}/{verse_number?} | Returns Bibles Verses based on filter criteria
[**v4_bible_verses_verse_by_language**](BibleVersesApi.md#v4_bible_verses_verse_by_language) | **GET** /bibles/verses/{language_code}/{book_id}/{chapter_id}/{verse_number?} | Returns Bibles Verses based on filter criteria


# **v4_bible_verses_verse_by_bible**
> V4BibleVersesAll v4_bible_verses_verse_by_bible(bible_id, book_id, chapter, verse_number, v, page=page, limit=limit)

Returns Bibles Verses based on filter criteria

The base bible route returning by default bibles and filesets that your key has access to

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
    api_instance = openapi_client.BibleVersesApi(api_client)
    bible_id = openapi_client.Id() # Id | The Bible ID to filter bible_verses by
book_id = openapi_client.Id() # Id | The book to filter bible_verses by
chapter = openapi_client.Chapter() # Chapter | The chapter to filter bible_verses by
verse_number = openapi_client.VerseNumber() # VerseNumber | The verse start to filter bible_verses by
v = 4 # int | The Version Number
page = 1 # int | The current page of the results (optional) (default to 1)
limit = 25 # int | The number of search results to return (optional) (default to 25)

    try:
        # Returns Bibles Verses based on filter criteria
        api_response = api_instance.v4_bible_verses_verse_by_bible(bible_id, book_id, chapter, verse_number, v, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BibleVersesApi->v4_bible_verses_verse_by_bible: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bible_id** | [**Id**](.md)| The Bible ID to filter bible_verses by | 
 **book_id** | [**Id**](.md)| The book to filter bible_verses by | 
 **chapter** | [**Chapter**](.md)| The chapter to filter bible_verses by | 
 **verse_number** | [**VerseNumber**](.md)| The verse start to filter bible_verses by | 
 **v** | **int**| The Version Number | 
 **page** | **int**| The current page of the results | [optional] [default to 1]
 **limit** | **int**| The number of search results to return | [optional] [default to 25]

### Return type

[**V4BibleVersesAll**](V4BibleVersesAll.md)

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

# **v4_bible_verses_verse_by_language**
> V4BibleVersesAll v4_bible_verses_verse_by_language(language_code, book_id, chapter, verse_number, v, page=page, limit=limit)

Returns Bibles Verses based on filter criteria

The base bible route returning by default bibles and filesets that your key has access to

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
    api_instance = openapi_client.BibleVersesApi(api_client)
    language_code = openapi_client.Id() # Id | 
book_id = openapi_client.Id() # Id | The book to filter bible_verses by
chapter = openapi_client.Chapter() # Chapter | The chapter to filter bible_verses by
verse_number = openapi_client.VerseNumber() # VerseNumber | The verse start to filter bible_verses by
v = 4 # int | The Version Number
page = 1 # int | The current page of the results (optional) (default to 1)
limit = 25 # int | The number of search results to return (optional) (default to 25)

    try:
        # Returns Bibles Verses based on filter criteria
        api_response = api_instance.v4_bible_verses_verse_by_language(language_code, book_id, chapter, verse_number, v, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BibleVersesApi->v4_bible_verses_verse_by_language: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | [**Id**](.md)|  | 
 **book_id** | [**Id**](.md)| The book to filter bible_verses by | 
 **chapter** | [**Chapter**](.md)| The chapter to filter bible_verses by | 
 **verse_number** | [**VerseNumber**](.md)| The verse start to filter bible_verses by | 
 **v** | **int**| The Version Number | 
 **page** | **int**| The current page of the results | [optional] [default to 1]
 **limit** | **int**| The number of search results to return | [optional] [default to 25]

### Return type

[**V4BibleVersesAll**](V4BibleVersesAll.md)

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

