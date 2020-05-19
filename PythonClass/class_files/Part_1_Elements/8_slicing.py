# coding: utf-8

'''
Slicing lists

To get a subset of a list, you can 'slice' it -- this returns a new list with the requested items.
'''
animals = ['cat', 'swallow', 'bird', 'sloth', 'alligator']

# To slice a list, provide a starting index and ending index, separated by a colon.
print animals[1:4]		# ['swallow', 'bird', 'sloth']

# The slice starts at the starting index and goes *up to* the ending index, not including the ending index.
# The easy way to know what you'll get is to subtract the starting index from the ending index;
# the result is the number of items you'll get.
print animals[2:4]		# 4-2 = 2, so I get 2 items: ['bird', 'sloth']

# If you leave out the ending index, it will go to the end:
print animals[2:]		# ['bird', 'sloth', 'alligator']

# If you leave out the starting index, it will start at the beginning of the list:
print animals[:3]		# ['cat', 'swallow', 'bird']

# Negative numbers are very useful when slicing -- this gives the last three items of the list:
print animals[-3:]		# ['bird', 'sloth', 'alligator']

# This gives up to the last three items:
print animals[:-3]		# ['cat', 'swallow']
