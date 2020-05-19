# coding: utf-8

'''
Reading files line by line

Documentation:
	https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files

'''


'''
You should never read in all file contents at once 
unless you know the file will be small.

In most cases, in case you get a large file you want
to read a file one line at a time, which you can do 
with a for loop.

When opening the file as part of the for loop, 
the file will also be closed automatically for you
at the end of the loop.
'''
for line in open('products.txt', 'r'):
	print line


'''
Because there's a newline at the end of the line in the file, 
and print adds a newline, we get doubled newlines. 

We can use the string's rstrip() method to strip whitespace 
from the right side of the line.
'''
for line in open('products.txt', 'r'):
	print line.rstrip()

'''
Exercise: ex_5_read_lines.py
'''