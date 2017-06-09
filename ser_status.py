import serial, time

ser = serial.Serial(
     port='/dev/ttyUSB0',
     baudrate=115200,
     parity=serial.PARITY_NONE,
     stopbits=serial.STOPBITS_ONE,
     bytesize=serial.EIGHTBITS)
ser.timeout = 3

data = "\x0D\x2A\x70\x6F\x77\x3D\x3F\x23\x0D"

ser.isOpen()
ser.flush()
ser.write(data)
time.sleep(3)
ser.readline()
while True:
 status = ser.readline()
 if "ON" in status:
  serial = "ON"
 elif "OFF" in status:
  serial = "OFF"
 else:
  serial = "Error communicating..."
 break

ser.close()
