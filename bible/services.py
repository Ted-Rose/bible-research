import requests
from django.conf import settings

class ESVApiError(Exception):
    """Custom exception for API-related errors."""
    pass

def get_passage_data(passage_query: str, format: str = 'json'):
    """
    Fetches passage data from the ESV API.

    Args:
        passage_query: The Bible passage to look up (e.g., "John 3:16", "Genesis 1").
        format: The desired format ('json', 'text', or 'audio').

    Returns:
        The response from the API, either as a dict (for json/text) or bytes (for audio).

    Raises:
        ESVApiError: If the API returns a non-200 status code or the passage is not found.
    """
    if format not in ['json', 'text', 'audio']:
        raise ValueError(f"Unsupported format: {format}")

    url = f'https://api.esv.org/v3/passage/{format}/'
    params = {
        'q': passage_query,
        'include-headings': False,
        'include-footnotes': False,
        'include-verse-numbers': True,
        'include-short-copyright': False,
        'include-passage-references': False
    }

    headers = {
        'Authorization': f'Token {settings.ESV_KEY}'
    }

    try:
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        resp.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        if format in ['json', 'text']:
            json_resp = resp.json()
            if not json_resp.get('passages'):
                raise ESVApiError(f"Passage not found for query: '{passage_query}'")
            return json_resp

        elif format == 'audio':
            return resp.content

    except requests.exceptions.RequestException as e:
        raise ESVApiError(f"A network error occurred: {e}") from e

    return None


def search_passages(search_text: str):
    """
    Searches the ESV API for passages containing the given text.

    Args:
        search_text: The text to search for (e.g., "Zeal of the Lord").

    Returns:
        A dictionary containing the search results.
    """
    # The 'search' functionality is just a variation of the passage query
    url = 'https://api.esv.org/v3/passage/search/'
    params = {'q': search_text}
    headers = {'Authorization': f'Token {settings.ESV_KEY}'}

    try:
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        raise ESVApiError(f"A network error occurred during search: {e}") from e
