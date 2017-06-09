#!/usr/bin/env python
# coding=utf-8
from data import *
from ser_status import *

print "Date:", date
print hostname
print "Ip:", ip
        #Print system-wide float percentage of all CPU used.
print "CPU used: %d %%" % cpuU
        #Print the CPU temp
print "CPU temp: %d°C" % cpuT
        #Print statistics of the system memory usage.
print "Ram total: %dMb" % ramT
print "Ram used: %dMb" % ramU
print "Ram free: %dMb" % ramF
print "Percent used ram: %d%%" % ramPU
        #Print if specified process 'omxplayer.bin' is running.
print process

print "Serial status:%s" % serial

        #Writes the data to logg.txt (overwrites each time)
with open("logg.txt", "w") as text_file:
    text_file.write("""Date: %s \n%s\nIp: %s
 CPU usage: %d \n CPU temp: %d \n Total ram: %d \n Ram used: %d
 Ram free: %d \n Ram free percent: %d \n %s
 Serial status: %s""" % (date, hostname, ip, cpuU, cpuT, ramT, ramU, ramF, ramPU, process, serial))


        #Mail alerts!
import mail

if (cpuT >62):
 mail.send("CPU temp is above 62°C!")
else:
 pass
	
if (ramPU >90):
 mail.send("RAM usage is over 90%!")
else:
 pass
	
if (process == "omxplayer.bin isn't running"):
 mail.send("omxplayer.bin isn't running!")
else:
 pass
	
if (serial == "ON"):
 pass
else:
 mail.send("Serial failure!")
