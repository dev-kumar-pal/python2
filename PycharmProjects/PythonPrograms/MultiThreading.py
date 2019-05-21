from threading import *

#print("Current executing thread ",threading.current_thread().getName())

def displaynumbers():
    print("Current executing thread ",current_thread().getName())

t = Thread(target=displaynumbers)
#t.setName('Numbers')
t.start()
#Thread(target=displayNumbers).start()
for i in range(10):
    #print(current_thread().getName())
    print('Main Thread')
#print("Current executing thread ",current_thread().getName())
