#!/usr/bin/env python

import json
import urllib
import urllib.parse
import urllib.request
import os


def main():
    city = "Leiria,pt"
    api_key = "2b2afaf78c88ac55d3e2127d280f0dbc"

    try:
        data = urllib.parse.urlencode({'q': city, 'appid': api_key, 'units': 'metric'})
        weather = json.loads(urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?' + data)
            .read())
        desc = weather['weather'][0]['description'].capitalize()
        temp = int(float(weather['main']['temp']))
        #return '{}, {}°F'.format(desc, temp)
        return '{}°C'.format(temp)
    except:
        return ''


if __name__ == "__main__":
	print(main())

