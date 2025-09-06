# openapi_client.AudioTimingApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_timestamps**](AudioTimingApi.md#v4_timestamps) | **GET** /timestamps | Returns Bible Filesets which have audio timestamps
[**v4_timestamps_verse**](AudioTimingApi.md#v4_timestamps_verse) | **GET** /timestamps/{fileset_id}/{book}/{chapter} | Returns audio timestamps for a chapter


# **v4_timestamps**
> list[object] v4_timestamps(v)

Returns Bible Filesets which have audio timestamps

This call returns a list of fileset that have timestamp metadata associated with them. This data could be used to search audio bibles for a specific term, make karaoke verse & audio readings, or to jump to a specific location in an audio file.

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
    api_instance = openapi_client.AudioTimingApi(api_client)
    v = 4 # int | The Version Number

    try:
        # Returns Bible Filesets which have audio timestamps
        api_response = api_instance.v4_timestamps(v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudioTimingApi->v4_timestamps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
    api_instance = openapi_client.AudioTimingApi(api_client)
    fileset_id = openapi_client.Id() # Id | The specific fileset to return references for
book = openapi_client.Id() # Id | The Book ID for which to return timestamps. For a complete list see the `book_id` field in the `/bibles/books` route.
chapter = openapi_client.ChapterStart() # ChapterStart | The chapter for which to return timestamps
v = 4 # int | The Version Number

    try:
        # Returns audio timestamps for a chapter
        api_response = api_instance.v4_timestamps_verse(fileset_id, book, chapter, v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AudioTimingApi->v4_timestamps_verse: %s\n" % e)
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

