import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
p = GPIO.PWM(27, 50)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
p = GPIO.PWM(27, 50)
p2 = GPIO.PWM(24, 50)

GPIO.output(2, 1)
GPIO.output(17, 1)

GPIO.output(3, 1)
GPIO.output(4, 0)

GPIO.output(14, 1)
GPIO.output(23, 1)

GPIO.output(15, 1)
GPIO.output(18, 0)


p.start(50)
time.sleep(2)
p.stop()

p2.start(50)
time.sleep(2)
p2.stop()

GPIO.cleanup()
