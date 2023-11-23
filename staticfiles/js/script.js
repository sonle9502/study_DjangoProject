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



// JavaScriptで確認ボタンにイベントリスナーを追加
document.addEventListener("DOMContentLoaded", function() {
    const kakuninButtons = document.querySelectorAll(".kakuninButton");
    kakuninButtons.forEach(function(button) {
        button.addEventListener("mouseover", function(e) {
            const taskId = button.getAttribute("data-task-id");
            const popup = document.getElementById("popup_" + taskId);
            
            // Show the popup
            popup.style.display = "block";

            // ポップアップの位置を設定
            // popup.style.left = e.clientX + "px"; // Add 10 pixels to create some spacing
            // popup.style.top = e.clientY - 70  + "px";
            popup.style.left = e.clientX + "px";
            popup.style.top = e.clientY + window.scrollY + "px"; 

            // ポップアップを表示
            //popup.style.display = "block";

        });

        button.addEventListener("mouseout", function(e) {
            const taskId = button.getAttribute("data-task-id");
            const popup = document.getElementById("popup_" + taskId);
            
            // ポップアップを表示
            popup.style.display = "none";

        });
    });
});
