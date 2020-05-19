# coding: utf-8


'''
List sorting
'''

animals = ['zebra', 'bird', 'cow', 'dog']


# sorted() returns a sorted copy of the list, useful when you don't want to change the original list.
print sorted(animals)
print sorted(animals, reverse = True)

# The sort() function is the same as sorted(), except it changes the list.
animals.sort()
print animals


'''
Exercise:	ex_2_sorted_words.py
'''