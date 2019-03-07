#!/usr/bin/python

# check if list2 is a rotation of list1


def isRotation(list1, list2):
    if len(list1) != len(list2):
        return False

    key = list1[0]
    key_counter = 0

    for i in range(len(list2)):
        if list2[i] == key:
            key_counter = i
            break

    if key_counter == 0:
        return False

    for x in range(len(list1)):
        l2_index = (key_counter + x) % len(list1)

        if list1[x] != list2[l2_index]:
            return False

    return True


print(isRotation([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 1, 2, 3]))
