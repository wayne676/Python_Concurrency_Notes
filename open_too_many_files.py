n_files = 254
files = []

# method 1
for i in range(n_files):
    files.append(open('output1/sample%i.txt' % i, 'w'))

"""
OSError: [Errno 24] Too many open files: 'output1/sample10239.txt'
This situation arose from what is known as file descriptor leakage. When Python opens a file inside a program, that opened
file is essentially represented by an integer. This integer acts as a reference point that program can use in order to have 
access to that 
ulimit -n will give the number of files that your system can handle. 
"""