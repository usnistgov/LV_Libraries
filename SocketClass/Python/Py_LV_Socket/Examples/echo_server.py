# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 08:15:22 2017

@author: GRA1
"""
import socket
import packet
import sys

def handle_err(ex):
        print('Error: {0}: {1}.\n\nIn line {2} of {3}'.format(type(ex).__name__,
            str(ex),sys.exc_info()[-1].tb_lineno,__file__))
            
HOST = '127.0.0.1'
PORT = 60100
data = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.settimeout(0.2)

try:
    s.bind((HOST, PORT))
    s.listen(1)
except Exception as e:
    handle_err(e)

else:
    print 'Waiting for connection'
    conn, addr = s.accept()
    print 'Connected by', addr

    try:
        while data != 'quit\n':
            data = packet.ReceivePacket(conn)
            print data
            packet.SendPacket(conn,data)
                
    except Exception as e:
        handle_err(e)


    print 'closing connection to', str(addr) 
    conn.close()
        
