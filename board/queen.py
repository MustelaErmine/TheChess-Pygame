class Queen:
    def __init__(self, color):
        self.color = color
        self.moved = False

    def char(self):
        return 'Q'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        can1 = correct_coords(row1, col1) and (abs(row1 - row) == abs(col1 - col) or
                                               row == row1 or col == col1) and \
               not (row == row1 and col1 == col)
        if not can1:
            return False
        can2 = 0
        caneat = 0
        sgn1 = 1 if row1 > row else -1 if row1 < row else 0
        sgn2 = 1 if col1 > col else -1 if col1 < col else 0
        row2 = row
        col2 = col
        while not (row2 == row1 and col2 == col1):
            row2 += sgn1
            col2 += sgn2
            can2 += 1 if board.field[row2][col2] is not None else 0
            if board.field[row2][col2] is not None:
                if board.field[row2][col2].get_color() != self.color and \
                        row2 == row1 and col2 == col1:
                    caneat += 1

        return can2 == 0 or caneat == 1 and can2 == 1

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)