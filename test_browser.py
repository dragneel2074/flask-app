"""
Test script for the WebBrowser utility class
"""
import sys
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add current directory to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import WebBrowser
try:
    from app.utils.browser import WebBrowser
    logger.info("Successfully imported WebBrowser")
except ImportError as e:
    logger.error(f"Error importing WebBrowser: {e}")
    sys.exit(1)

def test_browser():
    """Test basic functionality of the WebBrowser class"""
    logger.info("Creating WebBrowser instance...")
    browser = WebBrowser()
    
    # Test URL normalization
    test_urls = [
        "example.com",
        "http://example.com",
        "https://example.com",
        ""
    ]
    
    for url in test_urls:
        normalized = browser._normalize_url(url)
        logger.info(f"Normalized '{url}' to '{normalized}'")
    
    # Test fetching a page
    test_url = "http://example.com"
    logger.info(f"Fetching {test_url}...")
    content, error = browser.fetch_page(test_url)
    
    if error:
        logger.error(f"Error fetching {test_url}: {error}")
    else:
        logger.info(f"Successfully fetched {test_url}, content length: {len(content)}")
        
        # Test processing the page
        logger.info("Processing page content...")
        processed = browser.process_page(content, test_url)
        logger.info(f"Processed content length: {len(processed)}")
        
    # Print history
    logger.info(f"Browser history: {browser.get_history()}")
    
if __name__ == "__main__":
    logger.info("Starting WebBrowser test...")
    test_browser()
    logger.info("Test completed") 