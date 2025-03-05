# Flask Web Browser

A simple web browser built with Flask that allows users to browse websites through a proxy. This application demonstrates how to create a basic web browser using Python and Flask.

## Features

- Browse any website by entering a URL
- Form submission support
- Browsing history tracking
- URL navigation (back, forward, reload)
- Error handling

## Installation

1. Clone this repository:
```
git clone <repository-url>
cd flask-web-browser
```

2. Create a virtual environment and activate it:
```
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

3. Install the required packages:
```
pip install -r requirements.txt
```

## Usage

1. Run the application:
```
python run.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Enter a URL in the input field and click "Browse" to start browsing

## How It Works

This application works as a proxy to browse websites:

1. When you enter a URL, the Flask app fetches the content of that website
2. The HTML content is processed to make all links work with our proxy
3. The processed content is displayed in the browser

## Technical Details

- Uses the `requests` library to fetch web pages
- Uses `BeautifulSoup` to parse and modify HTML content
- Implements session tracking for browsing history
- Handles form submissions 

## Limitations

- JavaScript functionality on visited websites is limited
- Some websites may block proxy access
- Not all types of form submissions are supported
- No support for cookies or local storage
- Limited support for complex websites

## Security Considerations

This is a demonstration project and should not be used in production without additional security measures:

- The application does not sanitize or validate all input
- There is no content filtering
- No HTTPS support for secure browsing
- No authentication or user management

## License

This project is licensed under the MIT License - see the LICENSE file for details. 