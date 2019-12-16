import threading
from math import sqrt
def is_prime(x):
    if x < 2:
        print('%i is not a prime number.' % x)

    elif x == 2:
        print('%i is a prime number.' % x)

    elif x % 2 == 0:
        print('%i is not a prime number.' % x)

    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                print('%i is not a prime number.' % x)
                return

        print('%i is a prime number.' % x)

# step 1
class MyThread(threading.Thread):
    # step 2
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x
    # step 3
    def run(self):
        print('Starting processing %i ...' % x )
        is_prime(self.x)
"""
To create and customize a new thread using the threading mocule, there are specific steps that need to be followed:
1- Define a subclass of the threading.Thread class in your program
2- OVerride the default __init__ (self [,args])
3- OVerride the default run(self [,args]) method inside of the subclass

thread method:
start() starts a thread's activity
join() wait until thread terminates
"""

"""
join() wait until thread terminates
so if we do 
for x in my_input:
    temp_thread = MyThread(x)
    temp_thread.start()
    temp_thread.join()
then the program will run like a sequential program
"""

my_input = [2, 193, 323, 1327, 433785907]
threads = []
for x in my_input:
    temp_thread = MyThread(x)
    temp_thread.start()

    threads.append(temp_thread)

for thread in threads:
    thread.join()

print('Finished.')