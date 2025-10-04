"""
Client for the Digital Bible Platform (DBT) API using the generated
OpenAPI client.
"""
import logging
import os
import sys
from typing import Dict, Optional, Any
from django.conf import settings

# Set up logging
logger = logging.getLogger(__name__)
# Add the generated client to the Python path
client_path = os.path.join(os.path.dirname(__file__), 'dbt_client')
sys.path.append(client_path)
from openapi_client.api.bibles_api import BiblesApi
from openapi_client.api.search_api import SearchApi
from openapi_client.api.annotations_api import AnnotationsApi
from openapi_client.configuration import Configuration
from openapi_client.api_client import ApiClient
from openapi_client.exceptions import ApiException


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

        api_key = getattr(settings, 'DBT_KEY')

        if not api_key:
            raise ValueError("DBT_KEY not found in settings.")

        config = Configuration(
            host="https://b4.dbt.io/api",
            api_key={'key': api_key}
        )

        self.api_client = ApiClient(config)

        self.bibles_api = BiblesApi(self.api_client)
        self.search_api = SearchApi(self.api_client)
        self.annotations_api = AnnotationsApi(self.api_client)

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

    def get_chapters(
        self,
        bible_id: str,
        book_id: str,
        **kwargs
    ) -> Dict[str, Any]:
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

    def get_verses(
        self,
        book: str,
        chapter: str,
        bible_id: str = "ENGESV",
        **kwargs
    ) -> Dict[str, Any]:
        """
        Get verses for a specific chapter.

        Args:
            bible_id: Bible ID (called fileset_id in the DBT API)
            book: Book ID
            chapter: Chapter ID
            **kwargs: Additional query parameters

        Returns:
            Dictionary with verse data
        """
        return self._make_request(
                self.bibles_api.v4_bible_filesets_show_chapter,
                bible_id,
                book,
                chapter,
                **kwargs
            )

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
