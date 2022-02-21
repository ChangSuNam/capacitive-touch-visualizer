# this code will read the touch values from the ESP32,
# then convet the value to simley faces! ¨̮


import serial

ser = serial.Serial('/dev/cu.usbserial-0238DBD7', 115200)

while(True):
 	stringVal = str(ser.readline().strip(), 'ascii')
	intVal = int(stringVal)
	for x in range (intVal):
       		print("[¨̮]", end = "")	
	print("\n")

