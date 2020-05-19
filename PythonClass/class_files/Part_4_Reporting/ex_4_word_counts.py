# coding: utf-8

'''
TODO:	1. Figure out how many times each word occurs in stanford.txt.

		2. Print the results in sorted order, in this format:

			word: #
'''

words = {'Words':0} # word: count

for line in open('stanford.txt', 'r'):
    line = line.translate(None, ".,?!:;’”")
    for word in line.split():
        word = word.lower()
        if word not in words:
            words['Words'] += 1
            words[word] = 1
        else:
            words[word] += 1

print words["Words"]

for item, value in sorted(words.items()):
    print "{}: {}".format(item, value)