# coding: utf-8

'''
Functions

Documentation:
	https://www.tutorialspoint.com/python/python_functions.htm

A function allows you to re-use code without having to copy and paste
all the code every time you use it. Instead you can just call the function.

Functions have a name, and to call them you place parenthesis after the name:

	function_name()

If a function takes arguments, you pass those arguments in the parenthesis:

	function_name(argument)

A function can take multiple arguments, comma-separated:

	function_name(argument1, argument2)

If a function returns a value, you can assign the result to a variable:

	result = function_name()
'''

# max() is a built-in Python function that returns the highest number that was passed to it.
highest = max(5, 200, 1, 0)		# 200
print highest


# range() is a built-in Python function that gives you a list of numbers.
# By default it starts at zero and goes up to the specified number.
mynumbers = range(10)		# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print mynumbers

