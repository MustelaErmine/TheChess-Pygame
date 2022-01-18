from chess_const import *


class Knight:
    def __init__(self, color):
        self.color = color
        self.moved = False

    def get_color(self):
        return self.color

    def char(self):
        return 'N'

    def can_move(self, board, row, col, row1, col1):
        return 0 <= row1 <= 7 and 0 <= col1 <= 7 and \
               ((abs(row1 - row) == 2 and abs(col1 - col) == 1) or 
                (abs(row1 - row) == 1 and abs(col1 - col) == 2))

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)