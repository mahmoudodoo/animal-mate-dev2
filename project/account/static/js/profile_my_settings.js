// Get references to the elements
const selectButton = document.getElementById('select-button');
const optionsList = document.getElementById('options-list');

// Add a click event listener to the select button
selectButton.addEventListener('click', () => {
    // Toggle the 'open' class on the options list to show/hide it
    optionsList.classList.toggle('open');
});

// Add a click event listener to each option to handle selection
const options = document.querySelectorAll('.option');
options.forEach((option) => {
    option.addEventListener('click', () => {
        // Update the selected option text
        const selectedOption = option.querySelector('strong').textContent;
        document.getElementById('selected-option').textContent = selectedOption;

        // Remove the 'selected' class from all options
        options.forEach((opt) => {
            opt.classList.remove('selected');
        });

        // Add the 'selected' class to the clicked option
        option.classList.add('selected');

        // Close the options list
        optionsList.classList.remove('open');

        // Optionally, you can handle the selected value here as well
        const selectedValue = option.getAttribute('value');
        // Do something with the selectedValue, e.g., send it to a server
    });
});

// Close the options list when clicking outside of it
document.addEventListener('click', (event) => {
    if (!selectButton.contains(event.target) && !optionsList.contains(event.target)) {
        optionsList.classList.remove('open');
    }
});
