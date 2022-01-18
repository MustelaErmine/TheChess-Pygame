class Bishop:
    '''Класс слона. Пока что заглушка, которая может ходить в любую клетку.'''

    def __init__(self, color):
        self.color = color
        self.moved = False

    def get_color(self):
        return self.color

    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        return 0 <= row1 <= 7 and 0 <= col1 <= 7 and abs(row1 - row) == abs(col1 - col)

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)