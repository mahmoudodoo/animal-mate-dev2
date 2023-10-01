$(document).ready(function() {
  const dropzone = $('#dropzone-box');
  const fileCards = dropzone.find('.file-cards');
  const fileInput = $('#file-input');

  // Function to handle file selection
  function handleFiles(files) {
    if (fileCards.children().length + files.length > 4) {
      alert('You can only upload up to 4 files.');
      return;
    }

    
    
    for (const file of files) {
      const reader = new FileReader();
      reader.onload = function(e) {
        const card = createFileCard(file, e.target.result);
        fileCards.append(card);

        // Bind the click event to the remove button
        card.find('.remove-button').on('click', function(event) {
          event.stopPropagation(); // Stop event propagation to prevent file input from opening
          removeFileFromInput(file);
          card.remove(); // Remove the file card
        });
      };
      reader.readAsDataURL(file);
    }
  }

  // Function to create a file card
  function createFileCard(file, imageData) {
    const card = $(
      `<div class="file-card">
        <img src="${imageData}" alt="${file.name}" width="100" height="100">
        <div class="file-size">${formatFileSize(file.size)}</div>
        <div class="remove-button">Remove File</div>
      </div>`
    );
    return card;
  }

  // Function to format file size
  function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';

    const k = 1024;
    const sizes = ['Bytes', 'KiB', 'MiB', 'GiB', 'TiB'];
    const i = parseInt(Math.floor(Math.log(bytes) / Math.log(k)));

    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }

  // Event listener for clicking the drop zone to open file input dialog
  dropzone.on('click', function() {
    fileInput[0].click();
  });

  // Event listener for file input change
  fileInput.on('change', function() {
    const files = $(this)[0].files;
    handleFiles(files);
    // Clear the file input to allow selecting the same files again
    appendFilesToInput(files)
  });

  // Event listener for drag and drop
  dropzone.on('dragover', function(event) {
    event.preventDefault();
    dropzone.addClass('dragover');
  });

  dropzone.on('dragleave', function(event) {
    event.preventDefault();
    dropzone.removeClass('dragover');
  });

  dropzone.on('drop', function(event) {
    event.preventDefault();
    dropzone.removeClass('dragover');
    const files = event.originalEvent.dataTransfer.files;
    handleFiles(files);
    appendFilesToInput(files)
  });
});

function appendFilesToInput(files) {
  const fileInput = document.getElementById('file-input2');
  const currentFiles = Array.from(fileInput.files);

  // Add the new files to the current files
  for (const file of files) {
    currentFiles.push(file);
  }

  // Create a new DataTransfer object and set the updated files
  const dataTransfer = new DataTransfer();
  for (const file of currentFiles) {
    dataTransfer.items.add(file);
  }

  // Set the files using the dataTransfer object
  fileInput.files = dataTransfer.files;

  // Trigger a change event to update the file input's value
  fileInput.dispatchEvent(new Event('change'));
}




  function removeFileFromInput(fileToRemove) {
    const fileInput = document.getElementById('file-input2');
    const currentFiles = Array.from(fileInput.files);
  
    // Filter out the file to remove
    const updatedFiles = currentFiles.filter(file => file !== fileToRemove);
  
    // Create a new DataTransfer object and set the updated files
    const dataTransfer = new DataTransfer();
    for (const file of updatedFiles) {
      dataTransfer.items.add(file);
    }
  
    // Set the files using the dataTransfer object
    fileInput.files = dataTransfer.files;
  
    // Trigger a change event to update the file input's value
    fileInput.dispatchEvent(new Event('change'));
  }