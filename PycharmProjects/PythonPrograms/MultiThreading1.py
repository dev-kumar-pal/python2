from threading import *

class MyThread(Thread):
    def run(self):
        for i in range(100):
            print('Child Thread')

t = MyThread()
t.start()

for i in range(100):
    print('Main Thread')