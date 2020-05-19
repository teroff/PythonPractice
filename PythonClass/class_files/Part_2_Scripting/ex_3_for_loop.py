# coding: utf-8

'''
TODO:
	1. Use a for loop to print each item in the products list.

	2. Only print the items that don't start with 'i'.
	   You can use the string's startswith() method for this.
'''

products = ['iPod', 'HomePod', 'iPhone X', 'Watch', 'MacBook']

for product in products:
    print product

for product in products:
    if product.startswith("i"):
        continue
    else:
        print product

for product in products:
    if len(product) and product[0] != "i":
        print product