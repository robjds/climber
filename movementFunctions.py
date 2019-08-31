
import RPi.GPIO as GPIO   # Import the GPIO library.
import time

from dynamixel_helper import DxlHelper

helper = DxlHelper("climber_preset.json")
motor_ids = [0, 1, 2, 3] # 0 and 1 are the right side, 2 and 3 are the left
motors = []
for i in range(len(motor_ids)):
    motors.append(helper.get_motor(motor_ids[i]))
    motors[i].set_torque(True)

for i in range(len(motor_ids)):
    motors[i].set_goal_position(0)

frontServoPin = 15
backServoPin = 16
servoHigh = 100*2.25/20/2
servoLow  = 100*0.75/20/2
servoMid  = 100*1.5/20/2

speed = 0
twist = 0

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
print(" starting up.")
GPIO.setup(frontServoPin, GPIO.OUT)  # Set GPIO pin 12 to output mode.
frontPWM = GPIO.PWM(frontServoPin, 50)   # Initialize PWM on pwmPin 50Hz frequency
GPIO.setup(backServoPin, GPIO.OUT)  # Set GPIO pin 12 to output mode.
backPWM = GPIO.PWM(backServoPin, 50)   # Initialize PWM on pwmPin 50Hz frequency
frontPWM.start(servoMid)
backPWM.start(servoMid)

def updatemotors():
    for i in range(len(motor_ids)):
        if i > 1:
            motors[i].set_goal_velocity(speed-twist)
        else:
            motors[i].set_goal_velocity(speed+twist)

def forward():
    print("Forward.")
    speed += 10
    updatemotors()

def backward():
    print("Backward.")
    speed -= 10
    updatemotors()

def left():
    print("Left.")
    twist -= 10
    updatemotors()

def right():
    print("Right.")
    twist -= 10
    updatemotors()

def stop():
    print("Stop.")
    twist = 0
    speed = 0
    updatemotors()

def openfront():
    print("Opening front legs.")
    frontPWM.ChangeDutyCycle(servoHigh)

def closefront():
    print("Closing front legs.")
    frontPWM.ChangeDutyCycle(servoLow)

def cleanup():
    frontPWM.stop()
    backPWM.stop()
    GPIO.cleanup()       # resets GPIO ports used back to input mode
    twist = 0
    speed = 0
    updatemotors()
