import requests
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin, urlparse

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebBrowser:
    """Utility class to handle website browsing functionality"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.history = []
        # For debugging purposes
        logger.info("WebBrowser instance initialized")
    
    def _normalize_url(self, url):
        """Normalize URL by adding http:// if protocol is missing"""
        if not url:
            return None
            
        # Add http:// if no protocol specified
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            # Debug print
            logger.info(f"URL normalized to: {url}")
            
        return url
    
    def fetch_page(self, url):
        """Fetch a web page and return its content"""
        url = self._normalize_url(url)
        if not url:
            logger.error("Invalid URL provided")
            return None, "Invalid URL provided"
            
        try:
            logger.info(f"Attempting to fetch page: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()  # Raise exception for HTTP errors
            
            # Add to history
            if url not in self.history:
                self.history.append(url)
                
            return response.text, None
            
        except requests.exceptions.RequestException as e:
            error_msg = f"Error fetching page: {str(e)}"
            logger.error(error_msg)
            return None, error_msg
    
    def process_page(self, content, base_url):
        """Process page content and modify links to work with our proxy"""
        if not content:
            return ""
            
        try:
            logger.info(f"Processing page with base URL: {base_url}")
            soup = BeautifulSoup(content, 'lxml')
            
            # Process links to make them work with our proxy
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                # Convert relative URLs to absolute
                absolute_url = urljoin(base_url, href)
                # Update href to point to our proxy
                a_tag['href'] = f"/browse?url={absolute_url}"
                a_tag['target'] = '_self'  # Open in same tab
                
            # Debug print
            logger.info(f"Processed {len(soup.find_all('a', href=True))} links")
                
            # Handle forms
            for form in soup.find_all('form', action=True):
                action = form['action']
                absolute_action = urljoin(base_url, action)
                form['action'] = f"/submit?url={absolute_action}"
                
            return soup.prettify()
            
        except Exception as e:
            error_msg = f"Error processing page content: {str(e)}"
            logger.error(error_msg)
            return f"<html><body><h1>Error</h1><p>{error_msg}</p></body></html>"
    
    def get_history(self):
        """Return browsing history"""
        return self.history 