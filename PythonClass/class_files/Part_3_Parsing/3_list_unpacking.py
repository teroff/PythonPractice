# coding: utf-8

'''
List unpacking
'''

animals = ['bird', 'cow', 'dog']

'''
If you have a list on the right side of the assignment,
and the same number of variables on the left side
of the assignment, the list values will be 'unpacked'
into the variables.
'''
first, second, third = animals
print first
print second
print third

'''
Your only choices are one variable, which becomes a pointer
to the list object, or the same number of variables as
in the list, in which case the values are unpacked.

If you provide a different number of variables,
it's an error.
'''
# first, second = animals		# ValueError: too many values to unpack


'''
Exercise: ex_3_us_stores.py
'''