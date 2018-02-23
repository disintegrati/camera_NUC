#!/usr/bin/env python

import serial
import time
import os
arduino = serial.Serial("/dev/ttyACM0", 9600)
while True:
#          print arduino.readline()
	  x = arduino.readline()
	  if "1" in x:
		print "ricevo"
#		arduino.write(b"a")
		os.system("sh /home/nuc/Scrivania/camera/video2.sh")
		arduino.write(b"2")
		print "finito"
time.sleep(1)
