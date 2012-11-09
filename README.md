DPLA geodata
============

A simple offline copy of all current DPLA records containing geodata. Contains 36752 records!

The items are present in one JSON array, otherwise in the original DPLA API v1 format.


# Now with OpenStreetMaps augmentation
Also includes the script osm-augmentation.py which augments these records with OSM data where possible.
OSM augmentation looks like this: http://open.mapquestapi.com/nominatim/#reverse
{"place_id":"2173682858","licence":"Data Copyright OpenStreetMap Contributors, Some Rights Reserved. CC-BY-SA 2.0.","osm_type":"way","osm_id":"26996903","lat":"51.5217631080199","lon":"-0.162805741002427","display_name":"The Landmark, Melcombe Place, Marylebone, City of Westminster, Greater London, London, England, NW1 5QD, United Kingdom","address":{"hotel":"The Landmark","road":"Melcombe Place","suburb":"Marylebone","city":"City of Westminster","county":"Greater London","state_district":"London","state":"England","postcode":"NW1 5QD","country":"United Kingdom","country_code":"gb"}}