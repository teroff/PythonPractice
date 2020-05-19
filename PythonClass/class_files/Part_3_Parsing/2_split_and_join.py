# coding: utf-8

'''
split() and join() methods
'''


# The string methods split() and join() are common ways to manipulate strings.
slogan = "Python is my favorite language"
words = slogan.split()
print words

# The items are joined with whatever you specified as the separator between items.
print '-'.join(words)

# Another way to "change" a string is to turn it into a list and change the list, 
# then turn it back into a string.
words[2] = "everyone's"
slogan = ' '.join(words)
print slogan

# Split on other characters


'''
Exercise: 
	ex_2_words.py
'''