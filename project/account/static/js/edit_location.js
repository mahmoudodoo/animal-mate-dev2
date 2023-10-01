// edit_location.js

// Function to set the map view based on the user's location
function setMapView() {
    // Get the user's location from the data-location attribute of the map div
    var mapDiv = document.getElementById('map');
    var userLocation = mapDiv.getAttribute('data-location');

    // Parse the user's location into a coordinate array
    var coordinates = userLocation.split(',').map(parseFloat);

    if (coordinates.length === 2) {
        var map = L.map('map').setView(coordinates, 7); // Set the zoom level to 7

        // Add a tile layer
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

        // Add a default location marker
        var defaultMarker = L.marker(coordinates).addTo(map);

        // Initialize a marker for user interaction
        var marker;

        // Add a marker when the user clicks on the map
        map.on('click', function (e) {
            if (marker) {
                marker.setLatLng(e.latlng);
            } else {
                marker = L.marker(e.latlng).addTo(map);
            }

            // Update the hidden input field with the selected location
            document.getElementById('location').value = e.latlng.lat + ',' + e.latlng.lng;
        });
    }
}

// Function to handle form submission
function saveLocation() {
    // You can access the selected location from the hidden input field
    var locationValue = document.getElementById('location').value;

    // Perform any additional client-side validation if needed

    // Submit the form
    document.getElementById('post_form').submit();
}

// Call the setMapView function to set the initial map view
setMapView();
