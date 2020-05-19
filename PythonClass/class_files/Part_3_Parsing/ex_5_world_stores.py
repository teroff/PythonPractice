# coding: utf-8

'''
TODO: 
	1. Read in the spreadsheet of Apple stores 
	   ('world_stores.csv') using the csv module
	   and print each line in this format:

	   Country: Region (City)
'''


import csv

for index, row in enumerate(csv.reader(open('world_stores.csv', 'r'))):
    if index == 0: continue
    country, region, city = row[0], row[1], row[2]
    #country, region, city, location, url, info = row

    print "{country}: {region} ({city})".format(country=country, region=region.strip(), city=city.strip())