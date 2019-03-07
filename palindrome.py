#!/usr/bin/python

def reverseString(s):
    """
    :param s:
    :return:
    """

    if len(s) < 2:
        return "Not enough charachters"
    else:
        i = len(s) - 1
        revs = ""

        while i >= 0:
            revs = revs + str(s[i])
            i = i - 1
        return revs


def isPalindrom(s1, s2):
    """

    :param s1:
    :param s2:
    :return:
    """

    if s1 == s2:
        return True
    else:
        return False


word = "aba"

print(isPalindrom(word, reverseString(word)))
