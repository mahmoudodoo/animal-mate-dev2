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
    $(".delete-ads-button").click(function () {
        var button = $(this);
        var url = button.data("url");
        var animal_id = button.data("animal-id");

        $.ajax({
            type: "DELETE",
            url: url,
            data: {
                animal_id: animal_id,
            },
            success: function (data) {
                $("#ads_data").html(data); // Update the container with new data
                window.location.reload()
            },
            error: function (xhr, textStatus, errorThrown) {
                // Handle errors, if any
                console.error("Error:", errorThrown);
            },
        });
    });
});



