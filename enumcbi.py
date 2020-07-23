#!/usr/bin/env python 
#EnumCBI Enumeration script.
#Specify the port and enumeration commands in the configuration file enumcbi.conf
#https://github.com/anpmhn

import socket
import configparser
import os
import sys
from termcolor import colored, cprint
usage= "Usage: python3 enumcbi.py [ip address]"

if len(sys.argv) <= 1:
    print (usage)
    exit()

ipaddress = sys.argv[1]

config = configparser.ConfigParser(allow_no_value=True,strict=False, interpolation=None,delimiters=('='))
config.optionxform = str
config.read('enumcbi.conf')
for item in config.sections():
	#print (item)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(2)
	print("\n")
	if sock.connect_ex((ipaddress,int(item))) == 0:
		sock.close()
		openstatus =  ('Port '+item+' Open')
		cprint(openstatus,'green')
		print ("\n")
		for command in config[item]:
			command = command %ipaddress
			cmdtext = ("Running "+command)
			cprint(cmdtext,'yellow')
			print(os.system(command))
			print ("````````````````````````````````````````````````````````````````````````````````````")
			print ("\n")
			
	else:
		closedstatus =  ('Port '+item+' Closed')
		cprint(closedstatus, 'magenta')
		sock.close()


