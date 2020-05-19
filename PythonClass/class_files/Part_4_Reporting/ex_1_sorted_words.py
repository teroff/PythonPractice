# coding: utf-8

'''
TODO:	1. Print a sorted list of all the words in stanford.txt.

		2. Print the number of words found.
'''


# words = []

# for line in open('stanford.txt', 'r'):
#     for word in line.split():
#         words.append(word)

# uniwords = set(words)
# print sorted(words)
# print len(words)
# print "\n"
# print uniwords
# print len(uniwords)


numbersofwords = {"Number":0}
for line in open('stanford.txt', 'r'):
    for word in line.split():
        new_word = word.lower()
        if new_word not in numbersofwords:
            numbersofwords[new_word] = 1
            numbersofwords["Number"] += 1
        else:
            numbersofwords[new_word] += 1

print numbersofwords
print numbersofwords["Number"]