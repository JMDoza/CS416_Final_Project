$(document).ready(function () {

    // Creating map options
    var mapOptions = {
        center: [41.44218993074932, -72.83709282396603],
        zoom: 15
    }

    // Creating a map object
    var map = new L.map('map', mapOptions);

    // Creating a Layer object
    var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

    // Adding layer to the map
    map.addLayer(layer);

    var markers = L.featureGroup([new L.marker([41.44218993074932, -72.83709282396603])]);
    map.addLayer(markers);


    $('#search').click(function () {
        markers.clearLayers();
        map.locate({enableHighAccuracy: true});
        map.on('locationfound', function (event) {
            L.circle(event.latlng, event.accuracy).addTo(map);
            map.flyTo(event.latlng, 10)

            // Clear before adding in case the user clicks the button twice
            $('#results').empty();

            console.log(event.latlng.lat)

            // Get the search term and location from the input elements
            const searchTerm = "animal shelter";

            // This API enables cross-origin requests to anywhere
            // This will probably be very confusing for you to understand as to why we need another url in front of the actual url
            // However, browsers like Chrome prevents non-cross-origin requests, so this is a workaround for that
            // It’s basically a proxy that is used to bypass the CORS restrictions.
            // This site only serves requests after you visit the page below and temporarily unlock by clicking the button on this site.
            // More info: https://github.com/Rob--W/cors-anywhere/issues/301
            const corsAnywhereURL = 'https://cors-anywhere.herokuapp.com/';

            // You must enter your own API_KEY below
            const API_KEY = "t4WRnGUniwxt0AA6mCWujtrdnO0Ki7nSHOjprJJxrDeE2hYDOEss3K8ufBXT4vBdzCyPHojQi4OFO7ZFfnd35oWAHhJopazo2UYgG8MBgLZgTRpht2c_H_Vg1ampYXYx"

            $.ajax({
                url: corsAnywhereURL + 'https://api.yelp.com/v3/businesses/search',
                dataType: 'json',
                data: {'term': searchTerm, 'latitude': event.latlng.lat, 'longitude': event.latlng.lng},
                method: 'GET',
                headers: {
                    'Authorization': 'Bearer ' + API_KEY,
                },
                success: function (data) {
                    console.log(data);
                    // Grab the results from the API JSON return
                    const totalResults = data.total;
                    // If our results are greater than 0, continue
                    if (totalResults > 0) {
                        // Iterate through the JSON array of 'businesses' returned by the API
                        $.each(data.businesses, function (i, item) {

                            // Store each business's object in a variable
                            const business = item.id;
                            const phone = item.display_phone;
                            const image = item.image_url;
                            const name = item.name;
                            const distance = displayDistance(item.distance);
                            const address = item.location.address1;
                            const city = item.location.city;
                            const zipcode = item.location.zip_code;
                            const latitude = item.coordinates.latitude;
                            const longitude = item.coordinates.longitude;
                            const transactions = item.transactions;

                            markers.addLayer(L.marker([latitude, longitude]))

                            // Append our result into our page

                            $('#results').append('' +
                                '            <div class="">\n' +
                                '                  <div class="card staff business-color mb-3">\n' +
                                '                        <div class="row">\n' +
                                '                            <div class="col-sm-5">\n' +
                                `                                <img src="${image}" class="business-img" alt="business-image">\n` +
                                '                            </div>\n' +
                                '                            <div class="col-sm-7">\n' +
                                '                                <div class="card-body">\n' +
                                '                                    <div class="row">\n' +
                                '                                        <div class="col-sm-8">\n' +
                                `                                            <h4  class="card-title">${name}  </h4>\n` +
                                '                                        </div>\n' +
                                '                                        <div class="col-sm-4">\n' +
                                `                                            <small class="text-light">${distance}</small>\n` +
                                '                                            <br>\n' +
                                '                                        </div>\n' +
                                '                                    </div>\n' +
                                `                                    <p class="card-text text-light">${address} <br>${city}, ${zipcode}</p>\n` +
                                `                                    <p class="card-text text-light">Phone: ${phone}</p>\n` +
                                '                                </div>\n' +
                                '                            </div>\n' +
                                '                        </div>\n' +
                                '                    </div');
                            transactionGenerator(transactions, i);
                        });
                    } else {
                        // If our results are 0; no businesses were returned by the JSON therefore we display on the page no results were found
                        $('#results').append('<h5>No results were found!</h5>');
                    }

                }
            });
        });


    });

    // A function to convert from meters to miles
    function displayDistance(distance) {
        const milesPerMeter = 0.000621371;
        const distanceInMiles = distance * milesPerMeter;
        return distanceInMiles.toFixed(2) + 'mi';
    }

    function ratingGenerator(rating, index) {
        // 5-star rating generated via fa-star from fontAwesome
        for (let i = 0; i < 5; i++) {
            if (i < rating) {
                $('#rating-' + index).append('<span class="fa fa-star checked"></span>');
            } else {
                $('#rating-' + index).append('<span class="fa fa-star"></span>');
            }
        }
    }

    // A function to generate badge-pill for different transaction information of each business
    function transactionGenerator(transactions, index) {
        for (const transaction of transactions) {
            $('#transaction-' + index).append(`<span class="badge rounded-pill bg-primary ms-1">${transaction}</span>`);
        }
    }


});