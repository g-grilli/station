#!/usr/bin/python
from sense_hat import SenseHat
from datetime import datetime
from time import sleep
from threading import Thread
import psycopg2

try:
    conn = psycopg2.connect(dbname='zipcode' user ='postgres' host='localhost' password='')

except: print "I am unableto connect to the databse"

curr=conn.cursor()
TEMP_H=True
TEMP_P=True
HUMIDITY=True
PRESSURE=True
ORIENTATION=True
ACCELERATION=True
MAG=True
GYRO=True
DELAY=1800

def log_data():
    cur.execute(INSERT INTO sensor_data VALUES (sense_data));
    
def get_sense_data():
    sense_data=[]

    if TEMP_H:
        sense_data.append(sense.get_temperature_from_humidity())

    if TEMP_P:
        sense_data.append(sense.get_temperature_from_pressure())

    if HUMIDITY:
        sense_data.append(sense.get_humidity())

    if PRESSURE:
        sense_data.append(sense.get_pressure())

    if ORIENTATION:
        yaw,pitch,roll = sense.get_orientation().values()
        sense_data.extend([pitch,roll,yaw])

    if MAG:
        mag_x,mag_y,mag_z = sense.get_compass_raw().values()
        sense_data.extend([mag_x,mag_y,mag_z])

    if ACCELERATION:
        x,y,z = sense.get_accelerometer_raw().values()
        sense_data.extend([x,y,z])

    if GYRO:
        gyro_x,gyro_y,gyro_z = sense.get_gyroscope_raw().values()
        sense_data.extend([gyro_x,gyro_y,gyro_z])

    sense_data.append(datetime.now())

    return sense_data
    
def timed_log():
    while True:
      get_sense_data()
      log_data()
      sleep(DELAY)

##### Main Program #####
while True:
    if DELAY > 0:
        Thread(target= timed_log).start()
    
    if DELAY == 0:
        log_data()
    