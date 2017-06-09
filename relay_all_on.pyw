import serial
import sys

ser = serial.Serial(				#set up the serial connection
    port='COM3',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS
)

print(ser.isOpen())

status = "\x5B"						#sends status check command
ser.write(status)

s = ser.read(1) 					#reads status as byte
s = ord(s)							#convert byte to int representation
string = bin(s)[2:].rjust(8, '0')	#convert to 1s and 0s
#for bit in string:
#    print(bit)

if '0' in string:					# If byte is low, sends on command
    on = "\x64"
    ser.write(on)
else:
    sys.exit()