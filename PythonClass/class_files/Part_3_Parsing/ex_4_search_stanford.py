# coding: utf-8

'''
TODO:	1. How many times does the word 'college' appear in stanford.txt?
'''

total = 0

for line in open('stanford.txt', 'r'):
    total += line.lower().count('college')
    # for word in line.split():
    #     print word
    #     # if word.lower == "college":
    #     #     print "yay"
print total