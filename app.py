from flask import Flask, render_template, request
import logging
from Utils import browse_utils

app = Flask(__name__)

# Set up logging and enable debug prints
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    # Render the homepage with a form to input a URL
    app.logger.debug('Rendering index page')
    return render_template('index.html')

@app.route('/browse', methods=['GET', 'POST'])
def browse():
    # This route processes the URL input and fetches the website content
    url = request.values.get('url')
    app.logger.debug(f'Received URL: {url}')
    if not url:
        app.logger.debug('No URL provided, redirecting to index')
        return render_template('index.html', error='Please provide a URL.')
    try:
        # Use helper function from Utils to fetch content
        content = browse_utils.fetch_website(url)
        app.logger.debug('Website content fetched successfully')
        return render_template('display.html', url=url, content=content)
    except Exception as e:
        app.logger.error(f'Error fetching website: {e}')
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.logger.debug('Starting Flask app in debug mode')
    app.run(debug=True) 