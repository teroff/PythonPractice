#!/usr/bin/python

"""
Implement object permuation
"""


def permutation(element):
    """

    :param element:
    :return:
    """

    if len(element) <= 1:
        yield element

    else:
        for perm in permutation(element[1:]):
            for i in range(len(element)):
                yield perm[:i] + element[0:1] + perm[i:]


def permutations(word):
    if len(word) <=1:
        return [word]

    # get all permutations of length N-1
    perms = permutations(word[1:])
    char = word[0]
    result = []
    # iterate over all permutations of length N-1
    for perm in perms:
        # insert the character into every possible location
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])
    return result

print(permutations('123'))