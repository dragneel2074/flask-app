# Utils/browse_utils.py
import requests
import logging

# Set up logger for this module
logger = logging.getLogger(__name__)


def fetch_website(url):
    """Fetch the content of the website from the given URL."""
    logger.debug(f'Attempting to fetch website content from URL: {url}')
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        logger.debug('Website fetched successfully')
        return response.text
    except Exception as e:
        logger.error(f'Error occurred while fetching website: {e}')
        raise

# Debug print statement to confirm module import
logger.debug('Initialized browse_utils module with fetch_website function') 