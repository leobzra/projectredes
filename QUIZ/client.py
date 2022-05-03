import threading
from socket import socket, AF_INET, SOCK_DGRAM

class client:
def __init__(self,server):
	self.client_socket = None
	self.server= server
	self.client_socket = socket(AF_INET,SOCK_DGRAM)

def main():
	client = client(server)
	server= ('localhost','8080')

	nome= input('escolha um nome:boom, moon, soon, doom, zoom')
	nome= nome.encode()
