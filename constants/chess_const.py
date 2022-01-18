WHITE = 1
BLACK = 2


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


def convert_cell(x, y, player):
    if player == WHITE:
        return x, 7 - y
    return x, y