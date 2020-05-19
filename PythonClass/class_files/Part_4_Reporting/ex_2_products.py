# coding: utf-8

'''
TODO:
      1. Create a dictionary called products.
 
      2. Add these keys and values:
      		'HomePod': 349
      		'iPhone X': 999
      		'Watch': 1299
 
      3. Print the HomePod's price.
         
      4. Use a for loop to add together all the product prices 
         and print the total.
'''

products = {}

products["HomePod"] = 349
products["iPhone X"] = 999
products['Watch'] = 1299

total = 0
for item, value in products.items():
    if item == "HomePod":
        print "The price for {} is {}".format(item, value)
        total += value
    else:
        total += value

print total
