import _thread as thread
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
my_input = [2, 193, 323, 1327, 433785907]

for x in my_input:
    thread.start_new_thread(is_prime, (x,))

a = input('Type something to quit: \n')
print('Finished')

"""
If comment out the a=input(''), then program may terminate without printing out any input, in other words, the program
terminates before the threads can finish executing. 
$ python example2.py
Type something to quit: <--------------------
2 is a prime number.
193 is a prime number.
323 is not a prime number.
1327 is a prime number.
433785907 is a prime number.

$ python example2.py
323 is not a prime number.
2 is a prime number.
Type something to quit: <--------------------
193 is a prime number.
433785907 is a prime number.
1327 is a prime number.

so the last line of code is a workaround for the thread module finish all the threads before exit the program
"""