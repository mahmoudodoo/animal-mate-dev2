// JavaScript to handle the hover behavior
document.querySelector(".user-dropdown").addEventListener("mouseleave", function () {
  this.querySelector(".dropdown-content").style.display = "none";
});

document.querySelector(".user-dropdown").addEventListener("mouseenter", function () {
  this.querySelector(".dropdown-content").style.display = "block";
});



// Function to hide messages after 5 seconds
function hideMessages() {
  var messages = document.querySelectorAll('.messages .message');
  messages.forEach(function (message) {
    setTimeout(function () {
      message.style.display = 'none';
    }, 5000); // 5000 milliseconds = 5 seconds
  });
}

// Call the hideMessages function after the page has loaded
window.onload = function () {
  hideMessages();
};


$(document).ready(function () {
  $(".cat-dropdown").on("click", function (event) {
      event.preventDefault();
      var dropdownContent = $(this).find(".cat-dropdown-content");
      $(".cat-dropdown-content").not(dropdownContent).hide();
      dropdownContent.toggle();
  });

  // Close the dropdown if clicked outside
  $(document).on("click", function (event) {
      if (!$(event.target).closest(".cat-dropdown").length) {
          $(".cat-dropdown-content").hide();
      }
  });
});