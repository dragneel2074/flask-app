// Main JavaScript for Flask Web Browser

// Debug function to help with development
function debug(message) {
    console.log(`[DEBUG] ${message}`);
}

// Initialize when the document is loaded
document.addEventListener('DOMContentLoaded', function() {
    debug('Document loaded');
    
    // Handle form submissions - prevent default for potential AJAX use later
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        debug(`Found form with action: ${form.getAttribute('action')}`);
    });
    
    // Add event listeners to navigation buttons if they exist
    const backButton = document.querySelector('[onclick="window.history.back();"]');
    if (backButton) {
        debug('Found back button');
        backButton.addEventListener('click', function() {
            debug('Back button clicked');
        });
    }
    
    // Highlight the current URL in history list if it exists
    const currentUrl = document.querySelector('input[name="url"]')?.value;
    if (currentUrl) {
        debug(`Current URL: ${currentUrl}`);
        document.querySelectorAll('.list-group-item a').forEach(link => {
            if (link.textContent === currentUrl) {
                link.parentElement.classList.add('active');
                debug('Highlighted current URL in history');
            }
        });
    }
    
    // Log page load time for performance monitoring
    const loadTime = window.performance.timing.domContentLoadedEventEnd - window.performance.timing.navigationStart;
    debug(`Page loaded in ${loadTime}ms`);
}); 