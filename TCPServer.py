#!/usr/bin/python3

from http import client
import socket

def main():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #AF_INET is IPv4
    #SOCK_STREAM is TCP

    #Can do this two ways
    host = socket.gethostbyname()
    #host = 192.168.100.4

    #Specify the listener
    port = 456

    #Can do this two ways
    serverSocket.bind(host, port)
    #serverSocket.bind('192.168.100.4', port)

    #Now we are listening on 456 for a TCP connection
    serverSocket.listen(3)
    #Will allow three connections

    #Connection time
    while True:
        clientSocket, address = serverSocket.accept()

        #Show the connection and where
        print("We have a connection from %s " % str(address))

        message = 'Thank you for the connection/' + "\r\n"

        clientSocket.send(message.encode('ascii'))
        clientSocket.close()

    main()