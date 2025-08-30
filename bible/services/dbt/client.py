"""
Wrapper for the DBT API client.
This module provides a simplified interface to the DBT API client.
"""
import os
import yaml
from django.conf import settings
from bible.dbt_client.openapi_client.api import (
    BiblesApi,
    BooksApi,
    ChaptersApi,
    VersesApi,
    SearchApi,
)
from bible.dbt_client.openapi_client.configuration import Configuration
from bible.dbt_client.openapi_client.api_client import ApiClient


class DBTClient:
    """
    Client for the Digital Bible Platform API.
    This class provides a simplified interface to the DBT API client.
    """

    def __init__(self):
        """
        Initialize the DBT API client.

        Args:
            api_key: The API key for the DBT API. If not provided, it will be
                    retrieved from config.yaml or Django settings.
        """
        config_path = os.path.join(
            settings.BASE_DIR, 'config.yaml'
            )
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            self.api_key = config.get('DBT_API_KEY')

        # Configure the API client
        self.configuration = Configuration()
        self.configuration.api_key['key'] = self.api_key
        self.configuration.host = "https://4.dbt.io"
    
        # Create the API client
        self.api_client = ApiClient(self.configuration)
    
        # Initialize API instances
        self.bibles_api = BiblesApi(self.api_client)
        self.books_api = BooksApi(self.api_client)
        self.chapters_api = ChaptersApi(self.api_client)
        self.verses_api = VersesApi(self.api_client)
        self.search_api = SearchApi(self.api_client)

    def get_bibles(self, language=None, **kwargs):
        """
        Get a list of available Bibles.

        Args:
            language: Filter by language code (e.g., 'eng' for English)
            **kwargs: Additional parameters to pass to the API

        Returns:
            List of Bible objects
        """
        return self.bibles_api.v4_bibles_get(language=language, **kwargs)

    def get_bible(self, bible_id, **kwargs):
        """
        Get information about a specific Bible.
    
        Args:
            bible_id: The ID of the Bible
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            Bible object
        """
        return self.bibles_api.v4_bibles_id_get(id=bible_id, **kwargs)

    def get_books(self, bible_id, **kwargs):
        """
        Get a list of books for a specific Bible.
    
        Args:
            bible_id: The ID of the Bible
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            List of Book objects
        """
        return self.books_api.v4_bibles_bible_id_books_get(
            bible_id=bible_id, **kwargs
        )

    def get_book(self, bible_id, book_id, **kwargs):
        """
        Get information about a specific book.
    
        Args:
            bible_id: The ID of the Bible
            book_id: The ID of the book
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            Book object
        """
        return self.books_api.v4_bibles_bible_id_books_book_id_get(
            bible_id=bible_id, book_id=book_id, **kwargs
        )

    def get_chapters(self, bible_id, book_id, **kwargs):
        """
        Get a list of chapters for a specific book.
    
        Args:
            bible_id: The ID of the Bible
            book_id: The ID of the book
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            List of Chapter objects
        """
        return self.chapters_api.v4_bibles_bible_id_books_book_id_chapters_get(
            bible_id=bible_id, book_id=book_id, **kwargs
        )

    def get_chapter(self, bible_id, chapter_id, **kwargs):
        """
        Get information about a specific chapter.
    
        Args:
            bible_id: The ID of the Bible
            chapter_id: The ID of the chapter
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            Chapter object
        """
        return self.chapters_api.v4_bibles_bible_id_chapters_chapter_id_get(
            bible_id=bible_id, chapter_id=chapter_id, **kwargs
        )

    def get_verses(self, bible_id, chapter_id, **kwargs):
        """
        Get a list of verses for a specific chapter.
    
        Args:
            bible_id: The ID of the Bible
            chapter_id: The ID of the chapter
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            List of Verse objects
        """
        return self.verses_api.v4_bibles_bible_id_chapters_chapter_id_verses_get(
            bible_id=bible_id,
            chapter_id=chapter_id,
            **kwargs
        )

    def get_verse(self, bible_id, verse_id, **kwargs):
        """
        Get information about a specific verse.
    
        Args:
            bible_id: The ID of the Bible
            verse_id: The ID of the verse
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            Verse object
        """
        return self.verses_api.v4_bibles_bible_id_verses_verse_id_get(
            bible_id=bible_id,
            verse_id=verse_id,
            **kwargs
        )

    def search(self, bible_id, query, **kwargs):
        """
        Search for verses in a Bible.
    
        Args:
            bible_id: The ID of the Bible
            query: The search query
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            Search results
        """
        return self.search_api.v4_bibles_bible_id_search_get(
            bible_id=bible_id,
            query=query,
            **kwargs
        )
