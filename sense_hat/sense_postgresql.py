#!/usr/bin/python
from sense_hat import SenseHat
from datetime import datetime
from time import sleep
from threading import Thread
import psycopg2

try:
    conn = psycopg2.connect("dbname='zipcode' user='postgres' host='localhost' password=''")

except: print("I am unable to connect to the databse")

TEMP=True
TEMP_H=True
TEMP_P=True
HUMIDITY=True
PRESSURE=True
MAG=True
DELAY=30 

def log_data(tempH, tempP, hum, press, mag, dt):
    print(temp, tempH, tempP, hum, press, mag, dt)
    cur = conn.cursor()
    cur.execute("""INSERT INTO sensor_data(temp_h, temp_p, humidity, pressure, mag, datetime) 
     VALUES (%s, %s, %s, %s, %s, %s, %s)""", (temp, tempH, tempP, hum, press, mag, dt ));
    conn.commit()
    
def get_sense_data():
    sense = SenseHat()
    if TEMP
      temp = sense.get_temperature()
    
    if TEMP_H:
        tempH = sense.get_temperature_from_humidity()
        

    if TEMP_P:
        tempP = sense.get_temperature_from_pressure()
        

    if HUMIDITY:
        hum = sense.get_humidity()
      

    if PRESSURE:
        press = sense.get_pressure()

    if MAG:
        mag = sense.get_compass()

    dt= datetime.now()
    
    return(far(tempH), far(tempP), hummer(hum), bar(press), round(mag, 2), dt)
    
def timed_log():
    while True:
      log_data(*datalist)
      sleep(DELAY)
      
def far(temp):
  return round(((temp / 5 * 9) - 20) + 32, 1)
  
def bar(pressure):
  return round((pressure * 0.02952998751),1)

def hummer(humidity):
  return round(humidity, 1)

##### Main Program #####
sense=SenseHat()
while True:
    if DELAY > 0:
      datalist = get_sense_data()
      Thread(target = timed_log).start()
    
    if DELAY == 0:
      datalist = get_sense_data()
      log_data(*datalist)
    