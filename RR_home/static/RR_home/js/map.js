function initMap() {
            var map = new google.maps.Map(document.getElementById("map"), {
                zoom: 8,
                center: {
                    lat:56.007120,
                    lng:-3.709860
                }
            });

            var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            var locations = [
                {lat:56.006481, lng:-3.713440},
                {lat:56.007120, lng:-3.709860},
                {lat:56.0094028, lng:-3.7107378}
            ];

            var markers = locations.map(function(location, i){
                return new google.maps.Marker({
                    position: location,
                    label: labels[i % labels.length],
                
                });
            });
            var markerCluster = new MarkerClusterer(map, markers, {
                imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
            });
        }