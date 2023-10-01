const fileUploadInput = document.getElementById('file-upload');
const secondUploadButton = document.getElementById('upload-button-img');

fileUploadInput.addEventListener('change', function () {
    if (fileUploadInput.files.length > 0) {
        secondUploadButton.disabled = false;
    } else {
        secondUploadButton.disabled = true;
    }
});
function updateProgressBar() {
    const fields = document.querySelectorAll('.input-field');
    let filledFields = 0;

    // Check the input fields for values
    fields.forEach(function (field) {
        if (field.value.trim() !== '') {
            filledFields++;
        }
    });

    // Check the image condition
    const imgElement = document.querySelector('.upload-image-part img');
    if (imgElement && imgElement.getAttribute('src') && imgElement.getAttribute('src') !== 'avatar.jpg') {
        filledFields++;
    }

    // Check the checkbox condition
    const activateWhatsAppCheckbox = document.getElementById('activate-whatsapp');
    if (activateWhatsAppCheckbox && activateWhatsAppCheckbox.checked) {
        filledFields++;
    }

    // Calculate the width of the progress bar
    const progressBar = document.querySelector('.progress-bar');
    const widthPerField = 100 / 6; // 6 fields
    const progressBarWidth = filledFields * widthPerField;

    // Set the width of the progress bar
    progressBar.style.width = progressBarWidth + '%';
}

// Call the updateProgressBar function whenever there's a change in the form fields or image
const formElements = document.querySelectorAll('.input-field, #file-upload, #activate-whatsapp');
formElements.forEach(function (element) {
    element.addEventListener('change', updateProgressBar);
});

// Call the function initially to set the initial progress bar width
updateProgressBar();


$(document).ready(function () {
    // Select the modal and overlay elements
    const modal = $('#change-password-modal');
    const overlay = $('#modal-overlay');

    // Open the modal when the button is clicked
    $('.change-password-button').click(function () {
        modal.show(); // Show the modal
        overlay.show(); // Show the overlay
    });

    // Close the modal when clicking outside of it or on the overlay
    overlay.click(function (event) {
        if (event.target === overlay[0]) { // Check if the clicked element is the overlay itself
            modal.hide(); // Hide the modal
            overlay.hide(); // Hide the overlay
        }
    });

    // Handle form submission via Ajax
    $('#password-change-form').submit(function (e) {
        e.preventDefault();
        const formData = $(this).serialize();
        var button = $('.change-password-button');
        var url = button.data("url");
        $.ajax({
            type: 'POST',
            url: url,
            data: formData,
            success: function (data) {
                if (data.success) {
                    modal.hide(); // Hide the modal
                    overlay.hide(); // Hide the overlay
                    console.log('Password updated successfully.');
                    location.reload()
                } else {
                    location.reload()
                    console.log(data.error_message);
                }
            },
            error: function () {
                location.reload()
                console.log('An error occurred while updating the password.');
            }
        });
    });
});
