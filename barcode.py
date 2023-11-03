import sys
import serial
import time

#default usb device /dev/ttyACM0 9600 8n1
ser = serial.Serial("/dev/ttyACM0",115200,timeout=0.5)

print('serial test start ...')
if ser != None:
    print('serial ready...')
else:
    print('serial not ready')
    sys.exit()



ser.timerout=1 #read time out
ser.writeTimeout = 0.5 #write time out.

while True:
      line = ser.readline().decode()
      if len(line) > 0:
         print(line)
      time.sleep(0.1)
