from app.ask import ask


def fibo_range(args):
    def fibonacci(num):
        a, b = 0, 1
        for i in range(num):
            a, b = b, a + b
            if a < num:
                yield a
            else:
                break

    def count_fib(first, second):
        lst = []
        for fib in fibonacci(int(second)):
            if fib >= int(first):
                lst.append(fib)
            else:
                continue
        return print(lst)

    def _check_args():
        if args.arg_1 is not None and args.arg_2 is not None and args.arg_1.isdigit() and args.arg_2.isdigit() \
                and args.arg_1 != 'default' and args.arg_2 != 'default':
            return True
        else:
            return False

    while True:
        if _check_args():
            count_fib(args.arg_1, args.arg_2)
            args.arg_1 = args.arg_2 = 'default'
        else:
            args.arg_1 = input('Set start: ')
            args.arg_2 = input('Set end: ')
            if _check_args():
                count_fib(args.arg_1, args.arg_2)
                args.arg_1 = args.arg_2 = 'default'
            else:
                print('Enter the correct parameters. Should be positive number')
                continue

        if ask():
            continue
        else:
            break
