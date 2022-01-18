class Knight:
    def __init__(self, color):
        self.color = color
        self.moved = False

    def get_color(self):
        return self.color

    def char(self):
        return 'N'

    def can_move(self, board, row, col, row1, col1):
        return 0 <= row <= 7 and 0 <= col <= 7 and \
               ((abs(row - self.row) == 2 and abs(col - self.col) == 1) or 
                (abs(row - self.row) == 1 and abs(col - self.col) == 2))

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)