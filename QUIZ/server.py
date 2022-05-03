from threading import Thread
from time import sleep
from socket import socket, AF_INET, SOCK_DGRAM
import random

socket_servidor = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
socket_servidor.bind((localhost, port))

def main():

    class server:
        def __init__(self, ip, porta):
            self.ip = ip
            self.porta = porta
		

def msg(msg,root):
	codmsg= msg.encode()
	UDPServerSocket.sendto(codmsg,root)
  
def questionscheck():
	pastaperguntas = open('perguntas.txt', 'r')
	data= pastaperguntas.read().split(":")
  pastaperguntas.close()
	
def recebermsg():
	UDPServerSocket = socket(AF_INET, SOCK_DGRAM)
	UDPServerSocket.bind('localhost','8080')
	

while True:
    dados = socket_servidor.recvfrom(1024)
placar=[]
placargeral=[]

def questionscheck(questions)

for p in(5):
	findperg= random.choice(pastaperguntas)

if resposta == questions_temp.split(":"):
	print(' resposta exata ')
	placar+=25
if resposta == None:
  print('não respondeu fio')
  placar-=1
else:
	print(' resposta errada' )
	placar-= 5


append.placargeral(placar)
print(placargeral.sort())

	
