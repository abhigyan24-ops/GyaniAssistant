
import webbrowser
import requests
import json

# replace 'New York City' with the location you want to search for
url = 'https://www.google.com/maps/search/?api=1&query=New+York+City'

# open the webbrowser
webbrowser.open_new_tab(url)

# make request to Google Maps API
r = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=New+York+City&destination=Boston&key=AIzaSyBWv8wIDX-xxii6thENzwE7nOf_dcT-4CQ')

# parse the response
json_data = json.loads(r.text)

# print the total time and total km
total_time = json_data['routes'][0]['legs'][0]['duration']['text']
total_km = json_data['routes'][0]['legs'][0]['distance']['text']
print("Total Time: " + total_time)
print("Total Distance: " + total_km)