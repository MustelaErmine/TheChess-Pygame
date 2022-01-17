class Knight:
    def __init__(self, color):
        self.color = color
        self.moved = False

    def get_color(self):
        return self.color

    def char(self):
        return 'N'

    def can_move(self, board, row, col, row1, col1):
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)