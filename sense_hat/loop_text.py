from sense_hat import SenseHat

sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 255)

message = "WEATHER.GRILLI.TECH is awesome!!"

speed = 0.05

while True:
	sense.show_message(message, speed, text_colour=yellow, back_colour=blue)
