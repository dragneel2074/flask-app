import logging
import urllib.parse
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def rewrite_links(html_content, base_url):
    """Rewrite all hyperlinks in the HTML content so that they route through the /browse endpoint of our app.
    For each <a> tag with an href, the link is converted to an absolute URL using base_url, then re-encoded as 
    a proxy URL that points to /browse?url=<encoded_absolute_url>.

    Args:
        html_content (str): The original HTML of the website.
        base_url (str): The URL from which the HTML was fetched, used to resolve relative links.

    Returns:
        str: The modified HTML content with rewritten links.
    """
    logger.debug(f'Starting link rewriting process with base URL: {base_url}')
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Process each anchor tag with an href attribute
    for a in soup.find_all('a', href=True):
        original_href = a['href']
        logger.debug(f'Found link: {original_href}')
        # Resolve the href to an absolute URL using base_url
        absolute_url = urllib.parse.urljoin(base_url, original_href)
        logger.debug(f'Resolved absolute URL: {absolute_url}')
        # Encode the absolute URL and set the href to point to our /browse route
        proxy_url = '/browse?url=' + urllib.parse.quote(absolute_url, safe='')
        a['href'] = proxy_url
        logger.debug(f'Rewritten link: {proxy_url}')
        
    logger.debug('Finished rewriting all links')
    return str(soup) 