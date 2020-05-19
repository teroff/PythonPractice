# coding: utf-8

'''
TODO:
	1. Open the file 'stanford.txt' for reading.

	2. Print out the contents.
'''

# my_file = open('stanford.txt', 'r')

# content = my_file.read()

# my_file.close()

# print content


"""
It's always better to read line by line, because it uses a single line at a time

and opening a file using for loop closes the file after loop is done.

Which is aweseom (c)
"""

for line in open("numbers.txt", "r"):
    print line.strip()