# -*- coding: utf-8 -*-
"""
Spyder Editor

ex_14
"""
import urllib
import json
import ssl
print("Hello welcome to Ex 14\n")


""" Ex_14_01 """

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
# api_key = "AIzaSyB3PIgqRUE4ui8J7hHOpin0V1hlivULfik"
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    location = input("Enter location - ")
    if len(location) < 1: 
        break
    
    ## convert location to geocode
    parms = dict()
    parms['address'] = location
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    
    print("Retriving", url, "...")
    
    ## Open url
    fhand = urllib.request.urlopen(url, context = ctx)
    data = fhand.read().decode()
    print("Retrieved", len(data), "characters")
    
    ## Load data
    try:
        js = json.loads(data)
    except:
        js = None
        print("could not load")
        
    if not js or 'status' not in js or js['status'] != "OK":
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    
    ## Print data
    print(json.dumps(js, indent=5))
    print("\n ========= data loaded succesfully ========= \n")
    
    ## Get state id
    state = js["results"][0]["formatted_address"].split(',')
    state_id = state[1]
    print("====== state ID is ==== :" , state_id)


