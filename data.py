#!/usr/bin/env python
# coding=utf-8
import psutil
import os
import socket
import time
import datetime
from subprocess import PIPE, Popen

        #Checks the CPU temperature
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return float(res.replace("temp=","").replace("'C\n",""))
cpuT = getCPUtemperature()

        #Checks if specified process 'omxplayer.bin' is running.
PROCNAME = 'omxplayer.bin'
for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
     process = "omxplayer.bin is running"
    elif psutil.NoSuchProcess:
     pass
    else:
     process = "omxplayer.bin isn't running"

        #Current date/time
date = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        #CPU info
cpuU = psutil.cpu_percent(interval=1)   #CPU used in %
cpuT = (getCPUtemperature())                    #CPU temp
        #Info of the system memory usage.
ram = psutil.virtual_memory()
ramT = (ram.total / 2**20)                      #Ram total
ramU = (ram.used / 2**20)                       #Ram used
ramF = (ram.free / 2**20)                       #Ram free
ramPU = ram.percent                             #Ram used in %
        #Check hostname and ip
hostname = socket.gethostname()
ip = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1').readline()
