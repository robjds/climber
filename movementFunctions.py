
import RPi.GPIO as GPIO   # Import the GPIO library.
import time

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                          # Can use GPIO.setmode(GPIO.BCM) instead to use
                          # Broadcom SOC channel names.

frontServoPin = 4
backServoPin = 5

GPIO.setup(frontServoPin, GPIO.OUT)  # Set GPIO pin 12 to output mode.
frontpwm = GPIO.PWM(frontServoPin, 50)   # Initialize PWM on pwmPin 50Hz frequency
GPIO.setup(backServoPin, GPIO.OUT)  # Set GPIO pin 12 to output mode.
frontpwm = GPIO.PWM(backServoPin, 50)   # Initialize PWM on pwmPin 50Hz frequency

class robotController:
  def __init__(self, name):
    self.name = name

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

  def closefront(self):
    print(self.name + " closing frontlegs.")
