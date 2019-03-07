#!/usr/bin/python

def binary_search(list, value):

    list = sorted(list)
    min = 0
    max = len(list) - 1

    while min <= max:
        mid = (min + max) // 2

        if list[mid] < value:
            min = mid + 1

        elif value < list[mid]:
            max = mid - 1

        else:
            return mid

    return -1

l = [3, 6, 14, 48 ,75, 87, 15, 16, 33, 55, 56, 89]
x = 56

print(binary_search(l,x))