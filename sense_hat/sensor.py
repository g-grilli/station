#!usr/bin/env python 3
from sense_hat import SenseHat

sense = SenseHat() 
<<<<<<< HEAD
t = sense.get_temperature()
h = sense.get_humidity()
p = sense.get_pressure()

def temperature(t):
  return round((t / 5 * 9) + 32, 1)
  
def bar(p):
  return round((p / 0.02952998751, 1))

def hum(h):
  return round(humidity)

msg = "Temperature = {temperature(t)}, Barometric Pressure = {bar(p)}, Humidity = {hum(h)}".format(t,p,h)
sense.show_message(msg, scroll_speed=0.05)
=======
temp = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

def temperature(temp):
  return round((temp / 5 * 9) + 32, 1)
  
def bar(pressure):
  return round((pressure / 0.02952998751, 1))

def hum(humidity):
  return round(humidity)

print("Temperature: %s C" % temp)
>>>>>>> 5573cffbb1773dba35e2138d95706b60450fe916
