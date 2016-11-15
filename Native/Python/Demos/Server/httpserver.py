#!/usr/bin/python
import socket
import os
import RequestHandler

ADDRESS = (HOST,PORT) = "",8888
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDRESS)
server.listen(1)

print 'Server is on and listening to port %s ...' % PORT

# Consider the thread and select
# Consider to exploit the standard modules

while True:
	connection, ClientAddress = server.accept()
	request = connection.recv(1024)
	print 'The client needs: %s' % request
	requesthandler = RequestHandler.RequestHandler(request)
	response = requesthandler.response()
	connection.sendall(response)
	connection.close()
