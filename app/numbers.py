from app.ask import ask


def digit_to_string(args):
    def numbers(number):
        FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
                     "eight", "nine"]
        SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                      "sixteen", "seventeen", "eighteen", "nineteen"]
        OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
                      "eighty", "ninety"]
        HUNDRED = "hundred"

        n = number // 100
        t = [FIRST_TEN[n - 1], HUNDRED] if n > 0 else []

        n = (number // 10) % 10
        t += [OTHER_TENS[n - 2]] if n > 1 else []

        n = number % (10 if n > 1 else 20)
        t += [(FIRST_TEN + SECOND_TEN)[n - 1]] if n > 0 else []

        return print(' '.join(t))

    def _check_args():
        if args.num is not None and args.num.isdigit() and args.num != 'default' and int(args.num) < 1000:
            return True
        else:
            return False

    while True:
        if _check_args():
            numbers(int(args.num))
            args.num = 'default'
        else:
            args.num = input('Set your number: ').lower()
            if _check_args():
                numbers(int(args.num))
                args.num = 'default'
            else:
                print('Enter the correct parameters. N - should be positive number and less than 1000')
                continue

        if ask():
            continue
        else:
            break
