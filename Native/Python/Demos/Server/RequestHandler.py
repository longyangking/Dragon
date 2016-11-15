#!/usr/bin/python

class RequestHandler(object):
	def __init__(self,request):
		self.request = request
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
