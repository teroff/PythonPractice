# coding: utf-8

'''
if statement

Documentation:
	https://docs.python.org/2/tutorial/controlflow.html#if-statements
'''
# The = sign assigns a value:
pet = 'cat'


# A double equals sign == compares the values, returning True or False.
# So this statement asks if the variable pet holds a value
# equal to 'cat':
print pet == 'cat'	# True

# Is it equal to 'dog'?
print pet == 'dog'	# False


# Some math operations return True or False:
print 3 > 2			# True
print 3 > 5			# False


# if statements operate on True and False values.
if pet == 'cat':
	print "It's a cat!"

if pet == 'dog':
	print "It's a dog!"


# If you want to do something if the statement was false, you can use else:
if pet == 'dog':
	print "It's a dog!"
else:
	print "It's not a dog!"


# If the first statement is not true, you can do another comparison else using elif ("else if"):
if pet == 'dog':
	print "It's a dog!"
elif pet == 'cat':
	print "It's a cat!"


# You can have as many elif statements as you want.
# And you can still use else -- it will only be used if everything else was false.
if pet == 'dog':
	print "It's a dog!"
elif pet == 'bird':
	print "It's a bird!"
elif pet == 'swallow':
	print "It's a swallow!"
else:
	print "It's something else, not sure what."


# Given that if operates on any True/False value, you can also use it with a boolean variable:
monkeys_can_fly = False

if monkeys_can_fly:
	print "That's pretty cool!"
else:
	print "Too bad. I wish monkeys could fly."