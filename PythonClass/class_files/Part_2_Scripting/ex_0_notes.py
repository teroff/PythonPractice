# coding: utf-8

'''
Notes file: For taking notes and playing around!
'''


"""
string formating
"""

name = "Stanley"
job = "QA"
num = 42

print "{}: {}, {}".format(name,job,num)

print "{name}: {job}, {num}".format(name = name, job = "Teaching", num = num)

print "{0}: {1} and {0}".format(name, "Teaching", num)