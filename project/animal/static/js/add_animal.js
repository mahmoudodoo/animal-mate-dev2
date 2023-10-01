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
                
                if(data.cities.length===0){
                    cityFormSelect.append('<option value="' + selectedCountry + '">' + selectedCountry + '</option>');
                }

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
});

