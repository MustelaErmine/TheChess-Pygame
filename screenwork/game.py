import sys
import pygame

from chess import *
from pygame_const import *
from piece import * 


font = None
all_sprite = None
pieces_group = None

player = None

selected = None
selected_cells = set()


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
    for i in range(8):
        for j in range(8):
            x = margin_left + i * cell_size
            y = margin_top + j * cell_size
            color = red if (i + j) % 2 == 0 else black
            pygame.draw.rect(screen, color, (x + padding, y + padding, cell_size - padding * 2,
                                             cell_size - padding * 2))


def draw_selected(screen):
    for cell in selected_cells:
        cell = convert_cell(*cell, player)
        x = margin_left + cell[1] * cell_size
        y = margin_top + cell[0] * cell_size
        pygame.draw.rect(screen, blue, (x + padding // 2, y + padding // 2, 
                                        cell_size - padding, cell_size - padding), padding)
        #pygame.draw.rect(screen, blue, (x, y, cell_size, cell_size), padding)


def update(screen):
    pygame.draw.rect(screen, white, (0, 0, width, height))
    draw_cells(screen)
    draw_selected(screen)
    all_sprite.draw(screen)
    pygame.display.flip()


def game(screen, clock):
    global all_sprite, pieces_group, player, selected_cells, selected

    pieces_group = pygame.sprite.Group()
    all_sprite = pygame.sprite.Group()

    player = WHITE

    board = Board()

    pieces = []
    for i in range(8):
        pieces.append([])
        for j in range(8):
            if board.get_piece(i, j) is not None:
                pieces[-1].append(Piece(pieces_group, all_sprite, 
                                        board.get_piece(i, j), board, j, i))
            else:
                pieces[-1].append(None)

    pieces_group.update(player)
    update(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell = get_clicked_cell(*event.pos)
                if cell:
                    print(cell)
                    if selected:
                        selected = None
                        selected_cells = set()
                        print('move')
                    else:
                        piece = pieces[cell[0]][cell[1]]
                        selected = cell
                        if piece:
                            selected_cells = piece
                            selected_cells = piece.get_placing_cells()
                            print(selected_cells)
                else:
                    selected = None
                    selected_cells = set()
                update(screen)
        clock.tick(fps)

    main_menu()


def get_clicked_cell(x, y):
    x -= margin_left
    y -= margin_top
    if 0 <= y <= cell_size * 8 and 0 <= x <= cell_size * 8:
        i, j = y // cell_size, x // cell_size
        return convert_cell(i, j, player)
    else:
        return False


def make_move(row, col, row1, col1):
    pass