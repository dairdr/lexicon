/**
 * @fileoverview Result Controller Module for 'words' webapp.
 *
 * @author Dair 'daro' Díaz
 * @version 1.0.0
 */
var Words = (function(w){
	var _window = w || window;
	var $ = window.jQuery || $;
	var _console = (window.console = window.console || {});
	var _config = {
		name: 'result controller',
		map: {
			initialLatitude: 8.418020821312428,
			initialLongitude: -75.83859804687492
		},
		events: {
			click: 'click',
			ready: 'ready'
		}
	};
	var static_url = 'http://localhost:8000/static/dictionary/';
	var mapsLayer = [
		{
			id: 1,
			layer: [
				static_url + 'kml/cordoba.kml'
			]
		},
		{
			id: 2,
			layer: [
				static_url + 'kml/alto_sinu.kml',
				static_url + 'kml/medio_sinu.kml',
				static_url + 'kml/bajo_sinu.kml',
				static_url + 'kml/san_jorge.kml',
				static_url + 'kml/zona_costanera.kml'
			]
		},
		{
			id: 3,
			layer: [
				static_url + 'kml/alto_sinu.kml',
				static_url + 'kml/medio_sinu.kml',
				static_url + 'kml/bajo_sinu.kml',
				static_url + 'kml/san_jorge.kml'
			]
		},
		{
			id: 4,
			layer: [
				static_url + 'kml/alto_sinu.kml',
				static_url + 'kml/medio_sinu.kml',
				static_url + 'kml/bajo_sinu.kml'
			]
		},
		{
			id: 5,
			layer: [
				static_url + 'kml/alto_sinu.kml',
				static_url + 'kml/medio_sinu.kml'
			]
		},
		{
			id: 6,
			layer: [
				static_url + 'kml/alto_sinu.kml'
			]
		},
		{
			id: 7,
			layer: [
				static_url + 'kml/zona_sabanera.kml'
			]
		},
		{
			id: 8,
			layer: [
				static_url + 'kml/zona_costanera.kml',
				static_url + 'kml/zona_sabanera.kml'
			]
		},
		{
			id: 9,
			layer: [
				static_url + 'kml/san_jorge.kml',
				static_url + 'kml/zona_costanera.kml',
				static_url + 'kml/zona_sabanera.kml'
			]
		},
		{
			id: 10,
			layer: [
				static_url + 'kml/bajo_sinu.kml',
				static_url + 'kml/san_jorge.kml',
				static_url + 'kml/zona_costanera.kml',
				static_url + 'kml/zona_sabanera.kml'
			]
		},
		{
			id: 11,
			layer: [
				static_url + 'kml/medio_sinu.kml',
				static_url + 'kml/bajo_sinu.kml',
				static_url + 'kml/san_jorge.kml',
				static_url + 'kml/zona_costanera.kml',
				static_url + 'kml/zona_sabanera.kml'
			]
		}
	];

	/**
	 * Inicializa el modulo.
	 *
	 */

	function init(){
		createMap();
	};

	/**
	 * Crea el mapa con la API de Google Maps.
	 *
	 * Crea el mapa y muestra las capas correspondientes a la palabra que
	 * se esta buscando.
	 *
	 */
	function createMap(){
		var mapOptions = {
			center: new google.maps.LatLng(_config.map.initialLatitude, _config.map.initialLongitude),
			zoom: 8,
			maptypeId: google.maps.MapTypeId.ROADMAP
		}
		var mapContainer = $('#map-container')[0];
		var map = new google.maps.Map(mapContainer, mapOptions);
		/* Determinar cual capa mostrar segun el tipo de mapa */
		var mapId = parseInt($(mapContainer).attr('map-type'));
		$.each(mapsLayer, function(index, value){
			if(value.id == mapId){
				$.each(value.layer, function(i, v){
					new google.maps.KmlLayer(v).setMap(map);
				});
			}
		});
	};

	return {
		init: init,
		config: _config
	}
})(window);

if(window.jQuery)
	$(document).on(Words.config.events.ready, Words.init);