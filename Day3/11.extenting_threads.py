
from threading import Thread
from time import sleep


# Example extending the Thread class

def target_method():
        print("0000")

class WorkerThread(Thread):
    def __init__(self, daemon=None, target=None, name=None):
        super().__init__(daemon=daemon, target=target, name=name)


    def run(self):
        
        print("Run started")
        for i in range(0, 10):
            print('.', end='', flush=True)
            sleep(1)
        print("Run Ended")
        super().run()
        # self._target()

        


print('Starting')
t = WorkerThread(target=target_method)
t.start()