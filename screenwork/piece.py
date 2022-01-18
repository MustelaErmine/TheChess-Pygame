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
											   margin_top + pos_y * cell_size + padding)

	def update(self, *args):
		pos_x, pos_y, player = args
		self.x, self.y = pos_x, pos_y
		self.rect.x = margin_left + pos_x * cell_size + padding
		self.rect.y = margin_top + pos_y * cell_size + padding

	def get_placing_cells(self):
		cells = []
		for i in range(8):
			for j in range(8):
				if self.piece.can_move(self.board, self.pos_x, self.pos_y, i, j):
					cells.append((i, j))
