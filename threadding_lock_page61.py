import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print('Starting thread %s.' % self.name)
        thread_lock.acquire() # <-------------------------acquire the lock
        thread_count_down(self.name, self.delay)
        thread_lock.release() # <-------------------------release the lock
        print('Finished thread %s.' % self.name)

def thread_count_down(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)
        print('Thread %s counting down: %i...' % (name, counter))
        counter -= 1

thread_lock = threading.Lock() # <------------------ initialize a lock object

thread1 = MyThread('A', 0.5)
thread2 = MyThread('B', 0.5)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


print('Finished.')


"""
A primitive lock is in one of two states, “locked” or “unlocked”. 
It is created in the unlocked state. It has two basic methods, 
acquire(blocking=True, timeout=-1) # when blocking=False, current thread does not wait for the lock and sumply returns 0
if the lock cannot be acquired by the thread, when blcking=True, current thread blocks and waits for the lock be released 
and acquires it afterwards
and release()

For above example, because of the lock, it will run in sequentially 
"""