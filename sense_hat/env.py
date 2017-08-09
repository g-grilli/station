from sense_hat import SenseHat
sense = SenseHat()

def far(temp):
  return round(((temp / 5 * 9) - 23) + 32, 1)
  
def bar(pressure):
  return round((pressure * 0.02952998751),1)

def hummer(humidity):
  return round(humidity, 1)


while True:
    t = sense.get_temperature_from_pressure()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = far(t)
    p = bar(p)
    h = hummer(h)

    if t > 68 and t < 76:
        bg = (0, 100, 0)  # green
    else:
        bg = (0, 0, 100)  # blue

    msg = "Grilli.Tech is Awesome!  Current Conditions: Temperature = {0}, Pressure = {1}, Humidity - {2}".format(t, p, h)
    sense.set_rotation(180)
    sense.show_message(msg, scroll_speed=0.05, back_colour=bg)
