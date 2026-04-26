# 7. Naming Threads

import threading
from threading import Thread
from time import sleep

def worker(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)

# Start two normal threads and a daemon thread

t1 = Thread(name='worker', target=worker, args='A')
t2 = Thread(target=worker, args='B')  # use default name e.g. Thread-1
t3 = Thread(target=worker, args='B')  # use default name e.g. Thread-2
d = Thread(daemon = True, name='daemon', target=worker, args='C')

t1.start()
t2.start()
d.start()
t3.start()

for t in threading.enumerate():
    print(t.name)
