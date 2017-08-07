#!/usr/bin/python
from sense_hat import SenseHat
from datetime import datetime
from time import sleep
from threading import Thread
import psycopg2

try:
    conn = psycopg2.connect("dbname='zipcode' user='postgres' host='localhost' password=''")

except: print("I am unable to connect to the databse")

temp_h=True
temp_p=True
hummidity=True
pressure=True
MAG=True
delay=900

def log_data(tempH, tempP, hum, press, mag, dt):
    print(tempH, tempP, hum, press, mag, dt)
    cur = conn.cursor()
    cur.execute("""INSERT INTO sensor_data(temp_h, temp_p, humidity, pressure, mag, datetime) 
     VALUES (%s, %s, %s, %s, %s, %s)""", (tempH, tempP, hum, press, mag, dt ));
    conn.commit()
    
def get_sense_data():
    sense = SenseHat()
    
    if temp_h:
        tempH = sense.get_temperature_from_humidity()
        

    if temp_p:
        tempP = sense.get_temperature_from_pressure()
        

    if hummidity:
        hum = sense.get_humidity()
      

    if pressure:
        press = sense.get_pressure()

    if MAG:
        mag = sense.get_compass()

    dt= datetime.now()
    
    return(far(tempH), far(tempP), hummer(hum), bar(press), round(mag, 2), dt)
    
def timed_log():
    while True:
      datalist = get_sense_data()
      log_data(*datalist)
      sleep(delay)

def untimed_log():
    while True:
      datalist = get_sense_data()
      log_data(*datalist)
      sleep(1)
      
def far(temp):
  return round(((temp / 5 * 9) - 23) + 32, 1)
  
def bar(pressure):
  return round((pressure * 0.02952998751),1)

def hummer(humidity):
  return round(humidity, 1)

##### Main Program #####
sense = SenseHat()

if delay > 0:
 Thread(target = timed_log).start()

else:
 Thread(target = untimed_log).start()
    