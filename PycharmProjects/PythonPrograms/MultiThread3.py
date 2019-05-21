import time
from threading import *

def printsquares():
    for i in range(10):
        time.sleep(1)
        print(i*i)


def printdouble():
    for i in range(10):
        time.sleep(1)
        print(2*i)
print('Toatl no of Threads',active_count())
begintime = time.time()
#printdouble()
t1 = Thread(target=printsquares)
t1.start()

#printsquares()
t2 = Thread(target=printdouble)
t2.start()
print('Toatl no of Threads',active_count())
e = enumerate()

for i in e:
    print('Id no',current_thread().ident)
    print('name',i.getName())

t1.join()
t2.join()

endtime = time.time()


print("total time",endtime-begintime)

print('Toatl no of Threads',active_count())



