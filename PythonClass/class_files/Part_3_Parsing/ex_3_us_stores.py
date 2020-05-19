# coding: utf-8

'''
TODO:	1. Read the spreadsheet of US Apple stores ('us_stores.csv') and
		   print out each line.

		2. Figure out how to get the city, location, and URL
		   data from the line.

		3. Then change it so you are printing out each store location
		   in this format:

			  City: Location (URL)

		   For example:

	  		  Anchorage: Anchorage 5th Avenue Mall (/retail/anchorage5thavenuemall)
'''


# for line in open('us_stores.csv','r'):
#     # data = line.strip().split(',')

#     if "City" in line: continue

#     city, location, url = line.strip().split(',')

#     # print "{}: {} ({})".format(data[0], data[1], data[2])
#     print "{city}: {location} ({url})".format(city=city, location=location, url=url)


for index, line in enumerate(open('us_stores.csv', 'r')):
    if index == 0: continue
    city, location, url = line.strip().split(',')
    print "{city}: {location} ({url})".format(city=city,location=location, url=url)
