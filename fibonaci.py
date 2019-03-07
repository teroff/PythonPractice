# fibonacci sequence in Python

def f(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return f(n - 1) + f(n - 2)


def f_itter():
    a, b = 0, 1
    while True:
        yield a

        a, b = b, a + b


def f_sequence(startNumber, finishNumber):
    for cur in f_itter():
        if cur > finishNumber:
            return
        if cur >= startNumber:
            yield cur


for i in f_sequence(5, 155):
    print(i)
