# openapi_client.BiblesApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_bible_all**](BiblesApi.md#v4_bible_all) | **GET** /bibles | Returns Bibles based on filter criteria
[**v4_bible_books**](BiblesApi.md#v4_bible_books) | **GET** /bibles/{id}/book | Book information for a Bible
[**v4_bible_by_id_search**](BiblesApi.md#v4_bible_by_id_search) | **GET** /bibles/search | Returns metadata for all bibles meeting the given version in it&#39;s Bible ID
[**v4_bible_copyright**](BiblesApi.md#v4_bible_copyright) | **GET** /bibles/{bible_id}/copyright | Bible Copyright information
[**v4_bible_defaults**](BiblesApi.md#v4_bible_defaults) | **GET** /bibles/defaults/types | Default Bible for a language
[**v4_bible_filesets_show_chapter**](BiblesApi.md#v4_bible_filesets_show_chapter) | **GET** /bibles/filesets/{fileset_id}/{book}/{chapter} | Returns content for a single fileset, book and chapter
[**v4_bible_filesets_types**](BiblesApi.md#v4_bible_filesets_types) | **GET** /bibles/filesets/media/types | Available fileset types
[**v4_bible_one**](BiblesApi.md#v4_bible_one) | **GET** /bibles/{id} | Returns detailed metadata for a single Bible
[**v4_bible_search**](BiblesApi.md#v4_bible_search) | **GET** /bibles/search/{search_text} | Returns metadata for all bibles meeting the search_text in it&#39;s name
[**v4_download**](BiblesApi.md#v4_download) | **GET** /download/{fileset_id}/{book_id}/{chapter} | Download specific fileset
[**v4_download_list**](BiblesApi.md#v4_download_list) | **GET** /download/list | List of filesets which can be downloaded for this API key
[**v4_timestamps_verse**](BiblesApi.md#v4_timestamps_verse) | **GET** /timestamps/{fileset_id}/{book}/{chapter} | Returns audio timestamps for a chapter


# **v4_bible_all**
> V4BibleAll v4_bible_all(v, language_code=language_code, media=media, media_exclude=media_exclude, country=country, audio_timing=audio_timing, page=page, limit=limit)

Returns Bibles based on filter criteria

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
    api_instance = openapi_client.BiblesApi(api_client)
    v = 4 # int | The Version Number
language_code = openapi_client.Iso() # Iso | The iso code to filter results by. This will return results only in the language specified. For a complete list see the `iso` field in the `/languages` route (optional)
media = openapi_client.SetTypeCode() # SetTypeCode | Will filter bibles based upon the media type of their filesets (optional)
media_exclude = openapi_client.SetTypeCode() # SetTypeCode | Will exclude bibles based upon the media type of their filesets (optional)
country = openapi_client.Id() # Id | The iso code to filter results by. This will return results only in the language specified. For a complete list see the `iso` field in the `/country` route (optional)
audio_timing = False # bool | This will return results only which have audio timing information available for that bible. The timing information is stored in table bible_file_timestamps. (optional) (default to False)
page = 1 # int | The current page of the results (optional) (default to 1)
limit = 25 # int | The number of search results to return (optional) (default to 25)

    try:
        # Returns Bibles based on filter criteria
        api_response = api_instance.v4_bible_all(v, language_code=language_code, media=media, media_exclude=media_exclude, country=country, audio_timing=audio_timing, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiblesApi->v4_bible_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v** | **int**| The Version Number | 
 **language_code** | [**Iso**](.md)| The iso code to filter results by. This will return results only in the language specified. For a complete list see the &#x60;iso&#x60; field in the &#x60;/languages&#x60; route | [optional] 
 **media** | [**SetTypeCode**](.md)| Will filter bibles based upon the media type of their filesets | [optional] 
 **media_exclude** | [**SetTypeCode**](.md)| Will exclude bibles based upon the media type of their filesets | [optional] 
 **country** | [**Id**](.md)| The iso code to filter results by. This will return results only in the language specified. For a complete list see the &#x60;iso&#x60; field in the &#x60;/country&#x60; route | [optional] 
 **audio_timing** | **bool**| This will return results only which have audio timing information available for that bible. The timing information is stored in table bible_file_timestamps. | [optional] [default to False]
 **page** | **int**| The current page of the results | [optional] [default to 1]
 **limit** | **int**| The number of search results to return | [optional] [default to 25]

### Return type

[**V4BibleAll**](V4BibleAll.md)

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

# **v4_bible_books**
> V4BibleBooks v4_bible_books(id, v, book_id=book_id, verify_content=verify_content, verse_count=verse_count)

Book information for a Bible

Returns a list of translated book names and general information for the given Bible. The actual list of books may vary from fileset to fileset. For example, a King James Fileset may contain deuterocanonical books that are missing from one of it's sibling filesets nested within the bible parent.

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
    api_instance = openapi_client.BiblesApi(api_client)
    id = openapi_client.Id() # Id | 
v = 4 # int | The Version Number
book_id = openapi_client.Id() # Id | The book id. For a complete list see the `book_id` field in the `/bibles/books` route. (optional)
verify_content = True # bool | Filter all the books that have content (optional)
verse_count = True # bool | Retrieve how many verses the chapters of the books have (optional)

    try:
        # Book information for a Bible
        api_response = api_instance.v4_bible_books(id, v, book_id=book_id, verify_content=verify_content, verse_count=verse_count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiblesApi->v4_bible_books: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id**](.md)|  | 
 **v** | **int**| The Version Number | 
 **book_id** | [**Id**](.md)| The book id. For a complete list see the &#x60;book_id&#x60; field in the &#x60;/bibles/books&#x60; route. | [optional] 
 **verify_content** | **bool**| Filter all the books that have content | [optional] 
 **verse_count** | **bool**| Retrieve how many verses the chapters of the books have | [optional] 

### Return type

[**V4BibleBooks**](V4BibleBooks.md)

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

# **v4_bible_by_id_search**
> list[object] v4_bible_by_id_search(version, v)

Returns metadata for all bibles meeting the given version in it's Bible ID

metadata for all bibles meeting the version in it's Bible ID

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
    api_instance = openapi_client.BiblesApi(api_client)
    version = openapi_client.Id() # Id | 
v = 4 # int | The Version Number

    try:
        # Returns metadata for all bibles meeting the given version in it's Bible ID
        api_response = api_instance.v4_bible_by_id_search(version, v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiblesApi->v4_bible_by_id_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**Id**](.md)|  | 
 **v** | **int**| The Version Number | 

### Return type

**list[object]**

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

# **v4_bible_copyright**
> list[V4BibleFilesetsCopyright] v4_bible_copyright(bible_id, v, iso=iso)

Bible Copyright information

All bible fileset's copyright information and organizational connections

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
    api_instance = openapi_client.BiblesApi(api_client)
    bible_id = openapi_client.Id() # Id | The Bible ID to retrieve the copyright information for
v = 4 # int | The Version Number
iso = openapi_client.Iso() # Iso | The iso code to filter organization translations by. For a complete list see the `iso` field in the `/languages` route. (optional)

    try:
        # Bible Copyright information
        api_response = api_instance.v4_bible_copyright(bible_id, v, iso=iso)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiblesApi->v4_bible_copyright: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bible_id** | [**Id**](.md)| The Bible ID to retrieve the copyright information for | 
 **v** | **int**| The Version Number | 
 **iso** | [**Iso**](.md)| The iso code to filter organization translations by. For a complete list see the &#x60;iso&#x60; field in the &#x60;/languages&#x60; route. | [optional] 

### Return type

[**list[V4BibleFilesetsCopyright]**](V4BibleFilesetsCopyright.md)

### Authorization

[dbp_key](../README.md#dbp_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested bible copyrights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_bible_defaults**
> V4BiblesDefaults v4_bible_defaults(v, language_code=language_code)

Default Bible for a language

Returns default Bible for a language

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
    api_instance = openapi_client.BiblesApi(api_client)
    v = 4 # int | The Version Number
language_code = 'en' # str | The language code to filter results by (optional)

    try:
        # Default Bible for a language
        api_response = api_instance.v4_bible_defaults(v, language_code=language_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiblesApi->v4_bible_defaults: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v** | **int**| The Version Number | 
 **language_code** | **str**| The language code to filter results by | [optional] 

### Return type

[**V4BiblesDefaults**](V4BiblesDefaults.md)

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

# **v4_bible_filesets_show_chapter**
> object v4_bible_filesets_show_chapter(fileset_id, book, chapter, v, verse_start=verse_start, verse_end=verse_end)

Returns content for a single fileset, book and chapter

For a given fileset, book and chapter, return content (text, audio or video)

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
    api_instance = openapi_client.BiblesApi(api_client)
    fileset_id = openapi_client.Id() # Id | The fileset ID
book = openapi_client.Id() # Id | Will filter the results by the given book. For a complete list see the `book_id` field in the `/bibles/books` route.
chapter = openapi_client.ChapterStart() # ChapterStart | Will filter the results by the given chapter
v = 4 # int | The Version Number
verse_start = openapi_client.VerseStart() # VerseStart | Will filter the results by the given starting verse (optional)
verse_end = openapi_client.VerseEnd() # VerseEnd | Will filter the results by the given ending verse (optional)

    try:
        # Returns content for a single fileset, book and chapter
        api_response = api_instance.v4_bible_filesets_show_chapter(fileset_id, book, chapter, v, verse_start=verse_start, verse_end=verse_end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiblesApi->v4_bible_filesets_show_chapter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileset_id** | [**Id**](.md)| The fileset ID | 
 **book** | [**Id**](.md)| Will filter the results by the given book. For a complete list see the &#x60;book_id&#x60; field in the &#x60;/bibles/books&#x60; route. | 
 **chapter** | [**ChapterStart**](.md)| Will filter the results by the given chapter | 
 **v** | **int**| The Version Number | 
 **verse_start** | [**VerseStart**](.md)| Will filter the results by the given starting verse | [optional] 
 **verse_end** | [**VerseEnd**](.md)| Will filter the results by the given ending verse | [optional] 

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

# **v4_bible_filesets_types**
> object v4_bible_filesets_types(v)

Available fileset types

A list of all the file types that exist within the filesets

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
    api_instance = openapi_client.BiblesApi(api_client)
    v = 4 # int | The Version Number

    try:
        # Available fileset types
        api_response = api_instance.v4_bible_filesets_types(v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiblesApi->v4_bible_filesets_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v** | **int**| The Version Number | 

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

# **v4_bible_one**
> list[object] v4_bible_one(id, v, UNKNOWN_PARAMETER_NAME=UNKNOWN_PARAMETER_NAME)

Returns detailed metadata for a single Bible

Detailed information for a single Bible

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
    api_instance = openapi_client.BiblesApi(api_client)
    id = openapi_client.Id() # Id | 
v = 4 # int | The Version Number
UNKNOWN_PARAMETER_NAME = openapi_client.null() #  |  (optional)

    try:
        # Returns detailed metadata for a single Bible
        api_response = api_instance.v4_bible_one(id, v, UNKNOWN_PARAMETER_NAME=UNKNOWN_PARAMETER_NAME)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiblesApi->v4_bible_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id**](.md)|  | 
 **v** | **int**| The Version Number | 
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 

### Return type

**list[object]**

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

# **v4_bible_search**
> list[object] v4_bible_search(search_text, v)

Returns metadata for all bibles meeting the search_text in it's name

metadata for all bibles meeting the search_text in it's name

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
    api_instance = openapi_client.BiblesApi(api_client)
    search_text = openapi_client.Id() # Id | 
v = 4 # int | The Version Number

    try:
        # Returns metadata for all bibles meeting the search_text in it's name
        api_response = api_instance.v4_bible_search(search_text, v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiblesApi->v4_bible_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | [**Id**](.md)|  | 
 **v** | **int**| The Version Number | 

### Return type

**list[object]**

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

# **v4_download**
> object v4_download(fileset_id, book_id, chapter, v)

Download specific fileset

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
    api_instance = openapi_client.BiblesApi(api_client)
    fileset_id = openapi_client.Id() # Id | The fileset ID
book_id = openapi_client.Id() # Id | Will filter the results by the given book. For a complete list see the `book_id` field in the `/bibles/books` route.
chapter = openapi_client.ChapterStart() # ChapterStart | Will filter the results by the given chapter
v = 4 # int | The Version Number

    try:
        # Download specific fileset
        api_response = api_instance.v4_download(fileset_id, book_id, chapter, v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiblesApi->v4_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileset_id** | [**Id**](.md)| The fileset ID | 
 **book_id** | [**Id**](.md)| Will filter the results by the given book. For a complete list see the &#x60;book_id&#x60; field in the &#x60;/bibles/books&#x60; route. | 
 **chapter** | [**ChapterStart**](.md)| Will filter the results by the given chapter | 
 **v** | **int**| The Version Number | 

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

# **v4_download_list**
> object v4_download_list(v, limit=limit, page=page, type=type)

List of filesets which can be downloaded for this API key

List of filesets which can be downloaded for this API key

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
    api_instance = openapi_client.BiblesApi(api_client)
    v = 4 # int | The Version Number
limit = openapi_client.Id() # Id | The number of search results to return (optional)
page = 1 # int | The current page of the results (optional) (default to 1)
type = 'type_example' # str | Filter by type of content (audio, video, text) (optional)

    try:
        # List of filesets which can be downloaded for this API key
        api_response = api_instance.v4_download_list(v, limit=limit, page=page, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiblesApi->v4_download_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v** | **int**| The Version Number | 
 **limit** | [**Id**](.md)| The number of search results to return | [optional] 
 **page** | **int**| The current page of the results | [optional] [default to 1]
 **type** | **str**| Filter by type of content (audio, video, text) | [optional] 

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

# **v4_timestamps_verse**
> V4AudioTimestamps v4_timestamps_verse(fileset_id, book, chapter, v)

Returns audio timestamps for a chapter

This route will return timestamps for a chapter. Note that the fileset id must be available via the path `/timestamps`. At first, only a few filesets may have timestamps metadata applied.

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
    api_instance = openapi_client.BiblesApi(api_client)
    fileset_id = openapi_client.Id() # Id | The specific fileset to return references for
book = openapi_client.Id() # Id | The Book ID for which to return timestamps. For a complete list see the `book_id` field in the `/bibles/books` route.
chapter = openapi_client.ChapterStart() # ChapterStart | The chapter for which to return timestamps
v = 4 # int | The Version Number

    try:
        # Returns audio timestamps for a chapter
        api_response = api_instance.v4_timestamps_verse(fileset_id, book, chapter, v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BiblesApi->v4_timestamps_verse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileset_id** | [**Id**](.md)| The specific fileset to return references for | 
 **book** | [**Id**](.md)| The Book ID for which to return timestamps. For a complete list see the &#x60;book_id&#x60; field in the &#x60;/bibles/books&#x60; route. | 
 **chapter** | [**ChapterStart**](.md)| The chapter for which to return timestamps | 
 **v** | **int**| The Version Number | 

### Return type

[**V4AudioTimestamps**](V4AudioTimestamps.md)

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

