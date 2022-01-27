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
        if row == row1 and col == col1:
            return False

        return (abs(row - row1) <= 1) and (abs(col - col1) <= 1) and \
               not board.attacked(row1, col1, opponent(self.color)) and \
               board.get_piece(row1, col1) is None

    def can_attack(self, board, row, col, row1, col1):
        if row == row1 and col == col1:
            return False

        return (abs(row - row1) <= 1) and (abs(col - col1) <= 1) and \
               not board.attacked(row1, col1, opponent(self.color)) and \
               (board.get_piece(row1, col1) is None or 
                board.get_piece(row1, col1).get_color() == opponent(self.color))

    def checkmate(self, board, row, col):
        flag = True
        for i in range(8):
            for j in range(8):
                if self.can_move(board, row, col, i, j):
                    #print('can_move', i, j)
                    flag = False
        if not board.attacked(row, col, opponent(self.color)):
            flag = False
        return flag

    def king_stalemate(self, board, row, col):
        flag = False
        for i in range(8):
            for j in range(8):
                if self.can_move(board, row, col, i, j):
                    flag = True
        return flag and not board.attacked(row, col, opponent(self.color))