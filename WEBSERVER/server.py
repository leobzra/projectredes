import socket
import sys
from socket import socket, AF_INET, SOCK_STREAM
from _thread import *


host = ''


porta = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
socket.bind((host, port))
    
while True:
	print('aguarde')
	data, address = s.recvfrom(2048)
		
	print 'received: ' + data + '\nfrom: ' + address[0] + '\nlistening on porta: ' + str(address[1])
