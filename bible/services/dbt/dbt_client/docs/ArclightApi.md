# openapi_client.ArclightApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_video_jesus_film_languages**](ArclightApi.md#v4_video_jesus_film_languages) | **GET** /arclight/jesus-film/languages | Returns detailed metadata for a single Bible arclight


# **v4_video_jesus_film_languages**
> v4_video_jesus_film_languages(v, UNKNOWN_PARAMETER_NAME=UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2=UNKNOWN_PARAMETER_NAME2, UNKNOWN_PARAMETER_NAME2=UNKNOWN_PARAMETER_NAME2)

Returns detailed metadata for a single Bible arclight

Returns detailed metadata for a single Bible arclight

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
    api_instance = openapi_client.ArclightApi(api_client)
    v = 4 # int | The Version Number
UNKNOWN_PARAMETER_NAME = openapi_client.null() #  |  (optional)
UNKNOWN_PARAMETER_NAME2 = openapi_client.null() #  |  (optional)
UNKNOWN_PARAMETER_NAME2 = openapi_client.null() #  |  (optional)

    try:
        # Returns detailed metadata for a single Bible arclight
        api_instance.v4_video_jesus_film_languages(v, UNKNOWN_PARAMETER_NAME=UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2=UNKNOWN_PARAMETER_NAME2, UNKNOWN_PARAMETER_NAME2=UNKNOWN_PARAMETER_NAME2)
    except ApiException as e:
        print("Exception when calling ArclightApi->v4_video_jesus_film_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v** | **int**| The Version Number | 
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 

### Return type

void (empty response body)

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

