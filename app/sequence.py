import math


def sequence(n):
    lst = []
    for i in range(int(math.sqrt(int(n)) + 1)):
        if i * i >= int(n):
            break
        else:
            lst.append(str(i))
    return print(', '.join(lst))