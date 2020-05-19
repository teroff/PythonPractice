# coding: utf-8

'''
Files

Documentation:
	https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files

'''

'''
The open() function is used for file handling.

	open(path, file_mode)

The first argument to open is the path of the file,
as a string.

The second argument is the 'file mode', also as a string.
The file mode indicates what you are going to do to the file.

File modes: 
	'r' = read
	'w' = write    
    'a' = append
'''


# Open the specified file for reading.
myfile = open('products.txt', 'r')
contents = myfile.read()			# This reads the entire file in at once.
myfile.close()						# When opened this way, the file must be closed when you are done.
print contents

# Writing files
# As with reading files, the open() function is used to write files.
# The file mode is either set to 'w' for write or 'a' for append.
# Writing or appending creates the file if it doesn't already exist.
output = open('output.txt', 'w')

# The write() method writes out to the file.
# You must add a \n wherever you want a newline in the file.
output.write("Here's to the crazy ones.\n")

# Writing again appends the content to what you've already written.
output.write("The misfits.\nThe rebels.\nThe troublemakers.\n")

# You must close the file when done with it.
output.close()

'''
Exercise: ex_4_read_file.py
'''