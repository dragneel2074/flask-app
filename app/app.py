from flask import Flask, render_template, request, redirect, url_for, flash
import os
import logging
from app.utils.browser import WebBrowser

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev_key_for_debugging')

# Initialize the WebBrowser instance
browser = WebBrowser()

@app.route('/')
def index():
    """Home page with search form"""
    # Debug print
    logger.info("Home page accessed")
    return render_template('index.html', history=browser.get_history())

@app.route('/browse')
def browse():
    """Browse a webpage"""
    url = request.args.get('url')
    
    # Debug print
    logger.info(f"Browsing URL: {url}")
    
    if not url:
        flash('Please enter a URL', 'error')
        return redirect(url_for('index'))
        
    # Fetch the page content
    content, error = browser.fetch_page(url)
    
    if error:
        flash(f'Error: {error}', 'error')
        return render_template('error.html', error=error)
        
    # Process the page content to make it work with our proxy
    processed_content = browser.process_page(content, url)
    
    return render_template('browse.html', 
                          content=processed_content, 
                          url=url, 
                          history=browser.get_history())

@app.route('/submit', methods=['POST'])
def submit_form():
    """Handle form submissions from browsed pages"""
    url = request.args.get('url')
    
    # Debug print
    logger.info(f"Form submission to URL: {url}")
    
    if not url:
        flash('Invalid form submission', 'error')
        return redirect(url_for('index'))
        
    # This is a simplistic implementation - in a real browser you would
    # need to handle different form methods, encodings, etc.
    try:
        # Get form data
        form_data = request.form.to_dict()
        
        # Debug print form data
        logger.info(f"Form data: {form_data}")
        
        # Make the request
        response = browser.session.post(url, data=form_data, timeout=10)
        response.raise_for_status()
        
        # Process the response content
        processed_content = browser.process_page(response.text, url)
        
        return render_template('browse.html', 
                              content=processed_content, 
                              url=url, 
                              history=browser.get_history())
                              
    except Exception as e:
        error_msg = f"Error submitting form: {str(e)}"
        logger.error(error_msg)
        flash(error_msg, 'error')
        return render_template('error.html', error=error_msg)

@app.route('/clear-history')
def clear_history():
    """Clear browsing history"""
    # Debug print
    logger.info("Clearing browsing history")
    browser.history = []
    flash('Browsing history cleared', 'info')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    logger.error(f"404 error: {e}")
    return render_template('error.html', error="Page not found"), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    logger.error(f"500 error: {e}")
    return render_template('error.html', error="Server error"), 500

if __name__ == '__main__':
    # For debugging purposes, set debug to True
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    logger.info("Flask app starting in debug mode") 