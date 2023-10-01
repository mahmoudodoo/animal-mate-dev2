$(document).ready(function(){
    $('.slideshow-container').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000, // Adjust the autoplay speed in milliseconds
        dots: true,
        draggable: true, // Enables mouse dragging
        prevArrow: false, // Remove the prev arrow
        nextArrow: false, // Remove the next arrow
    });
});

$(document).ready(function () {
    // Attach a click event handler to the buttons with the "delete-fav-button" class
    $(".delete-fav-button").click(function () {
        var button = $(this);
        var url = button.data("url");
        var animal_id = button.data("animal-id");
        var csrf_token = $("input[name=csrfmiddlewaretoken]").val(); // Get the CSRF token from the input field

        $.ajax({
            type: "POST",
            url: url,
            data: {
                animal_id: animal_id,
                csrfmiddlewaretoken: csrf_token, // Include the CSRF token in the data
            },
            success: function (data) {
                $("#fav_data").html(data); // Update the container with new data
            },
            error: function (xhr, textStatus, errorThrown) {
                // Handle errors, if any
                console.error("Error:", errorThrown);
            },
        });
    });
});



