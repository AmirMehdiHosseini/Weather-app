import requests
import json
import time

api_key = '78392b6773396310bfcef5c2d6967491'


main_url = "http://api.openweathermap.org/data/2.5/weather?"


city = input()


complete_url = main_url + "appid=" + api_key + "&q=" + city


res = requests.get(complete_url)


json_info = res.json()


if json_info['cod'] != '404':


    temp       = json_info['main']
    min_temp   = int(float(temp['temp_min']) - 273.15)
    max_temp   = int(float(temp['temp_max']) - 273.15)
    temp_now   = int(float(temp['temp']) - 273.15)
    humidity   = str(temp['humidity']) + ' %'
    pressure   = temp['pressure']
    sunrise    = time.strftime('%I:%M:%S' , time.gmtime(json_info['sys']['sunrise'] - 21600))
    sunset     = time.strftime('%I:%M:%S' , time.gmtime(json_info['sys']['sunset'] - 21600))
    wind_speed = json_info['wind']['speed']
    name       = json_info['name']
    wtr        = json_info['weather']
    condition  = wtr[0]['description']

    