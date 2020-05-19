# coding: utf-8

'''
TODO:
	1. Use a for loop to print each line in the file 'stanford.txt'.

	2. Count the number of lines and print the result.

	3. Write the result in the form "<count> lines" to a file called 'output.txt'.
'''

number_of_lines = 0
for line in open('numbers.txt', 'r'):
    number_of_lines += 1
    # print line

myresult = open('results.txt','w')

message = str(number_of_lines) + " lines\n"

myresult.write(message)

myresult.close()

with open('results.txt', 'w') as output:
    # message = str(number_of_lines) + " lines in the file\n"
    message = number_of_lines
    print message
    output.write(message)

"""
using enumerate
don't forget to increment by 1 because everything starts from 0
"""
for line, string in enumerate(open('numbers.txt')):
    num_of_lines = line + 1
print str(num_of_lines) + " lines in the file"