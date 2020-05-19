# coding: utf-8

'''
Strings as lists
'''


# In Python, a string is considered a list.
# Being a list, all the standard list functionality works on strings.
language = "Python"
for character in language:
	print character

print language[3]
print language[-1]

if 'Py' in language:
	print "Let's have Py!"

print language[2:5]

print len(language)


'''
Strings are immutable
'''

# Unlike standard lists, strings are immutable (that is, they can't be changed).
# That means that functions that appear to change strings actually return new strings.
text = "HELLO!"

print text.lower()	# This returns a new string, it doesn't change the original string.
print text

# A workaround for creating a string is to assign the changed string to the original variable.
text = text.lower()
print text

print text.replace('h', 'z')

'''
Exercise:	
	ex_1_slicing_strings.py
'''