import json
import codecs
from urllib.request import urlopen
import string
from datetime import datetime
from .models import weather_data

def climate():
    high =[]
    low =[]
    day =[]
    dat =[]
    city = ['nagercoil', 'tirunelveli', 'chennai', 'coimbatore', 'madurai','tiruchirappalli','tuticorin','salem', 'erode', 'theni']
    for c in city:
        with urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22'+c+'%2C%20IND%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys') as url:
            data = url.read().decode()
        weather_json = json.loads(data)
        data_location = weather_json["query"]['results']['channel']['location']
        wind_dir = weather_json["query"]['results']['channel']['wind']['direction']
        wind_speed = weather_json["query"]['results']['channel']['wind']['speed']
        sunraise = weather_json["query"]['results']['channel']['astronomy']["sunrise"]
        place = data_location['city']

        data_item = weather_json["query"]['results']['channel']['item']
        fore_cast = data_item['forecast'][0]['text']
        temp = data_item['condition']['temp']
        date = data_item['condition']['date']
        data_image= weather_json["query"]['results']['channel']['image']
        for j in range(9):
            high.append(data_item['forecast'][j]['high'])
            low.append(data_item['forecast'][j]['low'])
            day.append(data_item['forecast'][j]['day'])
            dat.append(data_item['forecast'][j]['date'])
        data_location = weather_json["query"]['results']['channel']['location']['city']
        wind = weather_json["query"]['results']['channel']['wind']
        atmos =weather_json["query"]['results']['channel']['atmosphere']
        astronomy= weather_json["query"]['results']['channel']['astronomy']
        humidity= weather_json["query"]['results']['channel']['atmosphere']['humidity']
        presure= weather_json["query"]['results']['channel']['atmosphere']['pressure']
        visibility= weather_json["query"]['results']['channel']['atmosphere']['visibility']
        condition = weather_json["query"]['results']['channel']['item']['condition']
        time = condition['date'][17:25]
        temp = condition['temp']
        place = data_location
        t = str(datetime.now())
        z = weather_data.objects.latest('time')

        if str(z) != t[11:16]:
            print(t[11:16])
            k = datetime.now()
            full = str(k)
            date = full[0:10]

            w = weather_data(place=place, wind_speed=wind_speed, wind_direction=wind_dir, time=t[11:16],
                             temp=temp, astronomy=sunraise, date=date, presure=presure, humidity=humidity,
                             visibility=visibility)
            w.save()

        #print(presure)

