import multiprocessing
import time

class Worker(multiprocessing.Process):
    def __init__(self):
        super().__init__()
        self.num = 1
        self.period = 0

    def run(self):
        while True:
            if self.num > 10:
                break

            print('Worker: {num}'.format(num=self.num))
            time.sleep(1)
            if self.num%3 == 0:
                self.period += 1
                print('Worker: Period {period} completed'.format(period=self.period))
            self.num += 1

if __name__=='__main__':
    worker = Worker()
    worker.start()
    print("Worker deployed")

    worker.join()
    print('All workers completed')