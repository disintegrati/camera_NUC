#!/bin/python
import subprocess
import RPi.GPIO as GPIO
import time
import os
import threading
from threading import Thread
LedPin = 4
LedPinPulsazione = 6
StatusPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.setup(LedPinPulsazione, GPIO.OUT)
GPIO.output(LedPinPulsazione, GPIO.LOW)
GPIO.output(LedPin, GPIO.LOW)
GPIO.setup(StatusPin, GPIO.OUT)
GPIO.output(StatusPin, GPIO.HIGH)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)


def inCaricamento():
        t_end = time.time() + 15
        while time.time() < t_end:
                        GPIO.output(LedPin, GPIO.LOW)
                        time.sleep(0.3)
                        GPIO.output(LedPin, GPIO.HIGH)
                        time.sleep(0.3)
			GPIO.output(LedPin, GPIO.LOW)
	GPIO.output(StatusPin, GPIO.HIGH)
	

def inRegistrazione():
        t_end = time.time() + 15
	GPIO.output(StatusPin, GPIO.LOW)
        while time.time() < t_end:
                        GPIO.output(LedPinPulsazione, GPIO.LOW)
                        time.sleep(0.5)
                        GPIO.output(LedPinPulsazione, GPIO.HIGH)
                        time.sleep(0.5)
	GPIO.output(LedPinPulsazione, GPIO.LOW)
	

def destroy():
        GPIO.output(LedPin, GPIO.LOW)
        GPIO.cleanup()


def partiRegistrazione():
        while True:
                GPIO.setmode(GPIO.BCM)
                inputValue = GPIO.input(18)
                if(inputValue == False):
			subprocess.call("sudo python /home/pi/Desktop/camera/usbreset1/reset.py 046d:081d", shell=True)
                        print("Bottone premuto Inizio a registrare")
                        os.system("sh /home/pi/Desktop/camera/video.sh")
                        inRegistrazione()
                        subprocess.call("sudo python /home/pi/Desktop/camera/usbreset1/reset.py 046d:081d", shell=True)
				
                time.sleep(0.3)
                
def partiCaricamento():
        while True:
                inputValue = GPIO.input(18)
                if(inputValue == False):
                        print("video finito")
			print(Controller)
			inCaricamento()

if __name__ == '__main__':
        try:
		Thread(target = partiCaricamento).start()
                Thread(target = partiRegistrazione).start()
	except KeyboardInterrupt:
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
        
