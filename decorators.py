# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 15:15:29 2019

@author: pythor
"""

'''
Python Decorators?

A decorator takes in a function, 
adds some functionality and returns it. 
In this section, you will learn how you can create a 
decorator and why you should use it.
'''

'''
What are decorators in Python?
Python has an interesting feature called decorators 
to add functionality to an existing code.

This is also called metaprogramming as a part of 
the program tries to modify another part of the 
program at compile time.

Prerequisites for learning decorators
In order to understand about decorators, 
we must first know a few basic things in Python.

We must be comfortable with the fact that, 
everything in Python (Yes! Even classes), are objects. 
Names that we define are simply identifiers bound 
to these objects. 
Functions are no exceptions, they are objects too 
(with attributes). 
Various different names can be bound to the same 
function object.

Here is an example.
'''

#def first(a):
#    print(a)    
#
#first("Hello")
#
#second = first
#second('Hello')

'''
When you run the code, both functions first and 
second gives same output. 
Here, the names first and second refer to the 
same function object.

Now things start getting weirder.

Functions can be passed as arguments to 
another function.

If you have used functions like map, 
filter and reduce in Python, then you already 
know about this.
'''


#x=lambda a,b:a*b
#print(x(7,5))

#a=lambda x,y:x+y
#d=a(5,5)
#
#b=lambda m,n:m*n
#c=b(5,5)
#
#e=lambda d,c:d*c
#print(e(d,c))

#def multiply(i):
#    return (i*i)
#def add(i):
#    return (i+i)
#
#funcs = [multiply, add]
#for i in range(5):
#    value = list(map(lambda x: x(i), funcs))
#    print(value)


#value=list(map(lambda multiply:multiply(i),[multiply,add])

#number_list = range(-5, 5)
#less_than_zero = list(filter(lambda x: x < 0, number_list))
#print(less_than_zero)




#product = 1
#list = [1, 2, 3, 4]
#for num in list:
#    product = product * num  #product*=num
#print(product)


#from functools import reduce
#product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
#print(product)
#

#def update(n):
#    return n+2
#nums=[3,2,5,6,7,9,8,1,0]
#evens=list(filter(lambda n:n%2==0,nums))
#doubles=list(map(update,evens))
#print(evens)
#print(doubles)

#or

#nums=[3,2,5,6,7,9,8,1,0]
#evens=list(filter(lambda n:n%2==0,nums))
#doubles=list(map(lambda n:n*2,evens))
#print(evens)
#print(doubles)



'''
Such function that take other functions as 
arguments are also called higher order functions. 
Here is an example of such a function.
'''

#def inc(x):
#    return x + 1
#
#def dec(x):
#    return x - 1
#
#def operate(func, x):
#    result = func(x)
#    return result
#print(operate(inc,3))
#print(operate(dec,3))


'''
Furthermore, a function can return another function.
'''

#def is_called():
#    def is_returned():
#        print("Hello")
##    is_returned()
#    return is_returned
#
#new = is_called()
#
####Outputs "Hello"
#new()


'''
Here, is_returned() is a nested function 
which is defined and returned, each time 
we call is_called().
'''



'''
Getting back to Decorators
Functions and methods are called callable as 
they can be called.

In fact, any object which implements the special 
method __call__() is termed callable. 
So, in the most basic sense, a decorator is a 
callable that returns a callable.

Basically, a decorator takes in a function, adds 
some functionality and returns it.
'''

#def make_pretty(func):
#    def inner():
#        print("I got decorated")
#        func()
#    return inner
#
#def ordinary():
#    print("I am ordinary")
#
##ordinary()
###
####### let's decorate this ordinary function
#pretty = make_pretty(ordinary)
#pretty()

'''
In the example shown above, make_pretty() is a decorator. 

pretty = make_pretty(ordinary)
'''




'''
Now let's make a decorator to check for this case 
that will cause the error.
'''

#def smart_divide(func):
#   def inner(a,b):
#      print("I am going to divide",a,"and",b)
#      if b == 0:
#         print("Whoops! cannot divide")
#         return
#
#      return func(a,b)
#   return inner
#
#@smart_divide
#def divide(a,b):
#    return a/b
#
#print(divide(2,5))
#print(divide(2,0))
