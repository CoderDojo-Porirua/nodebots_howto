import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pins = {"L": dict(), "R": dict()}
#pins["L"]["en"] =  # Switch status (Analog) output
#pins["L"]["cs"] =  # Current sense (Analog) input
pins["L"]["ina"] = 13 # Clockwise input
pins["L"]["inb"] = 19 # Counter-clockwise input
pins["L"]["pwm"] = 26 # PWM input
pins["R"]["ina"] = 20 #Pin switched with b for consistency for the Right side, as a and b are wheel directions (clockwise and anticlockwise), not vehicle directions (forward and backward)
pins["R"]["inb"] = 16
pins["R"]["pwm"] = 21

pwm = dict()

for side in pins:
 for pin in pins[side]:
  GPIO.setup(pins[side][pin], GPIO.OUT)
 GPIO.output(pins[side]["ina"], 0)
 GPIO.output(pins[side]["inb"], 0)
 pwm[side] = GPIO.PWM(pins[side]["pwm"], 100)
 pwm[side].start(50)

def cleanup():
 for side in pwm:
  GPIO.output(pins[side]["ina"], 0)
  GPIO.output(pins[side]["inb"], 0)
  pwm[side].stop()
 GPIO.cleanup() 

def go(side, direction, speed):
 if direction == "F":
  GPIO.output(pins[side]["ina"], 1)
  GPIO.output(pins[side]["inb"], 0)
 else:
  GPIO.output(pins[side]["ina"], 0)
  GPIO.output(pins[side]["inb"], 1)
 pwm[side].ChangeDutyCycle(speed)

try:
 go("R", "F", 10)
 go("L", "F", 10)
 time.sleep(1)
 go("R", "B", 10)
 go("L", "B", 10)
 time.sleep(1)

except:
 cleanup()

cleanup()
