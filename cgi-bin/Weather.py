#! /usr/bin/env python3

import json
import requests
import json
import cgi


form = cgi.FieldStorage()
#city_name = "Kyoto"
city_name = form.getvalue('city','Kyoto')


API_KEY = "d01ed74f13d285ba9f785fb49335bf3a"

api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

url = api.format(city = city_name, key = API_KEY)
response = requests.get(url)
data = response.json()
jsonText = json.dumps(data, indent=4)


city = data["name"]
icon = data["weather"][0]["icon"]
temp = data["main"]["temp"]
temp_min = data["main"]["temp_min"]
temp_max = data["main"]["temp_max"]

humidity = data["main"]["humidity"]
speed = data["wind"]["speed"]


#print(jsonText)

print("Content-type: text/json\n")

weather = {"city": city, "icon": icon, "temp": temp,"temp_min": temp_min, "temp_max": temp_max, "humidity": humidity, "speed": speed}
#weather = {"city": "name","icon": "0d", "humidity": "main"}

print(json.dumps(weather))