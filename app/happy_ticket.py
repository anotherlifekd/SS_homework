import itertools


def moscow():
    count = 0
    for ticket in itertools.product(range(0, 10), repeat=6):
        if sum(ticket[:3]) == sum(ticket[3:]):
            count += 1
    return print(count)


def saint_petersburg():
    count = 0
    for ticket in itertools.product(range(0, 10), repeat=6):
        even = []
        odd = []
        for numbers in range(len(ticket)):
            if numbers % 2 == 0:
                even.append(ticket[numbers])
            else:
                odd.append(ticket[numbers])
        if sum(even) == sum(odd):
            count += 1
    return print(count)