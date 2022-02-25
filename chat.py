import socket
import threading

HOST =  '192.168.1.6'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()
clients = []
nicknames = []

# multiple clients connect to server and talking to server
# networking is connected to socket




