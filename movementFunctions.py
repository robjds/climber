
import RPi.GPIO as GPIO   # Import the GPIO library.
import time

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.

class robotController:
    frontServoPin = 15
    backServoPin = 16
    servoHigh = 100*2.25/20/2
    servoLow  = 100*0.75/20/2
    servoMid  = 100*1.5/20/2

    def __init__(self, name):
        self.name = name
        print(self.name + " starting up.")
        GPIO.setup(self.frontServoPin, GPIO.OUT)  # Set GPIO pin 12 to output mode.
        self.frontPWM = GPIO.PWM(self.frontServoPin, 50)   # Initialize PWM on pwmPin 50Hz frequency
        GPIO.setup(self.backServoPin, GPIO.OUT)  # Set GPIO pin 12 to output mode.
        self.backPWM = GPIO.PWM(self.backServoPin, 50)   # Initialize PWM on pwmPin 50Hz frequency
        self.frontPWM.start(self.servoMid)
        self.backPWM.start(self.servoMid)

    def forward(self):
        print(self.name + " forward.")

    def backward(self):
        print(self.name + " backward.")

    def left(self):
        print(self.name + " right.")

    def right(self):
        print(self.name + " right.")

    def stop(self):
        print(self.name + " stop.")

    def openfront(self):
        print(self.name + " opening frontlegs.")
        self.frontPWM.ChangeDutyCycle(self.servoHigh)

    def closefront(self):
        print(self.name + " closing frontlegs.")
        self.frontPWM.ChangeDutyCycle(self.servoLow)

    def cleanup(self):
        self.frontPWM.stop()
        self.backPWM.stop()
        GPIO.cleanup()                     # resets GPIO ports used back to input mode
