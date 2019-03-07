#!/usr/bin/python

def fib(n):
    """
    return fibonacci of number n
    :param n:
    :return:
    """

    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    else:
        return fib(n-1)+fib(n-2)


print(fib(50))