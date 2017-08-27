#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 3000                # Reserve a port for your service.

s.connect(('192.168.1.42', port))
s.send('connect')
while True:
	print "Server: " + s.recv(1024)
	text = raw_input("Client: ")
	if text == "exit":
		s.send('exit')
		s.close                     # Close the socket when done
	else:
		s.send(text)