from chess_const import *


class King:
    def __init__(self, color):
        self.color = color
        self.moved = False

    def get_color(self):
        return self.color

    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        if row != row1 and col != col1:
            return False

        return (abs(row - row1) == 1) or (abs(col - col1) == 1)

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)