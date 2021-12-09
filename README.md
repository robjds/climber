# Climber
Climbing robot teleoperation and data capturing code, for a climbing robot which uses 5 Dynamixel servos and 2 Analogue servos. The code is glueware that uses the 'easy dynamixel helper' (https://github.com/ryul1206/easy-dynamixel-helper) library to teleoperate the robot using a keyboard and terminal window.  

Keyboard.py allows you to control the robot with keyboard presses via terminal. Arrow keys drive the robot, 'K' stops movement. the A/S keys and Z/X keys open and close the front and back legs.

movementFunctions.py contains the functions used by Keyboard.py to turn the wheels and talk to the dynamixels

sensor_logging.py records IMU and distance sensor data to a csv file, and will record motor positions, speeds and torques via a pickle file, which is updated by Keyboard.py when it is running.

logged csv data is saved when the sensor_logging.py is terminated and are saved as 'DataRun0.csv' with filenames sequentially generated.

The .json files define the dynamixels for the four whegs and tail motor, which have the following ID numbers: 1 = front left, 2 = front right, 3 = back left, 4 = back right, 5 = tail.

Raspberry pi connections / pin numbers are as follows:

Servo1 : GPIO 3 (BOARD 15)
Servo2 : GPIO 4 (BOARD 16)
ToF interrupt: GPIO 0
IMU fsync: GPIO 7

IMU : I2C on pins 3 (SDA) and 5 (SCL)
ToF : I2C on pins 3 (SDA) and 5 (SCL)
Dynamixel Bus : USB
