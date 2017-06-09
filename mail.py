#!/usr/bin/env python
# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from data import *
from ser_status import *

sender = ''								# Fill in sender email address
recipients = ['']						# Fill in recipient email address
__pass__ = ""							# Fill in sender email password

def send(error_message):
    server = smtplib.SMTP('smtp.gmail.com' , 587)	# Change if needed
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(sender , __pass__)
    value = """%s
Ip: %s
Date/time: %s \n
CPU used: %d Mb
CPU temp: %d°C \n
Ram total: %d Mb
Ram used: %d Mb
Ram free: %d Mb
Percent used ram: %d%% \n
%s \n
Serial status:%r""" %(hostname, ip, date, cpuU, cpuT, ramT, ramU, ramF, ramPU, process, serial)
    msg = MIMEText(value)
    msg['Subject'] = error_message
    msg['From'] = sender
    msg['To'] = ",".join(recipients)	# Erase ",".join() if only one recipient
    server.sendmail(sender, recipients, msg.as_string())
    server.quit()
