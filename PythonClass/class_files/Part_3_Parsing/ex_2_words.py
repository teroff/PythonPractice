# coding: utf-8

'''
TODO: 
	1. Count the number of words in the file 'stanford.txt'. 
	   The string's split() method will be helpful.

	2. Print the result.
'''


# myfile = open('stanford.txt','r')
# data = myfile.read()
# myfile.close()

total = 0
for line in open('stanford.txt','r'):
    words = line.split()
    total += len(words)


print total

