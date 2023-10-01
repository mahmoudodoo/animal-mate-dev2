$(document).ready(function() {
    // Handle country selection change
    $('#countryCode').on('change', function() {
        var selectedCountry = $(this).val();        
        // Set the mobile number field with the selected country code
        $('#id_mobile_number').val('+' + selectedCountry);
    });

    // Disable editing of the mobile number field
    $('#id_mobile_number').on('input', function() {
        var inputValue = $(this).val();
        if (!inputValue.startsWith('+' + selectedCountry)) {
            // If the input doesn't start with the country code, reset it
            $(this).val('+' + selectedCountry);
        }
    });
});