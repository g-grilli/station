##### Libraries #####
from sense_hat import SenseHat
from datetime import datetime
from time import sleep
from threading import Thread

##### Logging Settings #####
TEMP_H=True
TEMP_P=False
HUMIDITY=True
PRESSURE=True
ORIENTATION=False
ACCELERATION=False
MAG=False
GYRO=False
DELAY=5

FILENAME = "Fall"
WRITE_FREQUENCY = 1

##### Functions #####
def file_setup(filename):
    sense_data=[]
    if TEMP_H:
      sense_data.append("temp_h")
    if TEMP_P:
      sense_data.append("temp_p")
    if HUMIDITY:
      sense_data.append("humidity")
    if PRESSURE:
      sense_data.append("pressure")
    if ORIENTATION:
      sense_data.extend(["pitch","roll","yaw"])
    if MAG:
      sense_data.extend(["mag_x","mag_y","mag_z"])
    if ACCELERATION:
      sense_.extend(["accel_x","accel_y","accel_z"])
    if GYRO:
      sense_data.extend(["gyro_x","gyro_y","gyro_z"])

    sense_data.append(datetime.now())

    with open(filename,"w") as f:
        f.write(",".join(str(value) for value in sense_data)+ "\n")

def log_data():
    output_string = ",".join(str(value) for value in sense_data)
    batch_data.append(output_string)
    
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
      log_data()
      sleep(DELAY)



##### Main Program #####
sense = SenseHat()
batch_data= []

if FILENAME == "":
    filename = "SenseLog-"+str(datetime.now())+".csv"
else:
    filename = FILENAME+"-"+str(datetime.now())+".csv"

file_setup(filename)

if DELAY > 0:
    sense_data = get_sense_data()
    Thread(target= timed_log).start()
    
while True:
    if DELAY == 0:
        log_data()
    if len(batch_data) >= WRITE_FREQUENCY:
        print("Writing to file..")
        with open(filename,"a") as f:
            for line in batch_data:
                f.write(line + "\n")
            batch_data = []

  


