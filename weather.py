#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyowm
import datetime

now = datetime.datetime.now()

owm = pyowm.OWM('b9249fc85f6f44bb0f5156f74b11761d', language = "RU")

observation = owm.weather_at_place('Brest, BY')
w = observation.get_weather()


print("Дата: " + now.strftime("%d.%m.%Y")) 
print("Время: " + now.strftime("%H:%M"))
print("------------------------------------------------")
print("Давление: " + str( w.get_pressure()['press'] ) + " мбар")
print("Облачность: " + str( w.get_detailed_status() ))
print("Скорость ветра: " + str(w.get_wind()['speed'] * 3.6) + " км/ч")
print("Влажность: " + str( w.get_humidity() ) + " %")
print("Температура: " + str( w.get_temperature('celsius')['temp'] ) + " °C")