"""
Client for the Digital Bible Platform (DBT) API using the generated
OpenAPI client.
"""
import os
import sys
import logging
from typing import Dict, Optional, Any
from django.conf import settings

# Add the generated client to the Python path
client_path = os.path.join(os.path.dirname(__file__), 'dbt_client')
sys.path.append(client_path)

# Add missing model classes to fix OpenAPI client issues

# Base class for all missing models
class BaseModel(str):
    """Base class for missing OpenAPI models"""
    openapi_types = {}
    attribute_map = {}
    
    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model"""
        return cls(dikt)

# Id class for country codes
class Id(BaseModel):
    """Custom Id class to fix missing model in OpenAPI client."""
    pass

# Name class for names
class Name(BaseModel):
    """Custom Name class to fix missing model in OpenAPI client."""
    pass

# Iso class for language codes
class Iso(BaseModel):
    """Custom Iso class to fix missing model in OpenAPI client."""
    pass

# SetTypeCode class for media types
class SetTypeCode(BaseModel):
    """Custom SetTypeCode class to fix missing model in OpenAPI client."""
    pass

# Add the classes to the models module
import openapi_client.models
openapi_client.models.Id = Id
openapi_client.models.Name = Name
openapi_client.models.Iso = Iso
openapi_client.models.SetTypeCode = SetTypeCode

from openapi_client.api.bibles_api import BiblesApi
from openapi_client.api.search_api import SearchApi
from openapi_client.configuration import Configuration
from openapi_client.api_client import ApiClient
from openapi_client.exceptions import ApiException

logger = logging.getLogger(__name__)


class DBTClient:
    """
    Client for the Digital Bible Platform (DBT) API using the generated
    OpenAPI client. Provides a simplified interface for common operations.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the DBT client with API key.

        Args:
            api_key: The DBT API key. If not provided, will try to get from
                environment.
        """
        # Get the API key from settings or environment if not provided
        self.api_key = api_key or settings.DBT_KEY or os.environ.get("DBT_API_KEY")

        if not self.api_key:
            logger.warning("No DBT API key provided. API calls may fail.")

        # Configure the API client
        config = Configuration(
            host="https://4.dbt.io/api"
        )
        
        # Set up API key for authentication
        # The API key is set in the configuration's api_key dictionary
        # The auth_settings method will add it as a query parameter
        config.api_key['key'] = self.api_key

        # Create API client
        self.api_client = ApiClient(config)

        # Initialize API interfaces
        self.bibles_api = BiblesApi(self.api_client)
        self.search_api = SearchApi(self.api_client)

    def _make_request(self, request_func, *args, **kwargs):
        """
        Make a request to the DBT API with error handling.

        Args:
            request_func: Function to call
            *args: Arguments to pass to the function
            **kwargs: Additional query parameters

        Returns:
            API response data
        """
        # Ensure version is set
        if 'v' not in kwargs:
            kwargs['v'] = 4
            
        # Do not add 'key' parameter directly
        # The OpenAPI client will handle adding the API key as a query parameter
        # through the auth_settings mechanism in api_client.py
            
        try:
            response = request_func(*args, **kwargs)
            return response
        except ApiException as e:
            logger.error(f"API error: {e}")
            if e.status == 401:
                logger.error("Authentication failed. Check your API key.")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
    
    # Bible endpoints

    def get_bibles(self, language: str = None, **kwargs) -> Dict[str, Any]:
        """
        Get available Bibles, optionally filtered by language.

        Args:
            language: ISO 639-3 language code (optional)
            **kwargs: Additional query parameters

        Returns:
            Dictionary with Bible data
        """
        if language:
            kwargs['language_code'] = language
        return self._make_request(self.bibles_api.v4_bible_all, **kwargs)
    
    def get_bible(self, bible_id: str, **kwargs) -> Dict[str, Any]:
        """
        Get details for a specific Bible.

        Args:
            bible_id: Bible ID
            **kwargs: Additional query parameters

        Returns:
            Dictionary with Bible details
        """
        return self._make_request(
            self.bibles_api.v4_bible_one,
            bible_id,
            **kwargs
        )
    
    def get_books(self, bible_id: str, **kwargs) -> Dict[str, Any]:
        """
        Get books for a specific Bible.

        Args:
            bible_id: Bible ID
            **kwargs: Additional query parameters

        Returns:
            Dictionary with book data
        """
        return self._make_request(
            self.bibles_api.v4_bible_books,
            bible_id,
            **kwargs
        )
    
    def get_book(self, bible_id: str, book_id: str, **kwargs) -> Dict[str, Any]:
        """
        Get details for a specific book.

        Args:
            bible_id: Bible ID
            book_id: Book ID
            **kwargs: Additional query parameters

        Returns:
            Dictionary with book details
        """
        # Note: There is no direct endpoint for a specific book
        # Use v4_bible_books and filter the results
        books = self._make_request(
            self.bibles_api.v4_bible_books,
            bible_id,
            **kwargs
        )
        if 'data' in books:
            for book in books['data']:
                if book.get('id') == book_id:
                    return {'data': book}
        return {'data': None}
    
    def get_chapters(self, bible_id: str, book_id: str, **kwargs) -> Dict[str, Any]:
        """
        Get chapters for a specific book.

        Args:
            bible_id: Bible ID
            book_id: Book ID
            **kwargs: Additional query parameters

        Returns:
            Dictionary with chapter data
        """
        # Note: Need to get the chapters from the book endpoint
        books = self._make_request(
            self.bibles_api.v4_bible_books,
            bible_id,
            **kwargs
        )
        if 'data' in books:
            for book in books['data']:
                if book.get('id') == book_id and 'chapters' in book:
                    return {'data': book['chapters']}
        return {'data': []}
    
    def get_verses(self, bible_id: str, chapter_id: str, **kwargs) -> Dict[str, Any]:
        """
        Get verses for a specific chapter.

        Args:
            bible_id: Bible ID
            chapter_id: Chapter ID
            **kwargs: Additional query parameters

        Returns:
            Dictionary with verse data
        """
        # In the API, we need to use the fileset ID
        # We'll assume bible_id is the fileset_id for now
        # And chapter_id is in the format 'BOOK.CHAPTER', e.g., 'GEN.1'
        if '.' in chapter_id:
            book, chapter = chapter_id.split('.')
            return self._make_request(
                self.bibles_api.v4_bible_filesets_show_chapter,
                bible_id,  # Using bible_id as fileset_id
                book,
                chapter,
                **kwargs
            )
        else:
            logger.error(f"Invalid chapter_id format: {chapter_id}. Expected format: 'BOOK.CHAPTER'")
            return {'data': []}
    
    def search(self, bible_id: str, query: str, **kwargs) -> Dict[str, Any]:
        """
        Search for text in a specific Bible.

        Args:
            bible_id: Bible ID
            query: Search query
            **kwargs: Additional query parameters

        Returns:
            Dictionary with search results
        """
        return self._make_request(
            self.search_api.v4_text_search,
            query=query,
            fileset_id=bible_id,
            **kwargs
        )
