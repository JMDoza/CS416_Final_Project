$(document).ready(function () {

    // Creating map options
    const mapOptions = {
        center: [41.44218993074932, -72.83709282396603],
        zoom: 15
    };

    // Creating a map object
    const map = new L.map('map', mapOptions);

    // Creating a Layer object
    const layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

    // Adding layer to the map
    map.addLayer(layer);

    const markers = L.featureGroup([new L.marker([41.44218993074932, -72.83709282396603])]);
    map.addLayer(markers);


    $('#search').click(function () {
        markers.clearLayers();
        map.locate({enableHighAccuracy: true});
        map.on('locationfound', function (event) {
            L.circle(event.latlng, event.accuracy).addTo(map);
            map.flyTo(event.latlng, 10)

            $('#results').empty();

            const searchTerm = "animal shelter";
            const corsAnywhereURL = 'https://cors-anywhere.herokuapp.com/';

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
                    const totalResults = data.total;
                    if (totalResults > 0) {
                        $.each(data.businesses, function (i, item) {

                            const phone = item.display_phone;
                            const image = item.image_url;
                            const name = item.name;
                            const distance = displayDistance(item.distance);
                            const address = item.location.address1;
                            const city = item.location.city;
                            const zipcode = item.location.zip_code;
                            const latitude = item.coordinates.latitude;
                            const longitude = item.coordinates.longitude;

                            markers.addLayer(new L.marker([latitude, longitude]))

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
                        });
                    } else {
                        $('#results').append('<h5>No results were found!</h5>');
                    }

                }
            });
        });


    });

    $('#location').click(function () {
        markers.clearLayers();
        markers.addLayer(L.marker(mapOptions.center))
        map.flyTo(mapOptions.center, mapOptions.zoom)
    })

    function displayDistance(distance) {
        const milesPerMeter = 0.000621371;
        const distanceInMiles = distance * milesPerMeter;
        return distanceInMiles.toFixed(2) + 'mi';
    }

});