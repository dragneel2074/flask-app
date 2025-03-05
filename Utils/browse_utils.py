# Utils/browse_utils.py
import requests
import logging

# Set up logger for this module
logger = logging.getLogger(__name__)


def fetch_website(url):
    """Fetch the content of the website from the given URL."""
    logger.debug(f'Attempting to fetch website content from URL: {url}')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com'
    }
    logger.debug(f'Custom headers set: {headers}')
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        # Set the encoding to the apparent encoding to handle non-UTF8 texts
        response.encoding = response.apparent_encoding
        logger.debug(f'Using encoding: {response.encoding}')
        logger.debug('Website fetched successfully')
        return response.text
    except Exception as e:
        logger.error(f'Error occurred while fetching website: {e}')
        raise

# Debug print statement to confirm module import
logger.debug('Initialized browse_utils module with fetch_website function') 