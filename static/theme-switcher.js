// static/theme-switcher.js
// Debug: Theme switcher script for light/dark mode

document.addEventListener('DOMContentLoaded', function() {
    console.debug('Theme switcher script initialized');
    
    // Create theme switcher button
    const themeSwitcher = document.createElement('div');
    themeSwitcher.className = 'theme-switcher';
    themeSwitcher.innerHTML = `
        <button class="btn btn-sm" id="theme-toggle">
            <i class="fas fa-moon"></i>
        </button>
    `;
    
    // Add theme switcher to the page
    document.body.appendChild(themeSwitcher);
    
    // Get the toggle button and icon
    const toggleBtn = document.getElementById('theme-toggle');
    const toggleIcon = toggleBtn.querySelector('i');
    
    // Check for saved theme preference or use device preference
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Set initial theme
    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
        document.body.classList.add('dark-theme');
        toggleIcon.classList.replace('fa-moon', 'fa-sun');
        console.debug('Dark theme applied based on preference');
    }
    
    // Toggle theme function
    function toggleTheme() {
        if (document.body.classList.contains('dark-theme')) {
            document.body.classList.remove('dark-theme');
            toggleIcon.classList.replace('fa-sun', 'fa-moon');
            localStorage.setItem('theme', 'light');
            console.debug('Switched to light theme');
        } else {
            document.body.classList.add('dark-theme');
            toggleIcon.classList.replace('fa-moon', 'fa-sun');
            localStorage.setItem('theme', 'dark');
            console.debug('Switched to dark theme');
        }
    }
    
    // Add click event to toggle button
    toggleBtn.addEventListener('click', toggleTheme);
    
    // Add CSS for theme switcher and dark theme
    const style = document.createElement('style');
    style.textContent = `
        .theme-switcher {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
        }
        
        .theme-switcher button {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: var(--primary-color);
            color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
        }
        
        .theme-switcher button:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }
        
        /* Dark theme styles */
        .dark-theme {
            background-color: #121212 !important;
            color: #e0e0e0 !important;
        }
        
        .dark-theme .navbar {
            background-color: #1e1e1e !important;
        }
        
        .dark-theme .card,
        .dark-theme .content-container {
            background-color: #1e1e1e !important;
            color: #e0e0e0 !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
        }
        
        .dark-theme .form-control {
            background-color: #2d2d2d !important;
            border-color: #444 !important;
            color: #e0e0e0 !important;
        }
        
        .dark-theme .form-label {
            color: #e0e0e0 !important;
        }
        
        .dark-theme footer {
            color: #aaa !important;
        }
    `;
    document.head.appendChild(style);
    console.debug('Theme switcher styles added');
});

// Debug: End of theme switcher script 