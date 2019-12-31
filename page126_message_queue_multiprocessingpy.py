# ch6/example7.py

from math import sqrt
import multiprocessing

class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        pname = self.name

        while not self.task_queue.empty():

            temp_task = self.task_queue.get()

            print('%s processing task: %s' % (pname, temp_task))

            answer = temp_task.process()
            self.task_queue.task_done()
            self.result_queue.put(answer)

class Task():
    def __init__(self, x):
        self.x = x

    def process(self):
        if self.x < 2:
            return '%i is not a prime number.' % self.x

        if self.x == 2:
            return '%i is a prime number.' % self.x

        if self.x % 2 == 0:
            return '%i is not a prime number.' % self.x

        limit = int(sqrt(self.x)) + 1
        for i in range(3, limit, 2):
            if self.x % i == 0:
                return '%i is not a prime number.' % self.x

        return '%i is a prime number.' % self.x

    def __str__(self):
        return 'Checking if %i is a prime or not.' % self.x

if __name__ == '__main__':

    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # enqueueing jobs
    my_input = [2, 36, 101, 193, 323, 513, 1327, 100000, 9999999, 433785907]
    for item in my_input:
        tasks.put(Task(item))

    # spawning consumers with respect to the
    # number cores available in the system
    n_consumers = multiprocessing.cpu_count()
    print('Spawning %i consumers...' % n_consumers)
    consumers = [Consumer(tasks, results) for i in range(n_consumers)]
    for consumer in consumers:
        consumer.start()
        
    tasks.join()

    for i in range(len(my_input)):
        temp_result = results.get()
        print('Result:', temp_result)

    print('Done.')

'''
For passing messages one can use Pipe() (for a connection between two processes) 
    or a Queue (which allows multiple producers and consumers).
Queue is essentially a Pipe with lock

If you use JoinableQueue then you must call JoinableQueue.task_done() for each task removed from the queue or 
    else the semaphore used to count the number of unfinished tasks may eventually overflow, raising an exception.

multiprocessing.Queue is different from queue.Queue
- Queue.Queue is just an in-memory queue that knows how to deal with multiple threads using it at the same time. 
    It only works if both the producer and the consumer are in the same process.
- Once you have them in separate system processes, which is what the multiprocessing library is about, things are a little more 
    complicated, because the processes no longer share the same memory

Create task queue and queue.
Based on number of CPUs, create X processes.
Start processes, process will get task from the task_queue
Fill the task_queue

Indicate that a formerly enqueued task is complete. For each get() used to 
    fetch a task, a subsequent call to task_done() tells the queue that the processing on the task is complete.
Blocks until all items in the queue have been gotten and processed.
'''