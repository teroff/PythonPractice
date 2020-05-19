# coding: utf-8

'''
csv's dictionary support

You can use the csv module to read in each row as a dictionary, with the header names as the keys.
'''
import csv

for store in csv.DictReader(open('world_stores.csv', 'r')):
	print store