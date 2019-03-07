#!/usr/bin/python

# Fibonacci series using iterators in Python
#


def fib():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

def subFib(startNumber, endNumber):
    for cur in fib():
        if cur > endNumber: return
        if cur >= startNumber: yield cur

a = fib()
print(a)


for i in subFib(10,2000):
    print(i)
