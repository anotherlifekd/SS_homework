import os
from app import chess, analytics, fibonacci, files, geron_triangle, happy_ticket, numbers, sequence, ask
import check_errors
from arguments import arguments

TASK = ('chess', 'analytics', 'geron_triangle', 'files', 'sequence', 'numbers', 'fibonacci', 'happy_ticket')

if __name__ == '__main__':

    args = arguments.parse()

    while True:
        if args.choose == 'chess':
            while True:
                if check_errors.check(args):
                    chess.ChessBoard(str(int(int(args.height) / 2)), str(int(int(args.width) / 2))).board()
                    args.height = 'default'
                else:
                    args.width = input('Enter a numeric value of the width of the chessboard: ')
                    args.height = input('Enter a numeric value of the height of the chessboard: ')
                    if check_errors.check(args):
                        chess.ChessBoard(str(int(int(args.height) / 2)), str(int(int(args.width) / 2))).board()
                        args.height = 'default'
                    else:
                        print('Enter the correct parameters. Width and height should be even positive number')
                        continue

                if ask.ask():
                    continue
                else:
                    break
        if args.choose == 'analytics':
            while True:
                if check_errors.check(args):
                    analytics.analytic(args.envelope_a, args.envelope_b, args.envelope_c, args.envelope_d)
                    args.envelope_a = args.envelope_b = args.envelope_c = args.envelope_d = 'default'
                else:
                    args.envelope_a = input('Enter a-side of the first envelope (number or float): ')
                    args.envelope_b = input('Enter b-side of the first envelope (number or float): ')
                    args.envelope_c = input('Enter a-side of the second envelope (number or float): ')
                    args.envelope_d = input('Enter b-side of the second envelope (number or float): ')
                    if check_errors.check(args):
                        analytics.analytic(args.envelope_a, args.envelope_b, args.envelope_c, args.envelope_d)
                        args.envelope_a = args.envelope_b = args.envelope_c = args.envelope_d = 'default'
                    else:
                        print('Parameters must be (number or float): ')
                        continue

                if ask.ask():
                    continue
                else:
                    break
        if args.choose == 'geron_triangle':
            while True:
                if check_errors.check(args):
                    print(geron_triangle.geron_triangle(args.triangle_a, args.triangle_b, args.triangle_c))
                    args.triangle_name = args.triangle_a = args.triangle_b = args.triangle_c = 'def'
                else:
                    while True:
                        result = {}
                        arg_list = []
                        while True:
                            arg_list.append(input('Enter <triangle name>, <side a>, <side b>, '
                                                  '<side c> (Parties must be number or float): ').split(','))
                            ask_triangle = input('Add triangle? (Y / YES): ').lower()
                            if ask_triangle == 'y' or ask_triangle == 'yes':
                                continue
                            else:
                                break
                        for i in arg_list:
                            result[i[0]] = result.get(i[0], 0) + geron_triangle.geron_triangle(i[1], i[2], i[3])
                        for name, value in sorted(result.items(), key=lambda x: x[1], reverse=True):
                            print(f'{name}: {value} cm')

                        if ask.ask():
                            continue
                        else:
                            break
                    break
        if args.choose == 'files':
            while True:
                if args.mod == 'c' and args.files_name != '0' and args.string_for_count != '0':
                    files.file(args.files_name, args.mod, args.string_for_count)
                    args.mod = '0'
                elif args.mod == 'r' and args.files_name != '0' and args.string_for_search != '0' \
                        and args.string_for_replace != '0':
                    files.file(args.files_name, args.mod, string_for_search=args.string_for_search,
                               string_for_replace=args.string_for_replace)
                    args.mod = '0'
                else:
                    mod = input('Which mod do you want to choose? (type C to count / type R to replace '
                                '/ type anything else to exit): ').lower()
                    if mod == 'c':
                        try:
                            direction_count = input('<direction of your file>, <counted string>: ').replace(' ', '') \
                                .split(',')
                            files.file(direction_count[0], mod, direction_count[1])
                        except IndexError:
                            print('Enter the correct parameters')
                            continue
                    elif mod == 'r':
                        try:
                            direction_replace = input(
                                '<direction of your file>, <search string>, <replace string>: ').replace \
                                (' ', '').split(',')
                            files.file(direction_replace[0], mod, string_for_search=direction_replace[1],
                                       string_for_replace=direction_replace[2])
                        except IndexError:
                            print('Enter the correct parameters')
                            continue
                    else:
                        break

                if ask.ask():
                    continue
                else:
                    break
        if args.choose == 'sequence':
            while True:
                if args.n.isdigit():
                    sequence.sequence(args.n)
                    args.n = 'default'
                else:
                    n = input('Set n: ').lower()
                    sequence.sequence(n)
                if ask.ask():
                    continue
                else:
                    break
        if args.choose == 'numbers':
            while True:
                if args.num.isdigit():
                    numbers.numbers(int(args.num))
                    args.num = 'default'
                else:
                    n = input('Set your number: ').lower()
                    numbers.numbers(int(n))
                if ask.ask():
                    continue
                else:
                    break
        if args.choose == 'fibonacci':
            while True:
                # if args.arg_1 is not None and args.arg_2 is not None:
                if args.arg_1.isdigit() and args.arg_2.isdigit():
                    fibonacci.count_fib(args.arg_1, args.arg_2)
                    args.arg_1 = args.arg_2 = 'default'
                else:
                    args.arg_1 = input('Set start: ')
                    args.arg_2 = input('Set end: ')
                    fibonacci.count_fib(args.arg_1, args.arg_2)
                if ask.ask():
                    continue
                else:
                    break
        if args.choose == 'happy_ticket':
            while True:
                try:
                    file_name = input('<File name.format>: ')
                    BASE_DIR = os.path.join(os.getcwd(), file_name)
                    with open(BASE_DIR) as file:
                        word = file.read().lower()
                        if 'moscow' in word:
                            happy_ticket.moscow()
                        elif 'piter' in word:
                            happy_ticket.saint_petersburg()
                        else:
                            print('ERROR')
                except IndexError:
                    print('Enter the correct parameters <File-name.format>:')
                    continue

                if ask.ask():
                    continue
                else:
                    break

        global_menu = input(f'CHOICE OF TASK: \n 1. {TASK[0]} \n 2. {TASK[1]} \n 3. {TASK[2]} \n 4. {TASK[3]} \n '
                            f'5. {TASK[4]} \n 6. {TASK[5]} \n 7. {TASK[6]} \n 8. {TASK[7]} \n '
                            f'9. Write something else to exit \n Enter the task: ').lower()

        if global_menu in TASK:
            args.choose = global_menu
            continue
        else:
            break
