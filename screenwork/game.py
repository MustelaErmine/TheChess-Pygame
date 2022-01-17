import sys
import pygame

from chess import *
from pygame_const import *
from piece import * 


font = None
all_sprite = None
pieces_group = None


def terminate():
    pygame.quit()
    sys.exit(0)


def main_menu(screen, clock):
    font = pygame.font.Font('OpenSans-Semibold.ttf', 50)
    pygame.draw.rect(screen, white, (0, 0, width, height))

    text_rendered = font.render('Чтобы начать новую игру,', 1, black)
    text_rect = text_rendered.get_rect()

    text_rect.x = width // 2 - text_rect.width // 2
    text_rect.y = height // 2 - 75

    screen.blit(text_rendered, text_rect)

    text_rendered = font.render('нажмите Enter', 1, black)
    text_rect = text_rendered.get_rect()

    text_rect.x = width // 2 - text_rect.width // 2
    text_rect.y = height // 2

    screen.blit(text_rendered, text_rect)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    running = False
        clock.tick(fps)

    game(screen, clock)


def draw_cells(screen):
    margin_top = 10
    margin_left = (width - 8 * cell_size) // 2

    padding = 3

    for i in range(8):
        for j in range(8):
            x = margin_left + i * cell_size
            y = margin_top + j * cell_size
            color = red if (i + j) % 2 == 0 else black
            pygame.draw.rect(screen, color, (x + padding, y + padding, cell_size - padding * 2,
                                             cell_size - padding * 2))


def update(screen):
	pygame.draw.rect(screen, white, (0, 0, width, height))
	draw_cells(screen)
	all_sprite.draw(screen)
	pygame.display.flip()


def game(screen, clock):
    global all_sprite, pieces_group

    pieces_group = pygame.sprite.Group()
    all_sprite = pygame.sprite.Group()

    p = Piece(Pawn(WHITE), pieces_group, all_sprite, 0, 0)

    update(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        clock.tick(fps)

    main_menu()