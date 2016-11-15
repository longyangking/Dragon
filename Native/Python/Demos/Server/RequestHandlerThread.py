#!/usr/bin/python
import threading

class RequestHandlerThread(threading.Thread):
	def __init__(self,connection,clientaddress):
		threading.Thread.__init__(self)
		self.connection = connection
		self.clientaddress = clientaddress
	def GetRequest(self):
		return self.connection.recv(1024)
	def head(self):
		return 'HTTP/1.1 200 OK'
	def content(self):
		index = open('index.html','r')
		content = ''
		for line in index:
			content += line
		index.close()
		return content
	def response(self):
		return '{head}\n\n{content}'.format(
			head = self.head(),
			content = self.content())
	def run(self):
		self.request = self.GetRequest() #Nothing happen...
		self.connection.sendall(self.response())
		self.connection.close()
