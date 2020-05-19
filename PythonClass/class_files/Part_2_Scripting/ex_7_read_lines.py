# coding: utf-8

'''
TODO:
	1. Use a for loop to read the file 'numbers.txt'.
	2. Print out the file line by line.
'''


for line in open('numbers.txt', 'r'):
    print line.strip()