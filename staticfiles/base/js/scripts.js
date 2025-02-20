// Navbar Toggle for Mobile
document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.querySelector(".nav-toggle");
    const navList = document.querySelector(".nav-list");
    const navLinks = document.querySelectorAll(".nav-list li"); // Select all <li> elements

    // Toggle the menu on button click
    toggleBtn.addEventListener("click", function () {
        this.classList.toggle("active");
        navList.classList.toggle("active");
    });

    // Close the menu when clicking on a navigation item
    navLinks.forEach(link => {
        link.addEventListener("click", function () {
            toggleBtn.classList.remove("active"); // Remove active state from button
            navList.classList.remove("active");  // Hide the menu
        });
    });
});



// Loading Screen
window.addEventListener('load', () => {
    const loadingScreen = document.querySelector('.loading-screen');
    loadingScreen.style.display = 'none';
});

// Smooth Scrolling
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        document.querySelector(targetId).scrollIntoView({
            behavior: 'smooth'
        });
    });
});