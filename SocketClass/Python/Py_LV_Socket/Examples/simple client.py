# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:24:30 2017

@author: gra1
"""

import socket
import packet
import sys

def handle_err(ex):
        print('Error: {0}: {1}.\n\nIn line {2} of {3}'.format(type(ex).__name__,
            str(ex),sys.exc_info()[-1].tb_lineno,__file__))
            

HOST = '127.0.0.1'
Listen_Port = 60100
userinput = ''

try:
    s = socket.create_connection((HOST, Listen_Port))
    s.settimeout(0.2)
except Exception as e:
    handle_err(e)


else: 
    try:
        while userinput != 'quit':
            userinput = raw_input("Input: ")        
            packet.SendPacket(s,userinput+'\n')
            data = packet.ReceivePacket(s)
            print data
    except Exception as e:
        handle_err(e)
  
    print 'Closing connection'
    try:
        s.close()
    except IOError as e:
       handle_err(e)
    