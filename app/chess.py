from app.ask import ask


def chess(args):
    def board(height, width):
        Chess_board = [(' ', '*'), ('*', ' ')]
        for _ in range(int(height)):
            print(*Chess_board[1] * int(width))
            print(*Chess_board[0] * int(width))

    def _check_args():
        if args.width is not None and args.height is not None and args.width.isdigit() and args.height.isdigit() and \
                int(args.width) % 2 != 1 and int(args.height) % 2 != 1 and args.width != 'default' and args.height != 'default':
            return True
        else:
            return False

    while True:
        if _check_args():
            board(str(int(int(args.height) / 2)), str(int(int(args.width) / 2)))
            args.height = 'default'
        else:
            args.width = input('Enter a numeric value of the width of the chessboard: ')
            args.height = input('Enter a numeric value of the height of the chessboard: ')
            if _check_args():
                board(str(int(int(args.height) / 2)), str(int(int(args.width) / 2)))
                args.height = 'default'
            else:
                print('Enter the correct parameters. Width and height should be even positive number')
                continue

        if ask():
            continue
        else:
            break
