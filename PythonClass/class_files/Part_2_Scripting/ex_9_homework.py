# coding: utf-8

'''
TODO:
	1. Use a for loop to read each line in the file 'numbers.txt'.

	2. Use int() to turn the text on the line into a number.

	3. Add up all the numbers in the file and write the result to 'results.txt'.

	The correct answer will be 6 digits and ends with a 0.
'''

import exercise_assistant


def readFile(textfile):
    total = 0
    for line, number in enumerate(open(textfile, 'r')):
        line += 1
        total += int(number)
    return line, total

def writeFile(resultfile, result):
    # print result
    with open(resultfile, 'w') as output:
        message = str(result)
        output.write(message)

def main():
    lines, total = readFile('numbers.txt')
    writeFile('results.txt',total)

if __name__ == '__main__':
    main()



