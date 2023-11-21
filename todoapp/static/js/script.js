// script.js
//alert("Hello, this is a Django project!");

document.addEventListener('DOMContentLoaded', function() {
    // This function will be executed when the DOM is fully loaded

    // Get the element with the ID 'change-text'
    var myElement = document.getElementById('change-text');

    // Check if the element exists
    if (myElement) {
        // Change the text content of the element
        myElement.textContent = "Hello from script.js!";
    }
});