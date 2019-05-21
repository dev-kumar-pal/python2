from threading import *

class MyThread():
    def display(self):
        for i in range(1000):
            print('Child Thread')

Thread(target=MyThread().display()).start()

for i in range(1000):
    print('Main Thread')