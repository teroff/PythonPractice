#!/usr/bin/python

def findMissing(l):
    """
    Find missing element in an array of integers
    :param l:
    :return: missing element
    """

    nxt = 1

    missingElements = set()

    while nxt < len(l) + 1:
        if nxt != l[nxt - 1]:
            missingElements.add(nxt)

        nxt += 1
    return missingElements


def findAllMising(l):
    new_l = set()
    [new_l.add(x) for x in range(min(l), max(l) + 1)]

    output = []

    for i in new_l:
        if i not in l: output.append(i)

    return output


print(findAllMising([1, 2, 3, 5, 6, 9]))

l = [1, 2, 4, 5, 6, 8]
print(findMissing(l))


def findMissing(list):
    l = []
    [l.append(x) for x in range(list[0], list[-1] + 1)]
    missing = sum(l) - sum(list)
    return missing


def findMissingTwoArrays(list1, list2):
    """
    There is an array of non-negative integers. A second array is formed by
    shuffling the elements of the first array and deleting a random element.
    Given these two arrays, find which element is missing in the second array.
    Here is an example input, the first array is shuffled and the number 5 is
    removed to construct the second array.
    list1 = [4,1,0,2,9,6,8,7,5,3]
    list2 = [6,4,7,2,1,0,8,3,9]
    """
    result = set()

    for i in list1:
        if i not in result:
            result.add(i)

    for i in list2:
        if i in result:
            result.remove(i)

    return result


def findMissingUsingXor(list1, list2):
    result = 0

    for i in list1 + list2:
        result ^= i

    return result


print(findMissingTwoArrays([4, 1, 0, 2, 9, 6, 8, 7, 5, 3], [6, 4, 7, 2, 1, 0, 8, 3, 9]))
print(findMissingUsingXor([4, 1, 0, 2, 9, 6, 8, 7, 5, 3], [6, 4, 7, 2, 1, 0, 8, 3, 9]))
