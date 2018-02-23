#!/bin/python
import RPi.GPIO as GPIO
import time
LedPin = 6
StatusPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.setup(StatusPin, GPIO.OUT)
GPIO.output(StatusPin, GPIO.HIGH)
GPIO.output(LedPin, GPIO.LOW)

GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)


def blink():
        t_end = time.time() + 15
	GPIO.output(StatusPin, GPIO.LOW)
        while time.time() < t_end:
                        GPIO.output(LedPin, GPIO.LOW)
                        time.sleep(0.5)
                        GPIO.output(LedPin, GPIO.HIGH)
                        time.sleep(0.5)
	GPIO.output(LedPin, GPIO.LOW)

def destroy():
        GPIO.output(LedPin, GPIO.LOW)
        GPIO.cleanup()

while True: 
	inputValue = GPIO.input(18)
	if(inputValue == False):
		print("Bottone premuto")
		blink()



