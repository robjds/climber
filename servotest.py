import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                          # Can use GPIO.setmode(GPIO.BCM) instead to use
                          # Broadcom SOC channel names.
servoPin = 15
GPIO.setup(servoPin, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(servoPin, 50)   # Initialize PWM on pwmPin 100Hz frequency

# main loop of program
print("\nPress Ctl C to quit \n")  # Print blank line before and after message.
dc=0                               # set dc variable to 0 for 0%
pwm.start(dc)                      # Start PWM with 0% duty cycle

sleepTime = 0.05

pinHigh = 100*2.25/20/2
pinLow  = 100*0.75/20/2
pinMid  = (pinHigh+pinLow)/2

dc=pinMid                               # set dc variable to 0 for 0%
pwm.start(dc)                      # Start PWM with 0% duty cycle

try:
  while True:                      # Loop until Ctl C is pressed to stop.
    while dc < pinHigh:
        pwm.ChangeDutyCycle(dc)
        dc += 0.375
        print(dc)
        time.sleep(sleepTime)             # wait .05 seconds at current LED brightness
    while dc > pinLow:
        pwm.ChangeDutyCycle(dc)
        dc -= 0.375
        print(dc)
        time.sleep(sleepTime)             # wait .05 seconds at current LED brightness
except KeyboardInterrupt:
  print("Ctl C pressed - ending program")


pwm.ChangeDutyCycle(pinMid)
time.sleep(1)
pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode
