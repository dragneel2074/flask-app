// static/loading.js
// Debug: Loading animation script for website browser

document.addEventListener('DOMContentLoaded', function() {
    console.debug('Loading animation script initialized');
    
    // Get the form element
    const form = document.querySelector('form[action="/browse"]');
    
    if (form) {
        // Create loading overlay elements
        const loadingOverlay = document.createElement('div');
        loadingOverlay.className = 'loading-overlay';
        loadingOverlay.innerHTML = `
            <div class="spinner-container">
                <div class="spinner-border text-light" role="status" style="width: 3rem; height: 3rem;"></div>
                <p class="mt-3 text-light">Loading website content...</p>
            </div>
        `;
        
        // Add loading overlay to body but hide it initially
        document.body.appendChild(loadingOverlay);
        console.debug('Loading overlay added to DOM');
        
        // Add submit event listener to show loading animation
        form.addEventListener('submit', function() {
            console.debug('Form submitted, showing loading animation');
            loadingOverlay.style.display = 'flex';
            
            // For very slow connections, add a timeout message
            setTimeout(function() {
                const spinnerContainer = document.querySelector('.spinner-container');
                if (spinnerContainer && document.body.contains(loadingOverlay)) {
                    const timeoutMsg = document.createElement('p');
                    timeoutMsg.className = 'text-light mt-2';
                    timeoutMsg.textContent = 'This is taking longer than expected. Please be patient...';
                    spinnerContainer.appendChild(timeoutMsg);
                    console.debug('Added timeout message to loading animation');
                }
            }, 8000);
        });
    } else {
        console.debug('Browse form not found on this page');
    }
    
    // Add CSS for the loading overlay
    const style = document.createElement('style');
    style.textContent = `
        .loading-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            backdrop-filter: blur(5px);
        }
        
        .spinner-container {
            text-align: center;
        }
    `;
    document.head.appendChild(style);
    console.debug('Loading overlay styles added');
});

// Debug: End of loading animation script 