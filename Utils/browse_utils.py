# Utils/browse_utils.py
import requests
import logging
import random
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up logger for this module
logger = logging.getLogger(__name__)

# After logger definition, add persistent session and proxies pool
session = requests.Session()
# Debug: Created persistent session for cookie handling

# You can add proxies to the pool if needed. For now, it's empty.
proxies_pool = []
# Debug: Proxies pool initialized as empty (add proxies if needed)

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), retry=retry_if_exception_type(Exception))
def fetch_website(url):
    """Fetch the content of the website from the given URL with retries and session handling."""
    logger.debug(f'Attempting to fetch website content from URL: {url}')
    # Define a list of user agents to rotate
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    ]
    chosen_user_agent = random.choice(user_agents)
    logger.debug(f'Chosen User-Agent: {chosen_user_agent}')
    
    # Set custom headers using the chosen user agent
    headers = {
        'User-Agent': chosen_user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com'
    }
    logger.debug(f'Custom headers set: {headers}')
    
    # Optionally rotate proxies if available
    proxy = random.choice(proxies_pool) if proxies_pool else None
    if proxy:
        logger.debug(f'Using proxy: {proxy}')
    else:
        logger.debug('No proxy will be used')
    
    try:
        response = session.get(url, headers=headers, proxies=proxy, timeout=10)
        response.raise_for_status()
        # Set the encoding to the apparent encoding to handle non-UTF8 texts
        response.encoding = response.apparent_encoding
        logger.debug(f'Using encoding: {response.encoding}')
        logger.debug('Website fetched successfully')
        return response.text
    except Exception as e:
        logger.error(f'Error occurred while fetching website using Requests: {e}')
        logger.debug('Attempting to fetch website using Selenium as backup')
        try:
            selenium_content = fetch_website_selenium(url)
            return selenium_content
        except Exception as selenium_exception:
            logger.error(f'Error occurred while fetching website using Selenium: {selenium_exception}')
            raise selenium_exception

def fetch_website_selenium(url):
    """Fetch the content of the website using Selenium as a backup method with optimized settings."""
    logger.debug(f'Attempting to fetch website content via Selenium for URL: {url}')
    options = Options()
    options.headless = True
    # Optimize Selenium performance
    options.page_load_strategy = 'eager'
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    logger.debug('Selenium options optimized for speed (eager loading, GPU disabled, images disabled)')
    try:
        driver = webdriver.Chrome(options=options)
        logger.debug('Initialized Selenium Chrome WebDriver')
        driver.get(url)
        selenium_content = driver.page_source
        logger.debug('Website fetched successfully via Selenium')
        return selenium_content
    except Exception as e:
        logger.error(f'Error occurred while fetching website using Selenium: {e}')
        raise
    finally:
        try:
            driver.quit()
            logger.debug('Selenium WebDriver closed')
        except Exception as quit_exception:
            logger.error(f'Error closing Selenium WebDriver: {quit_exception}')

# Debug print statement to confirm module import
logger.debug('Initialized browse_utils module with fetch_website function') 