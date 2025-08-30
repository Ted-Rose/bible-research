# openapi_client.LanguagesApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_alphabets_all**](LanguagesApi.md#v4_alphabets_all) | **GET** /alphabets | Returns Alphabets
[**v4_alphabets_one**](LanguagesApi.md#v4_alphabets_one) | **GET** /alphabets/{script_id} | Return details on a single Alphabet
[**v4_languages_all**](LanguagesApi.md#v4_languages_all) | **GET** /languages | Returns Languages
[**v4_languages_one**](LanguagesApi.md#v4_languages_one) | **GET** /languages/{id} | Returns details on a single Language
[**v4_languages_search**](LanguagesApi.md#v4_languages_search) | **GET** /languages/search/{search_text} | Returns languages related to this search
[**v4_numbers_index**](LanguagesApi.md#v4_numbers_index) | **GET** /numbers | Return all Alphabets that have a custom number sets
[**v4_numbers_range**](LanguagesApi.md#v4_numbers_range) | **GET** /numbers/range | Return a range of vernacular numbers
[**v4_numbers_show**](LanguagesApi.md#v4_numbers_show) | **GET** /numbers/{id} | Return a single custom number set


# **v4_alphabets_all**
> V4AlphabetsAllResponse v4_alphabets_all(v)

Returns Alphabets

Returns a list of the world's known scripts. This route might be useful to you if you'd like to query information about fonts, alphabets, and the world's writing systems. Some fileset returns may not display correctly without a font delivered by these via the `alphabets/{script_id}` routes.

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
    api_instance = openapi_client.LanguagesApi(api_client)
    v = 4 # int | The Version Number

    try:
        # Returns Alphabets
        api_response = api_instance.v4_alphabets_all(v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanguagesApi->v4_alphabets_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v** | **int**| The Version Number | 

### Return type

[**V4AlphabetsAllResponse**](V4AlphabetsAllResponse.md)

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

# **v4_alphabets_one**
> V4AlphabetsOneResponse v4_alphabets_one(script_id, v)

Return details on a single Alphabet

Returns a single alphabet along with whatever bibles and languages using it.

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
    api_instance = openapi_client.LanguagesApi(api_client)
    script_id = openapi_client.Script() # Script | The alphabet Script, which is used as the identifier
v = 4 # int | The Version Number

    try:
        # Return details on a single Alphabet
        api_response = api_instance.v4_alphabets_one(script_id, v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanguagesApi->v4_alphabets_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | [**Script**](.md)| The alphabet Script, which is used as the identifier | 
 **v** | **int**| The Version Number | 

### Return type

[**V4AlphabetsOneResponse**](V4AlphabetsOneResponse.md)

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

# **v4_languages_all**
> V4LanguagesAll v4_languages_all(v, country=country, language_code=language_code, language_name=language_name, include_translations=include_translations, l10n=l10n, page=page, limit=limit)

Returns Languages

Returns the List of Languages

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
    api_instance = openapi_client.LanguagesApi(api_client)
    v = 4 # int | The Version Number
country = openapi_client.Id() # Id | The ISO Country Code. For a complete list of Country codes,  please refer to the ISO Registration Authority. https://www.iso.org/iso-3166-country-codes.html (optional)
language_code = openapi_client.Iso() # Iso | The iso code to filter languages by. For a complete list see the `iso` field in the `/languages` route (optional)
language_name = openapi_client.Iso() # Iso | The language_name field will filter results by a specific language name (optional)
include_translations = True # bool | Include the ISO language ids for available translations (optional)
l10n = openapi_client.Iso() # Iso | When set to a valid three letter language iso, the returning results will be localized in the language matching that iso. (If an applicable translation exists). For a complete list see the `iso` field in the `/languages` route (optional)
page = 1 # int | The current page of the results (optional) (default to 1)
limit = 25 # int | The number of search results to return (optional) (default to 25)

    try:
        # Returns Languages
        api_response = api_instance.v4_languages_all(v, country=country, language_code=language_code, language_name=language_name, include_translations=include_translations, l10n=l10n, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanguagesApi->v4_languages_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v** | **int**| The Version Number | 
 **country** | [**Id**](.md)| The ISO Country Code. For a complete list of Country codes,  please refer to the ISO Registration Authority. https://www.iso.org/iso-3166-country-codes.html | [optional] 
 **language_code** | [**Iso**](.md)| The iso code to filter languages by. For a complete list see the &#x60;iso&#x60; field in the &#x60;/languages&#x60; route | [optional] 
 **language_name** | [**Iso**](.md)| The language_name field will filter results by a specific language name | [optional] 
 **include_translations** | **bool**| Include the ISO language ids for available translations | [optional] 
 **l10n** | [**Iso**](.md)| When set to a valid three letter language iso, the returning results will be localized in the language matching that iso. (If an applicable translation exists). For a complete list see the &#x60;iso&#x60; field in the &#x60;/languages&#x60; route | [optional] 
 **page** | **int**| The current page of the results | [optional] [default to 1]
 **limit** | **int**| The number of search results to return | [optional] [default to 25]

### Return type

[**V4LanguagesAll**](V4LanguagesAll.md)

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

# **v4_languages_one**
> V4LanguagesOne v4_languages_one(id, v)

Returns details on a single Language

Returns details on a single Language

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
    api_instance = openapi_client.LanguagesApi(api_client)
    id = openapi_client.Id() # Id | The language ID
v = 4 # int | The Version Number

    try:
        # Returns details on a single Language
        api_response = api_instance.v4_languages_one(id, v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanguagesApi->v4_languages_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id**](.md)| The language ID | 
 **v** | **int**| The Version Number | 

### Return type

[**V4LanguagesOne**](V4LanguagesOne.md)

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

# **v4_languages_search**
> V4LanguagesOne v4_languages_search(search_text, v)

Returns languages related to this search

Returns paginated languages that have search text in its name or country

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
    api_instance = openapi_client.LanguagesApi(api_client)
    search_text = openapi_client.Name() # Name | The language text to search by
v = 4 # int | The Version Number

    try:
        # Returns languages related to this search
        api_response = api_instance.v4_languages_search(search_text, v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanguagesApi->v4_languages_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | [**Name**](.md)| The language text to search by | 
 **v** | **int**| The Version Number | 

### Return type

[**V4LanguagesOne**](V4LanguagesOne.md)

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

# **v4_numbers_index**
> V4NumbersIndex v4_numbers_index(v)

Return all Alphabets that have a custom number sets

Returns a range of numbers

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
    api_instance = openapi_client.LanguagesApi(api_client)
    v = 4 # int | The Version Number

    try:
        # Return all Alphabets that have a custom number sets
        api_response = api_instance.v4_numbers_index(v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanguagesApi->v4_numbers_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v** | **int**| The Version Number | 

### Return type

[**V4NumbersIndex**](V4NumbersIndex.md)

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

# **v4_numbers_range**
> V4NumbersRange v4_numbers_range(script_id, start, end, v)

Return a range of vernacular numbers

This route returns the vernacular numbers for a set range.

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
    api_instance = openapi_client.LanguagesApi(api_client)
    script_id = openapi_client.Id() # Id | The script_id to return numbers for
start = 1 # int | The start of the range to select for
end = 2 # int | The end of the range to select for
v = 4 # int | The Version Number

    try:
        # Return a range of vernacular numbers
        api_response = api_instance.v4_numbers_range(script_id, start, end, v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanguagesApi->v4_numbers_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | [**Id**](.md)| The script_id to return numbers for | 
 **start** | **int**| The start of the range to select for | 
 **end** | **int**| The end of the range to select for | 
 **v** | **int**| The Version Number | 

### Return type

[**V4NumbersRange**](V4NumbersRange.md)

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

# **v4_numbers_show**
> V4NumbersShow v4_numbers_show(id, v)

Return a single custom number set

Returns a range of numbers

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
    api_instance = openapi_client.LanguagesApi(api_client)
    id = openapi_client.Id() # Id | The NumeralSystem id
v = 4 # int | The Version Number

    try:
        # Return a single custom number set
        api_response = api_instance.v4_numbers_show(id, v)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanguagesApi->v4_numbers_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id**](.md)| The NumeralSystem id | 
 **v** | **int**| The Version Number | 

### Return type

[**V4NumbersShow**](V4NumbersShow.md)

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

