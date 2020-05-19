# coding: utf-8

'''
The csv module

Never do your own parsing of csv files.
The format is more complicated that it seems,
with a number of edge cases.

Use the built-in csv module.
'''
import csv


'''
One approach is to use the csv.reader() method
to read a csv file. The reader() method takes
a file object and returns a list of rows.
Each row is a list of the values on that row.
'''
# csv_file = open('world_stores.csv', 'r')
# for row in csv.reader(csv_file):
# 	print row		# ['United States', 'Oklahoma', 'Tulsa', ' Woodland Hills', '']

for row in csv.reader(open('us_stores.csv', 'r')):
    print row

'''
Exercise: ex_1_world_stores.py 
'''