#!/usr/bin/python

def isPrime(n):
    """
    Returns True if number is prime
    Returns False if number is false
    """
    if n == 0:
        return "0 is not a number"

    if n == 1 or n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= w:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

        return True