"""
Variables and Types

Python is completely object oriented, and not "statically typed". 
You do not need to declare variables before using them, or declare their type.
Every variable in Python is an object.

This tutorial will go over a few basic types of variables.


Numbers
Python supports two types of numbers - integers(whole numbers) and 
floating point numbers(decimals). (It also supports complex numbers, 
which will not be explained in this tutorial).

To define an integer, use the following syntax:
"""

myint = 7
print(myint)

"To define a floating point number, you may use one of the following notations:"


myfloat = 7.356
print(myfloat)
myfloat = float(12)
print(myfloat)



"""
Strings

Strings are defined either with a single quote, double quotes and a triple quote.

The difference between the two is that using double quotes makes 
it easy to include apostrophes (whereas these would terminate the string if using single quotes)

Triple quotes is used to print data in a same order as you want without using multiple print() or \n .
"""

mystring1 = 'hello'
print(mystring1)
mystring2 = "hello"
print(mystring2)
mystring3 = """
    Hello

        World!"""
print(mystring3)

"Simple operators can be executed on numbers and strings:"

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld1 = hello + " " + world
helloworld2 = f"hello world"
print(helloworld1)
print(helloworld2)
