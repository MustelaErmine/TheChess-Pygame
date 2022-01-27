import sys
import pygame

from chess import *
from pygame_const import *
from piece import * 


font50 = None
font_player = None
font_howto = None
all_sprite = None
pieces_group = None

player = None

selected = None
selected_cells = set()


def terminate():
    pygame.quit()
    sys.exit(0)


def main_menu(screen, clock):
    global font50, font_player, font_howto
    font50 = pygame.font.Font('OpenSans-Semibold.ttf', 50)
    font_player = pygame.font.Font('OpenSans-Semibold.ttf', 30)
    font_howto = pygame.font.Font('OpenSans-Semibold.ttf', 20)
    pygame.draw.rect(screen, white, (0, 0, width, height))

    text_rendered = font50.render('Чтобы начать новую игру,', 1, black)
    text_rect = text_rendered.get_rect()

    text_rect.x = width // 2 - text_rect.width // 2
    text_rect.y = height // 2 - 75

    screen.blit(text_rendered, text_rect)

    text_rendered = font50.render('нажмите Enter', 1, black)
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
        if player == WHITE:
            x = margin_left + cell[1] * cell_size
            y = margin_top + (7 - cell[0]) * cell_size
        else:
            x = margin_left + (7 - cell[1]) * cell_size
            y = margin_top + cell[0] * cell_size
        pygame.draw.rect(screen, blue, (x + padding // 2, y + padding // 2, 
                                        cell_size - padding, cell_size - padding), padding)
        #pygame.draw.rect(screen, blue, (x, y, cell_size, cell_size), padding)


def draw_player_text(screen, text):
    text_rendered = font_player.render(text, 1, black)
    text_rect = text_rendered.get_rect()

    text_rect.x = player_text_center - text_rect.width // 2
    text_rect.y = player_text_top

    screen.blit(text_rendered, text_rect)


def update(screen):
    pygame.draw.rect(screen, white, (0, 0, width, height))
    pieces_group.update(player)
    draw_cells(screen)
    draw_selected(screen)
    draw_player_text(screen, 'Ходят ' + ('белые' if player == WHITE else 'черные'))
    draw_howto_text(screen)
    all_sprite.draw(screen)
    pygame.display.flip()


def draw_howto_text(screen):
    for i, line in enumerate(howto_text.split('\n')):
        text_rendered = font_howto.render(line, 1, black)
        text_rect = text_rendered.get_rect()

        text_rect.x = howto_left
        text_rect.y = howto_top + howto_padding * i

        screen.blit(text_rendered, text_rect)



def game(screen, clock):
    global all_sprite, pieces_group, player, selected_cells, selected, white_king, black_king, tclock

    tclock = clock

    pieces_group = pygame.sprite.Group()
    all_sprite = pygame.sprite.Group()

    player = WHITE

    board = Board()

    white_king = None
    black_king = None

    pieces = []
    for i in range(8):
        pieces.append([])
        for j in range(8):
            if board.get_piece(i, j) is not None:
                pieces[-1].append(Piece(pieces_group, all_sprite, 
                                        board.get_piece(i, j), board, j, i))
                if type(board.get_piece(i, j)) is King:
                    if board.get_piece(i, j).get_color() == WHITE:
                        white_king = (i, j)
                    else:
                        black_king = (i, j)
            else:
                pieces[-1].append(None)

    #print(white_king, black_king)

    update(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell = get_clicked_cell(*event.pos)
                if cell:
                    #print(cell)
                    if selected:
                        make_move(*selected, *cell, pieces, board, screen)
                        selected = None
                        selected_cells = set()
                    else:
                        piece = pieces[cell[0]][cell[1]]
                        if piece and piece.piece.color == player:
                            selected = cell
                            selected_cells = piece
                            selected_cells = piece.get_placing_cells()
                            #print(selected_cells)
                        else:
                            selected = None
                            selected_cells = set()
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
        if player == WHITE:
            return 7 - i, j
        return i, 7 - j
    else:
        return False


def make_move(row, col, row1, col1, pieces, board, screen):
    global player, white_king, black_king
    #print('move', row, col, row1, col1)
    piece2 = pieces[row1][col1]
    move = board.move_piece(row, col, row1, col1)
    #print(move)
    if move:
        piece = pieces[row][col]
        pieces[row1][col1] = piece
        pieces[row][col] = None
        player = opponent(player)
        piece.update(col1, row1, player)
        if piece2 is not None:
            piece2.kill()
        if (row, col) == white_king:
            white_king = (row1, col1)
        if (row, col) == black_king:
            black_king = (row1, col1)
        #print_board(board)
        #print(white_king, black_king)
        if board.get_piece(*white_king).checkmate(board, *white_king):
            won(screen, BLACK)
        if board.get_piece(*black_king).checkmate(board, *black_king):
            won(screen, WHITE)

def won(screen, color):
    global selected_cells
    print('won', color)
    selected_cells = []
    pygame.draw.rect(screen, white, (0, 0, width, height))
    pieces_group.update(player)
    draw_cells(screen)
    draw_selected(screen)
    draw_player_text(screen, 'Выиграли ' + ('белые' if color == WHITE else 'черные') + ', нажмите Enter')
    draw_howto_text(screen)
    all_sprite.draw(screen)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    running = False
        tclock.tick(fps)
    main_menu(screen, tclock)