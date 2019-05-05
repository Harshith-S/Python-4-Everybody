"""
Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. 
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. 
A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. 
If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to provide address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in 
http://www.py4e.com/code3/geojson.py

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJNeHD4p-540AR2Q0_ZjwmKJ8".

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2021 characters
Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8
Turn In

Please run your program to find the place_id for this location:

University of Greifswald
Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJ36_ ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. 
Your program should work with the Google API - but the place_id may not match for this assignment.
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
	api_key = 42
	serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
	serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
	address = input('Enter location: ')
	if len(address) < 1: break

	parms = dict()
	parms['address'] = address
	if api_key is not False: parms['key'] = api_key
	url = serviceurl + urllib.parse.urlencode(parms)

	print('Retrieving', url)
	uh = urllib.request.urlopen(url, context=ctx)
	data = uh.read().decode()
	print('Retrieved', len(data), 'characters')

	try:
		js = json.loads(data)
	except:
		js = None

	if not js or 'status' not in js or js['status'] != 'OK':
		print('==== Failure To Retrieve ====')
		print(data)
		continue

	print(json.dumps(js, indent=4))
 
	place_id = js["results"][0]["place_id"]
	print("Place id", place_id)