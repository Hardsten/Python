import serial

ser = serial.Serial(				#set up the serial connection
    port='COM4',					
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

print(ser.isOpen())
thestring = "\x7E\x30\x30\x30\x30\x20\x31\x0D"	#sends status check command
data = thestring

ser.write(data)
s = ser.read(1)
print(s)
ser.close()