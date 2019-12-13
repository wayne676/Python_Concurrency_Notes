

# ch3/example5.py

import queue
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print('Starting thread %s.' % self.name)
        process_queue()
        print('Exiting thread %s.' % self.name)

def process_queue():
    while True:
        try:
            x = my_queue.get(block=False)
        except queue.Empty:
            return
        else:
            print_factors(x)

        time.sleep(1)

def print_factors(x):
    result_string = 'Positive factors of %i are: ' % x
    for i in range(1, x + 1):
        if x % i == 0:
            result_string += str(i) + ' '
    result_string += '\n' + '_' * 20

    print(result_string)


# setting up variables
input_ = [1, 10, 4, 3]

# filling the queue
my_queue = queue.Queue()
for x in input_:
    my_queue.put(x)


# initializing and starting 3 threads
thread1 = MyThread('A')
thread2 = MyThread('B')
thread3 = MyThread('C')

thread1.start()
thread2.start()
thread3.start()

# joining all 3 threads
thread1.join()
thread2.join()
thread3.join()

print('Done.')

"""
If we have large number of tasks to be processed, we do not want to spawn the same large number of threads and have each 
thread execute only one task.
So we have thread pool and queue work together.

get() returns the next element of the calling queue and remove it from the queue object. 
If 'block' is false, return an item if one is immediately
        available, else raise the Empty exception 

A queue, filled with [1, 10, 4, 3]
3 threads takes task from queue and execute it.
How?
class MyThread(threading.Thread):
    def run(self):
        print('Starting thread %s.' % self.name)
        process_queue()  <----------------------------- thread takes taks and execute it
        print('Exiting thread %s.' % self.name)

PriorityQueue
pq = PriorityQueue()
pq.put((5 , 'Python'))
pq.put((4 , 'C'))
pq.put((3 , 'Js'))

print(pq.queue)
while not pq.empty():
    print(pq.get()[1])

Js
C
Python

"""