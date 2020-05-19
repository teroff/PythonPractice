# coding: utf-8

'''
Strings

Documentation:
	https://docs.python.org/2/tutorial/introduction.html#strings
'''

# Strings are text, a string of characters.
'not much'
"not much"

'''
There's no difference between single and double quotes except 
that you can avoid escaping the other kind of quote.

That is, if you use double quotes and want a double quote in the string, you have to escape it:
'''
"not \"much\" spam in it"

# But using single quotes lets you have a double-quote in the string:
'not "much" spam in it'

# Using double quotes lets you have a single-quote in the string:
"There's an apostrophe in here!"

# Strings can be added together.
"This is " + "two strings added together."

'''
Anything outside of quotes is considered code.
But anything inside quotes is treated as text.
Because the + below is inside the quotes, it's text
and not code.
'''
"This is + two strings added together."

# The print statement prints text for the user to read.
print "This is for you, user!"

# The print statement supports a comma to concatenate strings.
# The comma also adds a space between the strings.
print "print lets you add strings using a", "comma"

# The comma also converts non-text items to text.
print "This is my number:", 42