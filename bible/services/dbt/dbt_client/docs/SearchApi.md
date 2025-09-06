# openapi_client.SearchApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_text_search**](SearchApi.md#v4_text_search) | **GET** /search | Search a bible for a word


# **v4_text_search**
> V4TextSearch v4_text_search(query, fileset_id, v, limit=limit, page=page, sort_by=sort_by, books=books)

Search a bible for a word

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
    api_instance = openapi_client.SearchApi(api_client)
    query = 'Jesus' # str | The word or phrase being searched
fileset_id = openapi_client.Id() # Id | The Bible fileset ID
v = 4 # int | The Version Number
limit = 15 # int | The number of search results to return (optional) (default to 15)
page = 1 # int | The current page of the results (optional) (default to 1)
sort_by = 'sort_by_example' # str | The field to sort by (optional)
books = 'GEN,EXO,MAT' # str | The usfm book ids to search through separated by a comma (optional)

    try:
        # Search a bible for a word
        api_response = api_instance.v4_text_search(query, fileset_id, v, limit=limit, page=page, sort_by=sort_by, books=books)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SearchApi->v4_text_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The word or phrase being searched | 
 **fileset_id** | [**Id**](.md)| The Bible fileset ID | 
 **v** | **int**| The Version Number | 
 **limit** | **int**| The number of search results to return | [optional] [default to 15]
 **page** | **int**| The current page of the results | [optional] [default to 1]
 **sort_by** | **str**| The field to sort by | [optional] 
 **books** | **str**| The usfm book ids to search through separated by a comma | [optional] 

### Return type

[**V4TextSearch**](V4TextSearch.md)

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

