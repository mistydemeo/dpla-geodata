# Augmentation of DPLA Geospatial Data With OpenStreetMaps Reverse Lookups
# Takes existing DPLA item records with geospatial elements ('dpla_geodata.json') and uses MapQuest's OpenStreetMaps reverse lookup API to include OSM hierarchy and feature data
# Only works where a record has existing lattitude/longitude coordinates
# NOTE: this does not produce DPLA item records, it just takes the existing DPLA item records and adds the new OSM field in
# OSM data is licensed under the Open Data Commons Open Database License (http://opendatacommons.org/licenses/odbl/)
# The following license applies only to this script and not the data, which was initially extracted by Misty Demeo
# Copyright 2012 David Riordan
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


import simplejson as json
import requests
from ast import literal_eval

lookedupplaces = {}
calls = 0

def reverse(lat,lon):
	payload = {'lat':lat,'lon':lon}
	global calls
	calls += 1
	print calls
	return json.loads(requests.get("http://open.mapquestapi.com/nominatim/v1/reverse?format=json",params=payload).text)




geo = json.loads(open('dpla_geodata.json','r').read())


for item in geo:
	if "spatial" in item:
		for place in item["spatial"]:
			if 'coordinates' in place:
				coordinates = place['coordinates']

				
				try:
					#Use local cache if it hasn't been looked up before
					if coordinates not in lookedupplaces:
						print "getting %s at %s" %(place['name'], coordinates)
						lat,lon = literal_eval(coordinates)
						lookedupplaces[coordinates]=reverse(lat,lon)

					#assign to json
					place['osm']=lookedupplaces[coordinates]
				except TypeError:
					print "skipping that one - it sucks"
final = json.dumps(geo)
f = open('geo-with-osm.json', 'wb')
f.write(final.encode('utf-16'))












"""
	#iterate over the set of places
	for namedplace in item:


		#determine if there's a spatial data in the place
		if "spatial" in namedplace:
			print item

			print namedplace
			place = namedplace['spatial']

			#determine if there are coordinates
			if 'coordinates' in place:

				print "it's a keeper!"
				coordinates = place['coordinates']

				#Use local cache if it hasn't been looked up before
				if coordinates not in lookedupplaces:
					print "getting %s at %s" %(place['name'], coordinates)
					lookedupplaces[coordinates]="String goes here!"

				#assign to json
				place['osm']=lookedupplaces[coordinates]


print geo[50]
"""