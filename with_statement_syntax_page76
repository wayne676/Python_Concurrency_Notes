# ch4/example1.py

n_files = 254
files = []

for i in range(n_files):
    with open('output1/sample%i.txt' % i, 'w') as f:
        files.append(f)

'''
the f variable indicates the current opened file within the with block at each iteration of the for loop, and as soon as our program 
exits what with block (which is outside the scope of that f variable), there is no longer any other way to access it.

with [expression] (as [target]):
    [code]

with [expression1] as [target1], [expression2] as [target2]:
    [code]

with [expression1] as [target1]:
    with [expression2] as [target2]:
        [code]

'''