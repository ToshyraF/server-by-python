#!/usr/bin/python           # This is server.py file

import socket           

s = socket.socket()         # Create a socket object
host = '' # Get local machine name
port = 3000            # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

while True:
   s.listen(5) 
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   while True:
	   chat = c.recv(1024).decode('utf8')
	   print "Client: "+chat
	   if chat == "exit":
	   	 	print c.recv(1024)
	   	 	c.send('bye')
	   		s.close() 
	   else:
	   		text = raw_input("Server: ").decode('cp1252').encode('utf-8')
	   		
	   		c.send(text)