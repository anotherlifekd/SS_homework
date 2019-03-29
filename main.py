from app import chess, analytics, fibonacci, files, geron_triangle, happy_ticket, numbers, sequence, ask
from arguments import arguments

TASK = ('chess', 'analytics', 'geron_triangle', 'files', 'sequence', 'numbers', 'fibonacci', 'happy_ticket')


def menu():
    args = arguments.parse()

    while True:
        if args.choose == 'chess':
            chess.chess(args)
        if args.choose == 'analytics':
            analytics.analytics_cycle(args)
        if args.choose == 'geron_triangle':
            geron_triangle.geron_triangle(args)
        if args.choose == 'files':
            files.check_files(args)
        if args.choose == 'sequence':
            sequence.numeric_sequence(args)
        if args.choose == 'numbers':
            numbers.digit_to_string(args)
        if args.choose == 'fibonacci':
            fibonacci.fibo_range(args)
        if args.choose == 'happy_ticket':
            happy_ticket.tickets()

        global_menu = input(f'CHOICE OF TASK: \n 1. {TASK[0]} \n 2. {TASK[1]} \n 3. {TASK[2]} \n 4. {TASK[3]} \n '
                            f'5. {TASK[4]} \n 6. {TASK[5]} \n 7. {TASK[6]} \n 8. {TASK[7]} \n '
                            f'9. Write something else to exit \n Enter the task: ').lower()

        if global_menu in TASK:
            args.choose = global_menu
            continue
        else:
            break


if __name__ == '__main__':

    menu()
