import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
p = GPIO.PWM(27, 50)

GPIO.output(2, 1)
GPIO.output(17, 1)

GPIO.output(3, 1)
GPIO.output(4, 0)

p.start(50)
time.sleep(2)
p.stop()

GPIO.cleanup()
