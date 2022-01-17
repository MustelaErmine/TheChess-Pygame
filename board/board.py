class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        '''Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела.'''
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def move_piece(self, row, col, row1, col1):
        '''Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False'''

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.moved = True
        self.color = opponent(self.color)
        return True

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        if self.get_piece(row, col) is None or \
                self.get_piece(row, col).char() != 'P':
            return False
        p = self.get_piece(row, col)
        if p.get_color() == WHITE and row == 6 or \
                p.get_color() == BLACK and row == 1:
            if self.move_piece(row, col, row1, col1):
                d = None
                c = p.get_color()
                if char == 'Q':
                    d = Queen(c)
                elif char == 'B':
                    d = Bishop(c)
                elif char == 'N':
                    d = Knight(c)
                elif char == 'R':
                    d = Rook(c)
                self.field[row1][col1] = d
                return True
        return False

    def castling0(self):
        row = 0
        if self.color == BLACK:
            row = 7
        king = self.get_piece(row, 4)
        rook = self.get_piece(row, 0)
        if king is None or rook is None:
            return False
        elif king.char() != 'K' or rook.char() != 'R':
            return False
        elif king.moved or rook.moved:
            return False
        else:
            n = self.get_piece(row, 1) is not None
            n = n or self.get_piece(row, 2) is not None
            n = n or self.get_piece(row, 3) is not None
            if n:
                return False
        self.field[row][2] = king
        self.field[row][3] = rook
        self.field[row][0] = None
        self.field[row][4] = None
        self.color = opponent(self.color)
        return True

    def castling7(self):
        row = 0
        if self.color == BLACK:
            row = 7
        king = self.get_piece(row, 4)
        rook = self.get_piece(row, 7)
        if king is None or rook is None:
            return False
        elif king.char() != 'K' or rook.char() != 'R':
            return False
        elif king.moved or rook.moved:
            return False
        elif self.get_piece(row, 6) is not None or self.get_piece(row, 5) is not None:
            return False
        self.field[row][6] = king
        self.field[row][5] = rook
        self.field[row][7] = None
        self.field[row][4] = None
        self.color = opponent(self.color)
        return True
