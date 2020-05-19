# coding: utf-8

'''
Lists

Documentation:
	https://docs.python.org/2/tutorial/introduction.html#lists

Lists have an order to their items, and are changeable (mutable).
'''

# Square brackets create an empty list.
animals = []

# The append() method adds an item to the end of the list.
animals.append('cat')
animals.append('frog')
animals.append('bird')

# Or you can create a list from scratch like this, with the items comma-separated:
animals = ['cat', 'frog', 'bird', 'sloth', 'alligator']

# To access an item in the list, indicate the item number in brackets.
# Python lists are zero-based, meaning the first item is item #0.
first = animals[0]

# Negative numbers index from the end of the list, so -1 is the last item in the list.
last = animals[-1]

# You can change an item in the list.
animals[1] = 'swallow'

# Use the len() function to get the count of any kind of list.
count = len(animals)
if count > 2:
	print "That's a lot of animals!"


# To check for an item in the list, use 'if in'.
if 'dog' in animals:
	print 'Found a dog!'
elif 'bird' in animals:
	print 'Found a bird!'
else:
	print 'Found nothing!'

# You can also check for something *not* being in the list.
if 'cow' not in animals:
	print "Where's the beef?"