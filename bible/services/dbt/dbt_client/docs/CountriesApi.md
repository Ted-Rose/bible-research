# openapi_client.CountriesApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_countries_all**](CountriesApi.md#v4_countries_all) | **GET** /countries | Returns Countries
[**v4_countries_one**](CountriesApi.md#v4_countries_one) | **GET** /countries/{id} | Returns details for a single Country
[**v4_countries_search**](CountriesApi.md#v4_countries_search) | **GET** /countries/search/{search_text} | Returns Countries


# **v4_countries_all**
> V4CountriesAll v4_countries_all(v, l10n=l10n, include_languages=include_languages)

Returns Countries

Returns the List of Countries

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
    api_instance = openapi_client.CountriesApi(api_client)
    v = 4 # int | The Version Number
l10n = openapi_client.Iso() # Iso | When set to a valid three letter language iso, the returning results will be localized in the language matching that iso. (If an applicable translation exists). For a complete list see the `iso` field in the `/languages` route (optional)
include_languages = True # bool | When set to true, the return will include the major languages used in each country.  (optional)

    try:
        # Returns Countries
        api_response = api_instance.v4_countries_all(v, l10n=l10n, include_languages=include_languages)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CountriesApi->v4_countries_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v** | **int**| The Version Number | 
 **l10n** | [**Iso**](.md)| When set to a valid three letter language iso, the returning results will be localized in the language matching that iso. (If an applicable translation exists). For a complete list see the &#x60;iso&#x60; field in the &#x60;/languages&#x60; route | [optional] 
 **include_languages** | **bool**| When set to true, the return will include the major languages used in each country.  | [optional] 

### Return type

[**V4CountriesAll**](V4CountriesAll.md)

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

# **v4_countries_one**
> V4CountriesOne v4_countries_one(id, v)

Returns details for a single Country

Returns details for a single Country

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
    api_instance = openapi_client.CountriesApi(api_client)
    id = openapi_client.Id() # Id | 
v = 4 # int | The Version Number

    try:
        # Returns details for a single Country
        api_response = api_instance.v4_countries_one(id, v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CountriesApi->v4_countries_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id**](.md)|  | 
 **v** | **int**| The Version Number | 

### Return type

[**V4CountriesOne**](V4CountriesOne.md)

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

# **v4_countries_search**
> v4_countries_search(search_text, v)

Returns Countries

Returns the List of Countries filtered by names

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
    api_instance = openapi_client.CountriesApi(api_client)
    search_text = openapi_client.IsoA3() # IsoA3 | Search countries by name
v = 4 # int | The Version Number

    try:
        # Returns Countries
        api_instance.v4_countries_search(search_text, v)
    except ApiException as e:
        print("Exception when calling CountriesApi->v4_countries_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | [**IsoA3**](.md)| Search countries by name | 
 **v** | **int**| The Version Number | 

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

