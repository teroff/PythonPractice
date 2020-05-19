# coding: utf-8

'''
Objects

Everything in Python is an object. 
Objects have attributes and methods.
'''
answer = 42

# Use type() to see what kind of object it is:
print type(answer)		# It's an 'int' object.

# Use dir() -- short for directory -- to see what attributes and methods an object has:
print dir(answer)

# By convention, the items that start with an underscore are 'private' for the implementor
# of the object, and shouldn't be called.

# To get the documentation for an object, ask for help for that object type:
print help('int')

# To get the documentation for just one attribute or method, use dot notation:
print help('int.numerator')

# To access an attribute or call a method, use dot notation on the object:
print answer.numerator		# attributes don't have parenthesis
print answer.denominator

# Methods must be called using parenthesis.
print help('int.bit_length')
print answer.bit_length		# Using a method name without parenthesis gives a pointer to the method:
							# <built-in method bit_length of int object at 0x7fb54dd039e8>

print answer.bit_length()	# Using the method name with parenthesis actually calls the method.


# Numbers can be added together...
print 42 + 5

# Strings can be added together...
print "This is " + "a concatenated string"

# Strings and numbers cannot be added together...
#print "horses" + 5		# TypeError: cannot concatenate 'str' and 'int' objects

# You must indicate how you want them added together...
# If you want the number to be treated as a string, use the str() functiuon:
print "horses" + str(5)		# horses5

# If you want the string treated as a number, use the int() function:
print int("40") + 2			# 42

