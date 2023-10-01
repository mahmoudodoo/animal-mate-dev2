// Get the URL text and copy button
const urlText = document.querySelector('.url-text');
const copyButton = document.getElementById('copy-button');

// Add a click event listener to the copy button
copyButton.addEventListener('click', () => {
    // Create a temporary input element to copy the text
    const tempInput = document.createElement('input');
    tempInput.value = urlText.textContent;
    document.body.appendChild(tempInput);

    // Select the text in the input element
    tempInput.select();

    // Use the Clipboard API to copy the selected text to the clipboard
    navigator.clipboard.writeText(tempInput.value).then(() => {
        // Change the button text to indicate success
        copyButton.textContent = 'Copied!';
        setTimeout(() => {
            copyButton.innerHTML = '<i class="fa fa-files-o" aria-hidden="true"></i>';
        }, 2000); // Reset the button text after 2 seconds
    }).catch((error) => {
        console.error('Unable to copy text: ', error);
    }).finally(() => {
        // Remove the temporary input element
        document.body.removeChild(tempInput);
    });
});
