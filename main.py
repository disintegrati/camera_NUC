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
Control = 0

def inCaricamento():
	global Control 
	if(Control == 1):
		print("Sto caricando")
        	t_end = time.time() + 20
        	while time.time() < t_end:
                        GPIO.output(LedPin, GPIO.LOW)
                        time.sleep(0.3)
                        GPIO.output(LedPin, GPIO.HIGH)
                        time.sleep(0.3)
			GPIO.output(LedPin, GPIO.LOW)
			GPIO.output(StatusPin, GPIO.LOW)
		print("Pronto a registrare")
		GPIO.output(StatusPin, GPIO.HIGH)
	

def inRegistrazione():
        t_end = time.time() + 19
	GPIO.output(StatusPin, GPIO.LOW)
        while time.time() < t_end:
		global Control
		if (Control == 1): 
                        GPIO.output(LedPinPulsazione, GPIO.LOW)
                        time.sleep(0.5)
                        GPIO.output(LedPinPulsazione, GPIO.HIGH)
                        time.sleep(0.5)
	GPIO.output(LedPinPulsazione, GPIO.LOW)
	print("registrazione finita")
	 

def destroy():
        GPIO.output(LedPin, GPIO.LOW)
        GPIO.cleanup()


def partiRegistrazione():
	global Control
        if(Control == 0):
	        while True:
			GPIO.setmode(GPIO.BCM)
      	        	inputValue = GPIO.input(18)
			if(inputValue == False):
				subprocess.call("sudo python /home/pi/Desktop/camera/usbreset1/reset.py 046d:081d", shell=True)
                       	 	print("Bottone premuto Inizio a registrare")
                       	 	os.system("sh /home/pi/Desktop/camera/video.sh")
                       	 	subprocess.call("sudo python /home/pi/Desktop/camera/usbreset1/reset.py 046d:081d", shell=True)
				Control = 1
				inCaricamento()	
                	time.sleep(1)
                
def partiCaricamento():	
	global Control
	if (Control == 0):
		while True:
			inputValue = GPIO.input(18)
                	if(inputValue == False):
				Control = 1
				inRegistrazione() #errore?
				
if __name__ == '__main__':
       # Control = 0    
	try:
		Thread(target = partiCaricamento).start()
		Thread(target = partiRegistrazione).start()
	except KeyboardInterrupt:
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
        
