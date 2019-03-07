#!/usr/bin/python


# Reverse string
#
# start - This is super
# finish - super is This

def reverse(s):
    if len(s) < 2:
        return "Lenght of the string is too short"

    length = len(s)
    words = []
    spaces = " "
    i = 0

    while i < length:
        if s[i] not in spaces:
            wordstat = i

        while i < length and s[i] not in spaces:
            i += 1

        words.insert(0, s[wordstat:i])
        i += 1

    return " ".join(words)


t = "This is super"

print(reverse(t))
