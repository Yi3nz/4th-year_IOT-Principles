#Sarah Yun Tiong, x14111187, BSHC in IOT, 2017

import dweepy, grovepi, math, time, config
from grovepi import *

#Connected ports
sound_sensor = 0       # A0
light_sensor = 1       # A1
tem_and_hu_sensor = 2  # D2
led = 3                # D3
button = 4             #D7
buzzer = 8             #D8

#Mode
pinMode(button, "INPUT")
pinMode(led, "OUTPUT")

#Get the value from the sensors
def getTemperature():
    [tem, hum] = grovepi.dht(tem_and_hu_sensor, 0)
    return tem
    
def getHumidity():
    [tem, hum] = grovepi.dht(tem_and_hu_sensor, 0)
    return hum

def getButton():
    return digitalRead(button)
    
def getLed():
    return digitalRead(led)    

#Send the information to my dweet TrackingDV
def post(dic):
    #thing = 'TrackingDV'
    thing = config.thing
    print dweepy.dweet_for(thing, dic)
 
 
 
 def getDweetContent(st_sensor, sensor):
	st_sensor = content["{}Switch".format(sensor)]
 
 
 
 
 
#Get the information and store in a dictionary
def getReadings():
    dict = {}
    dict["Temperature"] = getTemperature();
    dict["Humidity"] = getHumidity();
    dict["Button"] = getButton();
    dict["LED"] = getLed();
    dict["Greeting"] = config.greet;
    return dict

while True:
    try:
        if digitalRead(button) : #If the button is pressed, light the led.
            digitalWrite(led, 1)
        else:
            digitalWrite(led, 0)
        
        dict = getReadings();
        post(dict)
        time.sleep(1)

    except IOError:
        print config.ioE #Print string from config.py

    except:
        print config.extE #Print string from config.py
