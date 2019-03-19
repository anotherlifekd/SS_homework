class ChessBoard():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def board(self):
        Chess_board = [(' ', '*'), ('*', ' ')]
        for _ in range(int(self.height)):
            print(*Chess_board[1] * int(self.width))
            print(*Chess_board[0] * int(self.width))