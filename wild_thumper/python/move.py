import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pins = {"a": dict(), "b": dict()}
pins["a"]["en"] = 2
pins["a"]["cs"] = 3
pins["a"]["ina"] = 4
pins["a"]["inb"] = 17
pins["a"]["pwm"] = 27
pins["b"]["en"] = 14
pins["b"]["cs"] = 15
pins["b"]["ina"] = 18
pins["b"]["inb"] = 23
pins["b"]["pwm"] = 24

for side in pins:
 for pin in pins[side]:
  GPIO.setup(pins[side][pin], GPIO.OUT)

a = GPIO.PWM(pins["a"]["pwm"], 50)
b = GPIO.PWM(pins["b"]["pwm"], 50)

GPIO.output(pins["a"]["en"], 1)
GPIO.output(pins["b"]["en"], 1)
GPIO.output(pins["a"]["cs"], 1)
GPIO.output(pins["b"]["cs"], 1)

def go(aforward, aspeed, bforward, bspeed, delay):
 if aforward:
  GPIO.output(pins["a"]["ina"], 1)
  GPIO.output(pins["a"]["inb"], 0)
 else:
  GPIO.output(pins["a"]["ina"], 0)
  GPIO.output(pins["a"]["inb"], 1)
 if bforward:
  GPIO.output(pins["b"]["ina"], 1)
  GPIO.output(pins["b"]["inb"], 0)
 else:
  GPIO.output(pins["b"]["ina"], 0)
  GPIO.output(pins["b"]["inb"], 1)
 a.start(aspeed)
 b.start(bspeed)
 time.sleep(delay)
 a.stop()
 b.stop()

go(1, 50, 1, 30, 1)
GPIO.cleanup() 
