import RPi.GPIO as GPIO
import time

LedPin = 7

def setup():
	GPIO.setmode(GPIO.BOARD) 
	GPIO.setup(LedPin, GPIO.OUT)
	GPIO.output(LedPin, GPIO.HIGH)

def blink():
	t_end = time.time() + 15
	while time.time() < t_end:
			GPIO.output(LedPin, GPIO.LOW)
			time.sleep(1)
			GPIO.output(LedPin, GPIO.HIGH)
			time.sleep(1)

def destroy():
	GPIO.output (LedPin, GPIO.LOW)
	GPIO.cleanup()
 
if __name__ == '__main__':
	setup()
	try:
		blink()
	except KeyboardInterrupt:
		destroy()


