# sudo pip install smbus2
# sudo pip install vl53l1x
# https://github.com/pimoroni/vl53l1x-python

# sudo pip install mpu9250
# https://github.com/MomsFriendlyRobotCompany/mpu9250

import os
import csv
import time

import VL53L1X

from mpu9250 import mpu9250
from time import sleep

i = 0
while os.path.exists("DataRun%s.csv" % i):
    i += 1

headerRow = ['time', 'tof', 'aX', 'aY','aZ', 'gX', 'gY','gZ', 'mX', 'mY','mZ','temp']
ouputFile = open("DataRun%s.csv" % i, "w")
with ouputFile:
   writer = csv.writer(ouputFile)
   writer.writerows(headerRow)

tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open() # Initialise the i2c bus and configure the sensor
tof.start_ranging(1) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range

imu = mpu9250()

print 'log started'
startTime = time.process_time()

try:
	while True:

        currentTime =  time.process_time() - startTime

        distance_in_mm = tof.get_distance() # Grab the range in mm

		gyr = imu.gyro
		magn = imu.mag
		temp = imu.temp
        acce = imu.accel

        outputData = ['{:.3}'.format(currentTime) ,
                      '{:.3}'.format(distance_in_mm) ,
                      '{:.3f},{:.3f},{:.3f}'.format(*acce) ,
                      '{:.3f},{:.3f},{:.3f}'.format(*gyr) ,
                      '{:.3f},{:.3f},{:.3f}'.format(*magn) ,
                      '{:.3}'.format(temp)]

        with ouputFile:
            writer.writerows(outputData)

except KeyboardInterrupt:
    tof.stop_ranging() # Stop ranging
    ouputFile.close();
	print 'bye ...'
