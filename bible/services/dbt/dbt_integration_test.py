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


# For testing, you can use a free test API key:
# 6ff42f85fc3a3825358ca470c638e29f

def run_test():
    """Run test queries with the DBT client."""
    print("\n" + "="*50)
    print("DBT API Integration Test")
    print("="*50)

    # Initialize client
    print("\nInitializing DBT client...")
    client = DBTClient()
    
    # Test 1: Get available Bibles
    print("\nTest 1: Get available Bibles")
    print("-"*30)
    try:
        # Use a simpler approach with direct API calls
        import requests
        base_url = "https://4.dbt.io/api"
        headers = {}
        params = {"key": client.api_key, "v": 4}
        
        response = requests.get(f"{base_url}/bibles", params=params, headers=headers)
        response.raise_for_status()
        bibles = response.json()
        
        print(f"Success! Found {len(bibles.get('data', []))} Bibles")
        
        # Show the first 3 Bibles
        print("\nSample Bibles:")
        for bible in bibles.get('data', [])[:3]:
            print(f"ID: {bible.get('id')}, Name: {bible.get('name')}, Language: {bible.get('language', {}).get('name')}")
    except Exception as e:
        print(f"Error fetching Bibles: {e}")
    
    # Test 2: Get English Bibles
    print("\nTest 2: Get English Bibles")
    print("-"*30)
    try:
        eng_bibles = client.get_bibles(language_code="eng", v=4)
        print(f"Success! Found {len(eng_bibles.get('data', []))} English Bibles")
        
        # Find ESV Bible ID
        esv_id = next((b.get('id') for b in eng_bibles.get('data', []) 
                      if 'ESV' in b.get('name', '')), None)
        
        if not esv_id:
            print("ESV Bible not found, using first available English Bible")
            if eng_bibles.get('data'):
                esv_id = eng_bibles['data'][0]['id']
            else:
                print("No English Bibles found")
                return
        
        print(f"Selected Bible ID: {esv_id}")
    except Exception as e:
        print(f"Error fetching English Bibles: {e}")
        return
    
    # Test 3: Get Bible books
    print("\nTest 3: Get books for selected Bible")
    print("-"*30)
    try:
        books = client.get_books(esv_id, v=4)
        print(f"Success! Found {len(books.get('data', []))} books")
        
        # Show the first 5 books
        print("\nSample Books:")
        for book in books.get('data', [])[:5]:
            print(f"ID: {book.get('id')}, Name: {book.get('name')}")
            
        # Select Genesis for further testing
        genesis_id = next((b.get('id') for b in books.get('data', []) 
                          if b.get('name') == 'Genesis'), 'GEN')
    except Exception as e:
        print(f"Error fetching books: {e}")
        return
    
    # Test 4: Get chapters in Genesis
    print(f"\nTest 4: Get chapters for {genesis_id}")
    print("-"*30)
    try:
        chapters = client.get_chapters(esv_id, genesis_id, v=4)
        print(f"Success! Found {len(chapters.get('data', []))} chapters in Genesis")
    except Exception as e:
        print(f"Error fetching chapters: {e}")
        return
    
    # Test 5: Get verses for Genesis 1
    chapter_id = f"{genesis_id}.1"
    print(f"\nTest 5: Get verses for {chapter_id}")
    print("-"*30)
    try:
        # We need to find a fileset ID first
        bible = client.get_bible(esv_id, v=4)
        fileset_id = None
        if 'data' in bible and 'filesets' in bible['data']:
            for fileset in bible['data']['filesets']:
                if fileset.get('type', {}).get('id') == 'text_plain':
                    fileset_id = fileset.get('id')
                    break
        
        if not fileset_id:
            print("No suitable fileset found, using Bible ID as fileset ID")
            fileset_id = esv_id
        
        print(f"Using fileset ID: {fileset_id}")
        
        verses = client.get_verses(fileset_id, chapter_id, v=4)
        verse_count = len(verses.get('data', []))
        print(f"Success! Found {verse_count} verses in Genesis 1")
        
        # Show the first 3 verses
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
    
    # Test 6: Search for a term
    search_term = "love"
    print(f"\nTest 6: Search for '{search_term}' in selected Bible")
    print("-"*30)
    try:
        search_results = client.search(fileset_id, search_term, v=4)
        # The structure might be different, adjust based on actual response
        verses = search_results.get('data', {}).get('verses', [])
        verse_count = len(verses)
        print(f"Success! Found {verse_count} verses containing '{search_term}'")
        
        # Show the first 3 search results
        print("\nFirst 3 search results:")
        for verse in verses[:3]:
            # Adjust based on actual response structure
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
