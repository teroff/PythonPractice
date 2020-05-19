# coding: utf-8

'''
TODO:	1. Print all the numbers in stanford.txt.

		2. Add together all the numbers and write the answer to 'results.txt'.
'''

# Your code here

def readFile(filename):
    total = 0
    for index, line in enumerate(open(filename, 'r')):
        for word in line.split():
            word = word.translate(None, "$¢.s,")
            if word.isdigit():
                total += int(word)
    return total

def writeResult(result, resultFile):
    with open(resultFile, 'w') as myfile:
        myfile.write(str(result))

def main():
    read_file = "stanford.txt"
    result_file = "results.txt"

    writeResult(readFile(read_file),result_file)

if __name__ == '__main__':
    main()


import exercise_assistant