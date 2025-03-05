import os
import sys
from app.app import app

if __name__ == '__main__':
    # Add the current directory to sys.path
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 