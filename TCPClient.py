#!/usr/bin/python3

from email import message
import socket

def main():
    #Making Client side socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Can get this host one of two ways
    host = socket.gethostname()
    #OR you can hardcode the host with "host = IPAddress"

    #Port needs to match server side
    port = 456

    #Can do two ways
    clientSocket.connect(('192.168.100.4', port))
    #clientSocket.connect((host, port))

    #This will specify the amount of data we can recieve
    message = clientSocket.recv(1024)

    clientSocket.close()

    print(message.decode('ascii'))

main()

