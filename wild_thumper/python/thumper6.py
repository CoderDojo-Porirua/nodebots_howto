import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pins = {"L": dict(), "R": dict()}
#pins["L"]["en"] = 2 # Switch status (Analog) output
#pins["L"]["cs"] = 3 # Current sense (Analog) input
pins["L"]["ina"] = 13 # Clockwise input
pins["L"]["inb"] = 19 # Counter-clockwise input
pins["L"]["pwm"] = 26 # PWM input
#pins["R"]["en"] = 14
#pins["R"]["cs"] = 15
pins["R"]["ina"] = 20 #Pin switched with b for consistency for the Right side, as a and b are wheel directions (clockwise and anticlockwise), not vehicle directions (forward and backward)
pins["R"]["inb"] = 16
pins["R"]["pwm"] = 21

pwm = dict()

for side in pins:
 for pin in pins[side]:
  GPIO.setup(pins[side][pin], GPIO.OUT)
# GPIO.output(pins[side]["en"], 1)
# GPIO.output(pins[side]["cs"], 1)
 pwm[side] = GPIO.PWM(pins[side]["pwm"], 50)
 pwm[side].start(0)

def cleanup():
 for side in pwm:
  pwm[side].stop()
 GPIO.cleanup()

def go(side, direction, speed):
 if direction == "B":
  GPIO.output(pins[side]["ina"], 1)
  GPIO.output(pins[side]["inb"], 0)
 else:
  GPIO.output(pins[side]["ina"], 0)
  GPIO.output(pins[side]["inb"], 1)
 pwm[side].ChangeDutyCycle(speed)

try:
 go("L", "F", 10)
 go("R", "F", 10)
 time.sleep(2)
 go("L", "F", 20)
 go("R", "F", 20)
 time.sleep(2)
 go("L", "F", 30)
 go("R", "F", 30)
 time.sleep(2)
 go("L", "F", 40)
 go("R", "F", 40)
 time.sleep(2)
 go("L", "F", 50)
 go("R", "F", 50)
 time.sleep(2)
 go("L", "F", 60)
 go("R", "F", 60)
 time.sleep(2)
 go("L", "F", 70)
 go("R", "F", 70)
 time.sleep(3)
 go("L", "F", 100)
 go("R", "F", 100)
 time.sleep(5)
 go("L", "F", 50)
 go("R", "F", 50)
 time.sleep(3)
 go("L", "F", 40)
 go("R", "F", 40)
 time.sleep(2)
 go("L", "F", 30)
 go("R", "F", 30)
 time.sleep(2)
 go("L", "F", 20)
 go("R", "F", 20)
 time.sleep(2)
 go("L", "F", 10)
 go("R", "F", 10)
 time.sleep(2)

except:
 cleanup()

cleanup()
