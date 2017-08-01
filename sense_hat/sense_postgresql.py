#!/usr/bin/python
from sense_hat import SenseHat
from datetime import datetime
from time import sleep
from threading import Thread
import psycopg2

try:
    conn = psycopg2.connect("dbname='zipcode' user='postgres' host='localhost' password=''")

except: print("I am unable to connect to the databse")

TEMP_H=True
TEMP_P=True
HUMIDITY=True
PRESSURE=True
MAG=True
DELAY=30

def log_data(tempH, tempP, hum, press, mag, dt):
    print(tempH, tempP, hum, press, mag, dt)
    cur = conn.cursor()
    cur.execute("""INSERT INTO sensor_data(temp_h, temp_p, humidity, pressure, mag, datetime) 
     VALUES (%s, %s, %s, %s, %s, %s)""", (tempH, tempP, hum, press, mag, dt ));
    conn.commit()
    
def get_sense_data():
    sense = SenseHat()

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
    
    return(tempH, tempP, hum, press, mag, dt)
    
def timed_log():
    while True:
      log_data(*datalist)
      sleep(DELAY)

##### Main Program #####
sense=SenseHat()
while True:
    if DELAY > 0:
      datalist = get_sense_data()
      Thread(target = timed_log).start()
    
    if DELAY == 0:
      datalist = get_sense_data()
      log_data(*datalist)
    