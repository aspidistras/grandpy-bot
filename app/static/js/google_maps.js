let map;
let coordinates = {lat: 48.866667, lng: 2.333333};

function initMap() {
	let options = {
		zoom: 3,
		center: coordinates,
	};
	map = new google.maps.Map(document.getElementById('map'), options);

	let marker = new google.maps.Marker({
		position: coordinates,
		map: map,
		title: 'Paris'
	});
	marker.setMap(map);

}
google.maps.event.addDomListener(window, "load", initialize);