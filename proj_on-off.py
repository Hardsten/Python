from datetime import datetime
import serial

ser1 = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser2 = serial.Serial(
    port='/dev/ttyUSB1',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

wake_string = "\x0D\x2A\x70\x6F\x77\x3D\x6F\x6E\x23\x0D"
sleep_string = "\x0D\x2a\x70\x6f\x77\x3d\x6f\x66\x66\x23\x0D"

def wake_up():
    data = wake_string

    ser1.write(data)
    s = ser1.read(1)
    print(s)
    ser1.close()

    ser2.write(data)
    s = ser2.read(1)
    print(s)
    ser2.close()

def go_sleep():
    data = sleep_string

    ser1.write(data)
    s = ser1.read(1)
    print(s)
    ser1.close()	

    ser2.write(data)
    s = ser2.read(1)
    print(s)
    ser2.close()

now = datetime.now()
hour = int(now.hour)
min = int(now.minute)

if hour >= 18:
    print ("Turning off projector")
    go_sleep()

elif hour == 9:
    if min >= 50:
        print ("Turning on projector")
        wake_up()