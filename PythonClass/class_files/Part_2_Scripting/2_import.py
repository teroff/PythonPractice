# coding: utf-8

'''
importing files

import allows you to read in code files and add extra functionality to your script.

When you import a file, Python first looks in your script's directory for that file.
If it's not found there, Python then looks in directories where third party
modules are installed, and then in directories where Python built-in modules
are installed. It imports the first file it finds with the specified name.
'''


# To import a file, use the filename without extension.
import sys			# The sys module gives access to useful information about the system.

# When imported, a file is turned into an object that you can use.
print type(sys)		# <type 'module'>

# As with any object, you can use dir() to see what you can do with it.
print dir(sys)

print sys.platform	# The operating system you are using.

print sys.version	# The version of Python you are running.

print sys.path		# A list of the directories Python looks in for modules.

for item in sys.path:
	print item