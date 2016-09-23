import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pins = {"L": dict(), "R": dict()}
pins["L"]["en"] = 2
pins["L"]["cs"] = 3
pins["L"]["ina"] = 4
pins["L"]["inb"] = 17
pins["L"]["pwm"] = 27
pins["R"]["en"] = 14
pins["R"]["cs"] = 15
pins["R"]["ina"] = 23 # Swapped for the opposite side
pins["R"]["inb"] = 18
pins["R"]["pwm"] = 24

pwm = dict()

for side in pins:
 for pin in pins[side]:
  GPIO.setup(pins[side][pin], GPIO.OUT)
 GPIO.output(pins[side]["en"], 1)
 GPIO.output(pins[side]["cs"], 1)
 pwm[side] = GPIO.PWM(pins[side]["pwm"], 100)
 pwm[side].start(0)

def cleanup():
 for side in pwm:
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
 go("L", "B", 50)
 go("R", "B", 50)
 time.sleep(2)

except:
 cleanup()

cleanup()
