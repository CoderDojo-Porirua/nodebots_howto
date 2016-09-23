import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pins = {"L": dict(), "R": dict()}
pins["L"]["en"] = 2 # Switch status (Analog) output
pins["L"]["cs"] = 3 # Current sense (Analog) input
pins["L"]["ina"] = 4 # Clockwise input
pins["L"]["inb"] = 17 # Counter-clockwise input
pins["L"]["pwm"] = 27 # PWM input
pins["R"]["en"] = 14
pins["R"]["cs"] = 15
pins["R"]["ina"] = 23
pins["R"]["inb"] = 18
pins["R"]["pwm"] = 24

pwm = dict()

for side in pins:
 for pin in pins[side]:
  GPIO.setup(pins[side][pin], GPIO.OUT)
 GPIO.output(pins[side]["en"], 1)
 GPIO.output(pins[side]["cs"], 1)
 pwm[side] = GPIO.PWM(pins[side]["pwm"], 50)
 pwm[side].start(0)

def cleanup():
 for side in pwm:
  pwm[side].stop()
 GPIO.cleanup() 

def go(side, direction, speed):
 if direction == "F":
  GPIO.output(pins[side]["ina"], 1)
  GPIO.output(pins[side]["inb"], 0)
 elif direction == "B":
  GPIO.output(pins[side]["ina"], 0)
  GPIO.output(pins[side]["inb"], 1)
 else:
  GPIO.output(pins[side]["ina"], 0)
  GPIO.output(pins[side]["inb"], 0)  
 pwm[side].ChangeDutyCycle(speed)

try:
 go("L", "S", 0)
 go("L", "S", 0)
 go("L", "F", 50)
 time.sleep(1)
 go("R", "F", 50)
 time.sleep(1)
 go("L", "B", 50)
 time.sleep(1)
 go("R", "B", 50)
 time.sleep(1)

except:
 cleanup()

cleanup()
