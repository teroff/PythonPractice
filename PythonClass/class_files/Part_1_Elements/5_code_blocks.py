# coding: utf-8

'''
Code blocks
'''
pet = 'cat'

# A code block is indented code, as we saw with the if statements:
if pet == 'cat':
	# These indented lines are the code block.
	# They are only executed if the if statement is True.
	print "It's a cat!"
	print "I like cats."


# Code blocks are always preceded by a line that ends with colon:
if pet == 'dog':
	print "It's a dog!"


# Every line in a code block must be indented the same way.
# You can use any indentation you want, as long as each line uses the same indentation.
if pet == 'sloth':
  print "I like sloths."
  print "They are cool."


# The code block is closed by the first unindented line:
if pet == 'cat':
	print "Lions are cats too."
	print "Pretty cool fact."
print "By being unindented, this line closes the code block. It's not part of the block, but it does close it."

