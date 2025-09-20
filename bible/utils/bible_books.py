"""Utility functions for working with Bible books and their standard abbreviations."""

# Mapping of full book names to standard book IDs used by the DBT API
DBT_BOOK_NAME_TO_ID = {
    # Old Testament
    'genesis': 'GEN', 'exodus': 'EXO', 'leviticus': 'LEV',
    'numbers': 'NUM', 'deuteronomy': 'DEU', 'joshua': 'JOS',
    'judges': 'JDG', 'ruth': 'RUT', '1 samuel': '1SA',
    '2 samuel': '2SA', '1 kings': '1KI', '2 kings': '2KI',
    '1 chronicles': '1CH', '2 chronicles': '2CH', 'ezra': 'EZR',
    'nehemiah': 'NEH', 'esther': 'EST', 'job': 'JOB',
    'psalms': 'PSA', 'proverbs': 'PRO', 'ecclesiastes': 'ECC',
    'song of solomon': 'SNG', 'isaiah': 'ISA', 'jeremiah': 'JER',
    'lamentations': 'LAM', 'ezekiel': 'EZK', 'daniel': 'DAN',
    'hosea': 'HOS', 'joel': 'JOL', 'amos': 'AMO',
    'obadiah': 'OBA', 'jonah': 'JON', 'micah': 'MIC',
    'nahum': 'NAM', 'habakkuk': 'HAB', 'zephaniah': 'ZEP',
    'haggai': 'HAG', 'zechariah': 'ZEC', 'malachi': 'MAL',
    # New Testament
    'matthew': 'MAT', 'mark': 'MRK', 'luke': 'LUK',
    'john': 'JHN', 'acts': 'ACT', 'romans': 'ROM',
    '1 corinthians': '1CO', '2 corinthians': '2CO', 'galatians': 'GAL',
    'ephesians': 'EPH', 'philippians': 'PHP', 'colossians': 'COL',
    '1 thessalonians': '1TH', '2 thessalonians': '2TH', '1 timothy': '1TI',
    '2 timothy': '2TI', 'titus': 'TIT', 'philemon': 'PHM',
    'hebrews': 'HEB', 'james': 'JAS', '1 peter': '1PE',
    '2 peter': '2PE', '1 john': '1JN', '2 john': '2JN',
    '3 john': '3JN', 'jude': 'JUD', 'revelation': 'REV'
}


def get_dbt_book_id(book_name):
    """Convert a book name to its standard book ID.

    Args:
        book_name (str): The name of the book (e.g., '2 chronicles')

    Returns:
        str: The standard book ID (e.g., '2CH'), or None if not found
    """
    normalized = ' '.join(book_name.lower().strip().split())
    return DBT_BOOK_NAME_TO_ID.get(normalized, None)
