"""
Client for the Digital Bible Platform API (Bible Brain).
This module provides a direct interface to the DBT API using requests.
"""
import os
import json
import logging
import requests
import yaml
from typing import Dict, Optional, Any
from django.conf import settings

logger = logging.getLogger(__name__)


class DBTClientError(Exception):
    """Exception raised for DBT API client errors."""
    pass


class DBTClient:
    """
    Client for the Digital Bible Platform API (Bible Brain).
    This class provides a direct interface to the DBT API using requests.
    """

    BASE_URL = "https://4.dbt.io"

    def __init__(self):
        """
        Initialize the DBT API client.
        """
        # Load API key from config file
        config_path = os.path.join(settings.BASE_DIR, 'config.yaml')
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            self.api_key = config.get('DBT_API_KEY')

        if not self.api_key:
            raise DBTClientError("DBT API key not found in config.yaml")

        # Initialize session
        self.session = requests.Session()
        self.session.params = {'key': self.api_key, 'v': '4'}
        self.session.headers.update({
            'Accept': 'application/json',
            'User-Agent': 'BibleResearchApp/1.0'
        })

    def _make_request(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make a request to the API.

        Args:
            endpoint: The API endpoint path
            params: Query parameters

        Returns:
            The JSON response

        Raises:
            DBTClientError: If the request fails
        """
        url = f"{self.BASE_URL}/{endpoint}"
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error making request to DBT API: {e}")
            raise DBTClientError(f"Error making request to DBT API: {e}")
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON response from DBT API: {e}")
            raise DBTClientError(
                f"Error decoding JSON response from DBT API: {e}"
            )

    def get_bibles(self, language: Optional[str] = None) -> Dict[str, Any]:
        """
        Get a list of available Bibles.

        Args:
            language: Filter by language code (e.g., 'eng' for English)

        Returns:
            Dictionary containing the list of Bibles
        """
        params = {}
        if language:
            params['language'] = language
        return self._make_request('bibles', params)

    def get_bible(self, bible_id: str) -> Dict[str, Any]:
        """
        Get information about a specific Bible.

        Args:
            bible_id: The ID of the Bible

        Returns:
            Dictionary containing Bible information
        """
        return self._make_request(f'bibles/{bible_id}')

    def get_books(self, bible_id: str) -> Dict[str, Any]:
        """
        Get a list of books for a specific Bible.

        Args:
            bible_id: The ID of the Bible

        Returns:
            Dictionary containing the list of books
        """
        return self._make_request(f'bibles/{bible_id}/books')

    def get_book(self, bible_id: str, book_id: str) -> Dict[str, Any]:
        """
        Get information about a specific book.

        Args:
            bible_id: The ID of the Bible
            book_id: The ID of the book

        Returns:
            Dictionary containing book information
        """
        return self._make_request(f'bibles/{bible_id}/books/{book_id}')

    def get_chapters(self, bible_id: str, book_id: str) -> Dict[str, Any]:
        """
        Get a list of chapters for a specific book.

        Args:
            bible_id: The ID of the Bible
            book_id: The ID of the book

        Returns:
            Dictionary containing the list of chapters
        """
        return self._make_request(f'bibles/{bible_id}/books/{book_id}/chapters')

    def get_chapter(self, bible_id: str, chapter_id: str) -> Dict[str, Any]:
        """
        Get information about a specific chapter.

        Args:
            bible_id: The ID of the Bible
            chapter_id: The ID of the chapter

        Returns:
            Dictionary containing chapter information
        """
        return self._make_request(f'bibles/{bible_id}/chapters/{chapter_id}')

    def get_verses(self, bible_id: str, chapter_id: str) -> Dict[str, Any]:
        """
        Get a list of verses for a specific chapter.

        Args:
            bible_id: The ID of the Bible
            chapter_id: The ID of the chapter

        Returns:
            Dictionary containing the list of verses
        """
        endpoint = f'bibles/{bible_id}/chapters/{chapter_id}/verses'
        return self._make_request(endpoint)

    def get_verse(self, bible_id: str, verse_id: str) -> Dict[str, Any]:
        """
        Get information about a specific verse.

        Args:
            bible_id: The ID of the Bible
            verse_id: The ID of the verse

        Returns:
            Dictionary containing verse information
        """
        return self._make_request(f'bibles/{bible_id}/verses/{verse_id}')

    def search(self, bible_id: str, query: str) -> Dict[str, Any]:
        """
        Search for verses in a Bible.

        Args:
            bible_id: The ID of the Bible
            query: The search query

        Returns:
            Dictionary containing search results
        """
        params = {'query': query}
        return self._make_request(f'bibles/{bible_id}/search', params)
