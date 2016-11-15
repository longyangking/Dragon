#!/usr/bin/python
import socket
import RequestHandlerThread

ADDRESS = (HOST,PORT) = '',8888
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDRESS)
server.listen(1)
print 'Server is on and listening to PORT %s ...' % PORT

while True:
	connection, clientaddress = server.accept()
	requesthandlerthread =RequestHandlerThread.RequestHandlerThread(connection,clientaddress)
	requesthandlerthread.start()
server.close()
