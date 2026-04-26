from threading import Thread


def simple_worker():
    print('hello')

# The thread will run the function simple_worker
t1 = Thread(target=simple_worker)
t1.start()
# t1.start()

print(t1.name)
print(t1.ident)
print(t1.is_alive())
t1.join()