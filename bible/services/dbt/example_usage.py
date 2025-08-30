"""
Example usage of the DBT client in Django shell.

Run with:
python manage.py shell < bible/services/dbt/example_usage.py
"""
from bible.services.dbt.client import DBTClient
import json
from pprint import pprint

# Initialize the client
print("Initializing DBT client...")
client = DBTClient()

# Get all Bibles
print("\nFetching all Bibles...")
try:
    bibles = client.get_bibles()
    print(f"Found {len(bibles.get('data', []))} Bibles")
except Exception as e:
    print(f"Error fetching Bibles: {e}")
    bibles = {'data': []}

# Get English Bibles
print("\nFetching English Bibles...")
try:
    eng_bibles = client.get_bibles(language="eng")
    print(f"Found {len(eng_bibles.get('data', []))} English Bibles")
    
    # Print the first few English Bibles
    print("\nFirst 3 English Bibles:")
    for bible in eng_bibles.get('data', [])[:3]:
        print(f"ID: {bible.get('id')}, Name: {bible.get('name')}")
except Exception as e:
    print(f"Error fetching English Bibles: {e}")
    eng_bibles = {'data': []}

# Get a specific Bible (ESV)
# Using the ESV ID from the list above
esv_id = next((b.get('id') for b in eng_bibles.get('data', []) 
              if 'ESV' in b.get('name', '')), None)

if esv_id:
    print(f"\nFetching ESV Bible (ID: {esv_id})...")
    esv = client.get_bible(esv_id)
    print(f"Bible name: {esv.get('data', {}).get('name')}")
    
    # Get books for ESV
    print("\nFetching books for ESV...")
    books = client.get_books(esv_id)
    print(f"Found {len(books.get('data', []))} books")
    
    # Get Genesis
    genesis_id = "GEN"
    print(f"\nFetching Genesis (ID: {genesis_id})...")
    genesis = client.get_book(esv_id, genesis_id)
    print(f"Book name: {genesis.get('data', {}).get('name')}")
    
    # Get chapters for Genesis
    print("\nFetching chapters for Genesis...")
    chapters = client.get_chapters(esv_id, genesis_id)
    print(f"Found {len(chapters.get('data', []))} chapters in Genesis")
    
    # Get verses for Genesis 1
    chapter_id = "GEN.1"
    print(f"\nFetching verses for {chapter_id}...")
    verses = client.get_verses(esv_id, chapter_id)
    print(f"Found {len(verses.get('data', []))} verses in Genesis 1")
    
    # Print the first few verses
    print("\nFirst 5 verses of Genesis 1:")
    for verse in verses.get('data', [])[:5]:
        print(f"Verse {verse.get('id')}: {verse.get('content')}")
    
    # Search for a term
    search_term = "love"
    print(f"\nSearching for '{search_term}' in ESV...")
    search_results = client.search(esv_id, search_term)
    print(f"Found {len(search_results.get('data', {}).get('verses', []))} verses containing '{search_term}'")
    
    # Print the first few search results
    print(f"\nFirst 3 verses containing '{search_term}':")
    for verse in search_results.get('data', {}).get('verses', [])[:3]:
        print(f"{verse.get('reference')}: {verse.get('text')}")
else:
    print("ESV Bible not found")

print("\nExample usage complete!")
