import itertools
import os
from app.ask import ask


def tickets():
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

    while True:
        try:
            file_name = input('<File name.format>: ')
            BASE_DIR = os.path.join(os.getcwd(), file_name)

            with open(BASE_DIR) as file:
                word = file.read().lower()
                if 'moscow' in word:
                    moscow()
                elif 'piter' in word:
                    saint_petersburg()
                else:
                    print('ERROR')
        except IndexError:
            print('Enter the correct parameters <File-name.format>:')
            continue

        if ask():
            continue
        else:
            break
