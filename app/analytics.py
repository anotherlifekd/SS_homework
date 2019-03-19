from app.ask import ask


def analytics(args):
    def envelope(a, b, c, d):
        if float(a) > float(c) and float(b) > float(d):
            return print('YES')
        else:
            return print('NO')

    def _check_args():
        if args.envelope_a is not None and args.envelope_b is not None and args.envelope_c is not None and \
                args.envelope_d is not None and args.envelope_a.replace('.', '', 1).isdigit() and \
                args.envelope_b.replace('.', '', 1).isdigit() and args.envelope_c.replace('.', '', 1).isdigit() and \
                args.envelope_d.replace('.', '', 1).isdigit() and float(args.envelope_a) > 0 and float(args.envelope_b) > 0 and \
                float(args.envelope_c) > 0 and float(args.envelope_d) > 0:
            return True
        else:
            return False

    while True:
        if _check_args():
            envelope(args.envelope_a, args.envelope_b, args.envelope_c, args.envelope_d)
            args.envelope_a = args.envelope_b = args.envelope_c = args.envelope_d = 'default'
        else:
            args.envelope_a = input('Enter a-side of the first envelope (number or float): ')
            args.envelope_b = input('Enter b-side of the first envelope (number or float): ')
            args.envelope_c = input('Enter a-side of the second envelope (number or float): ')
            args.envelope_d = input('Enter b-side of the second envelope (number or float): ')
            if _check_args():
                envelope(args.envelope_a, args.envelope_b, args.envelope_c, args.envelope_d)
                args.envelope_a = args.envelope_b = args.envelope_c = args.envelope_d = 'default'
            else:
                print('Parameters must be (number or float): ')
                continue

        if ask():
            continue
        else:
            break
