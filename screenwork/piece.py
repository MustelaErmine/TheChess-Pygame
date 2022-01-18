import pygame

from pygame_const import *
from chess import *


class Piece(pygame.sprite.Sprite):
    def __init__(self, pieces_group, all_sprites, piece, board, pos_x, pos_y):
        super().__init__(pieces_group, all_sprites)
        self.piece = piece
        color = 'w' if piece.color == WHITE else 'b'
        size = cell_size - padding * 2
        self.board = board
        self.image = pygame.transform.scale(load_image(color + piece.char().lower() + '.png'),
                                            (size, size))
        self.x, self.y = pos_x, pos_y
        self.rect = self.image.get_rect().move(margin_left + pos_x * cell_size + padding, 
                                               margin_top + (7 - pos_y) * cell_size + padding)

    def update(self, *args):
        if len(args) == 1:
            pos_x, pos_y = self.x, self.y
            player = args[0]
        else:
            pos_x, pos_y, player = args
        self.x, self.y = pos_x, pos_y
        self.rect.x = margin_left + pos_x * cell_size + padding
        self.rect.y = margin_top + (7 - pos_y) * cell_size + padding

    def get_placing_cells(self):
        cells = set()
        for i in range(8):
            for j in range(8):
                move = self.piece.can_move(self.board, self.y, self.x, i, j) and \
                       self.board.get_piece(i, j) is None
                attack = self.piece.can_attack(self.board, self.y, self.x, i, j) and \
                       self.board.get_piece(i, j) is not None and \
                       self.board.get_piece(i, j).color == opponent(self.piece.color)
                if attack or move:
                    cells.add((i, j))
        return cells
