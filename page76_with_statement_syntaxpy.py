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
紧跟with后面的语句被求值后，返回对象的“–enter–()”方法被调用，这个方法的返回值将被赋值给as后面的变量
当with后面的代码块全部被执行完之后，将调用前面返回对象的“–exit–()”方法

（１）enter()方法被执行； 
（２）enter()方法的返回值，在这个例子中是”Foo”，赋值给变量sample； 
（３）执行代码块，打印sample变量的值为”Foo”； 
（４）exit()方法被调用；

exit()方法中有３个参数， exc_type, exc_val, exc_tb，这些参数在异常处理中相当有用。 
exc_type：　错误的类型 
exc_val：　错误类型对应的值 
exc_tb：　代码中错误发生的位置 
def __exit__(self, exc_type, exc_val, exc_tb):
        print "type: ", exc_type
        print "val: ", exc_val
        print "tb: ", exc_tb
'''