"""
Test script for the DBT client integration.

This script demonstrates how to use the DBT client to make requests to the DBT API.
It assumes you have an API key set in the DBT_API_KEY environment variable.

Run with:
python manage.py shell < bible/services/dbt/dbt_integration_test.py

Or:
export DBT_API_KEY=your_api_key
python bible/services/dbt/dbt_integration_test.py
"""
import os
import sys
import json
from pprint import pprint

# Add the project root to the path if running directly
if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bible_research.settings")

from bible.services.dbt.client import DBTClient


def run_test():
    """Run test queries with the DBT client."""
    print("\n" + "="*50)
    print("DBT API Integration Test")
    print("="*50)

    client = DBTClient()
    chapter_id = f"GEN.1"
    print(f"\nTest 5: Get verses for {chapter_id}")
    print("-"*30)
    try:
        fileset_id = "ENGESV"
        chapter_id = "GEN.1"
        verses = client.get_verses(fileset_id, chapter_id, v=4)
        verse_count = len(verses.get('data', []))
        print(f"Success! Found {verse_count} verses in Genesis 1")

        print("\nFirst 3 verses:")
        for verse in verses.get('data', [])[:3]:
            # The verse structure might be different, adjust based on actual response
            verse_id = verse.get('verse_start', '')
            content = verse.get('verse_text', '')
            print(f"Verse {verse_id}: {content}")
    except Exception as e:
        print(f"Error fetching verses: {e}")
        print(f"Error details: {str(e)}")
        return

    search_term = "love"
    print(f"\nSearch for '{search_term}' in selected Bible")
    print("-"*30)
    try:
        search_results = client.search(fileset_id, search_term, v=4)
        verses = search_results.get('data', {}).get('verses', [])
        verse_count = len(verses)
        print(f"Success! Found {verse_count} verses containing '{search_term}'")

        print("\nFirst 3 search results:")
        for verse in verses[:3]:
            reference = verse.get('reference', '')
            text = verse.get('text', '')
            print(f"{reference}: {text}")
    except Exception as e:
        print(f"Error searching: {e}")
        print(f"Error details: {str(e)}")
    
    print("\n" + "="*50)
    print("DBT API Integration Test Complete")
    print("="*50 + "\n")


if __name__ == "__main__":
    run_test()
