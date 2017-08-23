import threading
from time import ctime,sleep

class subprocess(threading.Thread):
    def __init__(self,func):
        threading.Thread.__init__(self)
        self.num = 0
        self.func = func
    
    def run(self):
        print('subprocess start!')
        while True:
            sleep(1)
            print("Sub {num}".format(num=self.num))
            if self.num%4 == 0:
                self.func()

    def setnum(self,num):
        self.num = num

class mainprocess:
    def __init__(self):
        self.num = 1

    def init(self):
        self.subprocess = subprocess(self.response)
        self.subprocess.start()
    
    def test(self):
        while True:
            sleep(3)
            print("Main Emit")
            self.subprocess.setnum(self.num)
            self.num += 1

    def response(self):
        print('Waiting for response...')
        sleep(10)
        print('Responsed')
        self.num = 1
        self.subprocess.setnum(self.num)

if __name__=='__main__':
    mainp = mainprocess()
    mainp.init()
    mainp.test()