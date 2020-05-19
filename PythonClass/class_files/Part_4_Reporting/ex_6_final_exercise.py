# coding: utf-8

'''
TODO:	1. Using 'world_stores.csv', determine how many stores are in each country.

		2. Sort the results and write them to a file called 'results.txt' in this format,
           one country per line:

           country: count
'''
import csv

worlrdstores = {} # country: count

for line in csv.DictReader(open('world_stores.csv', 'r')):

    # the line below is exactly the same a the following 4 lines of code
    # with if and else statements of checking and adding items to the dictionary
    #
    worlrdstores[line['Country']] =  worlrdstores.get(line['Country'], 0) +1

    # if line['Country'] not in worlrdstores:
    #     worlrdstores[line['Country']] = 1
    # else:
    #     worlrdstores[line['Country']] += 1

print worlrdstores

with open('results.txt', 'w') as output:
    for country, stores in sorted(worlrdstores.items()):
        print "{}: {}\n".format(country, stores)
        output.write("{}: {}\n".format(country, stores))

import exercise_assistant
