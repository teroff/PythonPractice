# coding: utf-8

'''
String formatting
'''


# In the simplest form, use the string.format() method to interpolate values.
# The format() method replaces {} with the value passed as an arguement.
text = "Insert the value here: {}".format(10)

# You can insert as many values as you like.
text = "The {} brown fox jumps over the {} dog".format("quick", "lazy")
print text

# If you think of the string as a re-usable template, it becomes more powerful.
# Remember that since strings are immutable, the format method returns a new version of the
# string, leaving the original template as-is.
template = "The {} brown fox jumps over the {} dog"
first = template.format("careless", "ambivalent")
second = template.format("bad", "delighted")
print first
print second

# You can specify an index order (starts with 0) for the arguments.
template = "The {1} brown fox jumps over the {0} dog"
first = template.format("lazy", "quick")
print first

# The template can have named values, letting you assign them in any order.
# In this case you are required to provide the named arguments.
template = "The {fox_type} brown fox jumps over the {dog_type} dog"
first = template.format(dog_type="spotted", fox_type="springy")
print first

# Using either named values or index order, you can then have the template access a dictionary item.
template = "The {0[fox_type]} brown fox jumps over the {0[dog_type]} dog"
myDict = {"fox_type": "little", "dog_type": "rotund"}
first = template.format(myDict)
print first

# You can also call a method or access an attribute.
import sys
template = "You are running on {0.platform}"
first = template.format(sys)
print first

# You can also format numbers.
# This will print the number as provided.
print "{}".format(3.141592653589793)	# 3.14159265359

# This will round the float to 3 trailing digits.
print "{:0.3f}".format(3.141592653589793)	# 3.142

'''
Exercise: ex_3_us_stores.py
'''