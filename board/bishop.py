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
        return True  # Заглушка

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)