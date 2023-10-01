$(document).ready(function() {
    $('#country_animal').change(function() {
        var selectedCountry = $(this).val();
        var cityFormSelect = $('#city_form');
        var url = $(this).data("url");
        $.ajax({
            url: url,  
            data: {'selected_country': selectedCountry},
            dataType: 'json',
            success: function(data) {
                // Clear existing options
                cityFormSelect.empty();

                // Add the new options based on the retrieved data
                cityFormSelect.append('<option value="">---------</option>');
                $.each(data.cities, function(index, city) {
                    cityFormSelect.append('<option value="' + city + '">' + city + '</option>');
                });

                // Enable the city_form select input
                cityFormSelect.prop('disabled', false);
            },
            error: function(xhr, status, error) {
                console.error('Error fetching cities:', error);
            }
        });
    });



    $('#delete-animal').click(function(event) {
        event.preventDefault(); // Prevent the form submission
    
        var url = $(this).data("url");
        var secondUrl = $(this).data("secondurl");
        var confirmDelete = confirm("Are you sure you want to delete this cat?");
        
        if (confirmDelete) {
          $.ajax({
            url: url,
            type: 'DELETE', // Use the DELETE method
            data: { csrfmiddlewaretoken: '{{ csrf_token }}' }, // Include CSRF token
            success: function(data) {
              // Handle success response here
              console.log("Cat deleted successfully!");
              
              // Redirect the user to data-secondurl after deletion
              window.location.href = secondUrl;
            },
            error: function(xhr, status, error) {
              // Handle error response here
              console.log("Error deleting cat.");
              console.error('Error deleting animal:', error);
            }
          });
        }
      });


});


