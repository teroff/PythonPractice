# coding: utf-8

'''
TODO:	1. Get a list of all store countries from world_stores.csv.

		2. Sort the list.

		3. Print the sorted countries, one country per line.
'''

import csv

countries = []
for line in csv.DictReader(open('world_stores.csv', 'r')):
    if line['Country'] not in countries:
            countries.append(line['Country'])

print "Number of countries: {}".format(len(countries))
for c in sorted(countries):
    print c