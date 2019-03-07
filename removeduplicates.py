#!/usr/bin/python

"""

Remove duplicates characters in a given stringRemove duplicates characters in a given string keeping the only first occurrences. For example,
is the input is "Public Relationship" the output should be "Public Reatonshp"

We need a data structure to keep track of the characters we have seen so far, which can perform efficient find
operation. Assuming we don't know the string format: ASCII or Unicode, we need to use a data type that would support
our needs.
For example, if we know that the input will be in ASCII form, we can just create a boolean array of size 128 and perform
lookup by indexing the character's value. In the case on Unicode though, we need to use a much larger array of size
more than 100K.

Set data structure perfectly suits our needs.

We can use an array as a return object and use "".join(result) to convert array to string format,  but I decided to use
string directly to avoid all the cost of conversion.

"""


def removeDuplicate(string, keepSpace=True):

    seen = set()
    result = ""

    for char in string:
        if char not in seen:
            seen.add(char)
            result+=char

        elif char == " " and keepSpace:
            result+=char

    return result

print(removeDuplicate("Public Relationship"))