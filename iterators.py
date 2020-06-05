# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:50:00 2019

@author: pythor
"""
'''
Iterators are objects that can be iterated upon. 
In this session, you will learn how iterator works and 
how you can build your own iterator 
using __iter__ and __next__ methods.
'''
'''

What are iterators in Python?
Iterators are everywhere in Python. 
They are elegantly implemented within for loops, 
comprehensions, generators etc. but hidden in plain sight.

Iterator in Python is simply an object that can be iterated upon. 
An object which will return data, one element at a time.

Technically speaking, Python iterator object must implement two 
special methods, __iter__() and __next__(), 
collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it. 
Most of built-in containers in Python 
like: list, tuple, string etc. are iterables.

The iter() function (which in turn calls the __iter__() method)
returns an iterator from them.
'''

'''
Iterating Through an Iterator in Python
We use the next() function to manually iterate 
through all the items of an iterator. 
When we reach the end and there is no more data to be returned, 
it will raise StopIteration.


Following is an example.
'''


## define a list
#my_list = [4, 7, 0, 3]
#
## get an iterator using iter()
#my_iter = iter(my_list)
##
## iterate through it using next()
#
#print(next(my_iter))
########
#print(next(my_iter))
############
############# next(obj) is same as obj.__next__()
############
#print(my_iter.__next__())
############
#print(my_iter.__next__())
############
############# This will raise error, no items left
#print(next(my_iter))

'''
How for loop actually works?
As we see in the above example, 
the for loop was able to iterate automatically 
through the list.

In fact the for loop can iterate over any iterable. 
Let's take a closer look at how the for loop is 
actually implemented in Python.
'''


##for element in iterable:
#     do something with element
## create an iterator object from that iterable

#iterable=[3,2,4,5,2,1]
#iter_obj = iter(iterable)
#
## infinite loop
#while True:
#    try:
#        # get the next item
#        element = next(iter_obj)
#        print(element)
#        # do something with element
#    except StopIteration:
#        # if StopIteration is raised, break from loop
#        break
#print('hello')

'''
So internally, the for loop creates an iterator object, 
iter_obj by calling iter() on the iterable.

Ironically, this for loop is actually an infinite while loop.

Inside the loop, it calls next() to get the 
next element and executes the body of the 
for loop with this value. 
After all the items exhaust, 
StopIteration is raised which is internally caught and the loop ends. 
Note that any other kind of exception will pass through.
'''


'''
Building Your Own Iterator in Python?
Building an iterator from scratch is easy in Python. 
We just have to implement the methods __iter__() and __next__().

The __iter__() method returns the iterator object itself.
If required, some initialization can be performed.

The __next__() method must return the next item in the sequence. 
On reaching the end, and in subsequent calls, it must raise StopIteration.

Here, we show an example that will give us next power of 2 in each iteration. 
Power exponent starts from zero up to a user set number.
'''

#class PowTwo():
#    """Class to implement an iterator
#    of powers of two"""
#
#    def __init__(self, maxo = 0):
#        self.maxo = maxo
#
#    def __iter__(self):
#        self.n = 0
#        return self
#
#    def __next__(self):
#        if self.n <= self.maxo:
#            result = 2 ** self.n
#            self.n += 1
#            return result
#        else:
#            raise StopIteration
#a = PowTwo(5)
#i = iter(a)
#print(next(i))
#print(next(i))
#print(next(i))
#print(next(i))
#print(next(i))
#print(next(i))
#print(next(i))
