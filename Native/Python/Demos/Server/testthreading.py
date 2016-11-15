#!/usr/bin/python
import threading
import time

class TestThreading(threading.Thread):
	def __init__(self,text):
		threading.Thread.__init__(self)
		self.text = text
	def run(self):
		for i in range(3):
			time.sleep(1) #Wait for 1 second
			print '{name}: {number}'.format(
				name = self.text,
				number = str(i))

for i in range(3):
	test = TestThreading('Thread '+str(i))
	time.sleep(1)
	test.start()
	
