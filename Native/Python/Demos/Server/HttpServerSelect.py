#!/usr/bin/python
import socket
import RequestHandlerSelect
import select

ADDRESS = (HOST,PORT) = '',8888
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADDRESS)
server.listen(1)

print 'Server is on and listening to PORT %s ...',PORT

inputs = [server]
outputs = []
exceptions = []

while True:
	rlist,wlist,elist = select.select(inputs,outputs,exceptions,1)
	for r in rlist:
		if r is server:
			connection, clientaddress = r.accept()
			request = connection.recv(1024)
			print request
			handler = RequestHandlerSelect.RequestHandlerSelect(request)
			connection.sendall(handler.response())
			connection.close()
server.close()
