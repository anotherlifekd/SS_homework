import math
from app.ask import ask


def numeric_sequence(args):

    def sequence(number):
        lst = []
        for i in range(int(math.sqrt(int(number)) + 1)):
            if i * i >= int(number):
                break
            else:
                lst.append(str(i))
        return print(', '.join(lst))

    def _check_args():
        if args.n is not None and args.n.isdigit() and args.n != 'default':
            return True
        else:
            return False

    while True:
        if _check_args():
            sequence(args.n)
            args.n = 'default'
        else:
            args.n = input('Set n: ').lower()
            if _check_args():
                sequence(args.n)
            else:
                print('Enter the correct parameters. N - should be positive number')
                continue

        if ask():
            continue
        else:
            break
