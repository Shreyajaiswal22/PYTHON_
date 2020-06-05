# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:11:24 2019

@author: pythor
"""
'''
What is recursion in Python?
Recursion is the process of defining something in 
terms of itself.

A physical world example would be to place two parallel 
mirrors facing each other.
Any object in between them would be reflected recursively.
'''

# An example of a recursive function to
# find the factorial of a number

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))


'''
Advantages of Recursion:
    
Recursive functions make the code look clean 
and elegant.

A complex task can be broken down into simpler 
sub-problems using recursion.

Sequence generation is easier with recursion than 
using some nested iteration.

Disadvantages of Recursion:

Sometimes the logic behind recursion is hard 
to follow through.

Recursive calls are expensive (inefficient) 
as they take up a lot of memory and time.

Recursive functions are hard to debug.
'''



#import file_handling as fh
#print(fh.add(5,12))
#fh.fib()
#print(fh.div(4,4))




#from file_handling import add,multy,div
#print(add(5,5))
#print(multy(5,5))
#print(div(4,4))



#from file_handling import *
#print(add(5,5))
#print(multy(5,5))
#print(div(4,4))
#fib()

