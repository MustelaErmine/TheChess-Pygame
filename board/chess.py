from queen import *
from king import *
from knight import *
from rook import *
from pawn import *
from bishop import *
from board import *

WHITE = 1
BLACK = 2


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8