import serial
import time
import os
#arduino = serial.Serial("/dev/ttyACM0", 9600)
while True:

	def get_serial_port():
    		return "/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()

	arduino = serial.Serial(get_serial_port(), 9600)
	x = arduino.readline()
	if "1" in x:
		print "ricevo"
		os.system("sh /home/nuc/Scrivania/camera/video2.sh")
		arduino.write(b"2")
		print "finito"
time.sleep(1)
