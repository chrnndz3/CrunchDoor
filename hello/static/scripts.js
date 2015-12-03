

$('#search').click(function(event){
	event.preventDefault();
	var searchText = $('#searchText').val();
  orderBy = "name";
	if(searchText === undefined || searchText ==='')
		searchText = 'all';
	document.location.href = '/crunchDoorApp/companies/'+searchText + '/'+ orderBy;
});

$('#update-filter').click(function(event){
	event.preventDefault();
	var searchText = $('#searchText').val();
  var orderBy = $('#orderBy').val();
  if(searchText === 'all'){
    alert("Sorry, 'all' is a reserved keyword. Try another search word.");
    return;
  }
	if(searchText === undefined || searchText === "")
		document.location.href = '/crunchDoorApp/companies/all/'+ orderBy;
  else
	document.location.href = '/crunchDoorApp/companies/'+searchText + '/'+ orderBy;
});





// var map;
// var marker ='';
// var sv;
// initMap = function() {
//  	sv = new google.maps.StreetViewService();

//   // Set up the map.
//   map = new google.maps.Map(document.getElementById('map'), {
//   	zoom: 10,
//   	streetViewControl: false,
//   }) ;
//   map.setCenter({lat:37.633394, lng:-122.239849});


//   //add event listener for guessLocation

//   map.addListener('click', function(event) {

//   		if(marker !== '')
//   			marker.setMap(null);
//   		marker =  new google.maps.Marker({
//   			position: event.latLng,
//   			icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
//   			animation: google.maps.Animation.DROP,
//   			map: map
//   		});

  	
//   });
// }