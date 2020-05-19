# coding: utf-8

'''
Finding text
'''


if 'Python' in "Monty Python":
	print "It's a Python!"

print 'parrot'.count('r')			# 2

print 'parrot'.endswith('t')		# True

print 'parrot'.startswith('t')	# False

# find() and rfind() return -1 if nothing found.
print 'find first'.find('i')		# 1

print 'locate last'.rfind('l')	# 7

print 'alphanumeric42'.isalnum()		# True

print 'alphabetic'.isalpha()			# True

print '42'.isdigit()					# True

print ' \t\r\n'.isspace()				# True

print 'All Capitalized'.istitle()		# True

print 'ALL UPPERCASE'.isupper()		# True

print 'before|after'.partition('|')	# ('before', '|', 'after')

print 'first|first last|last'.rpartition('|')		# ('first|first last', '|', 'last')

print 'parrot asleep'.replace('asleep', 'deceased')	# parrot deceased

print 'first\nsecond\nthird'.splitlines()	# ['first', 'second', 'third']

print "this is my Dog?".translate(None, " ?g") # deletes all the provided charaters from the string


'''
Exercise:	ex_4_search_stanford.py
'''