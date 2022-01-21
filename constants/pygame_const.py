import os
import pygame
import sys

width = 1100
height = 780
size = (width, height)

black, white, blue, red = '#121212', '#F5F5F5', '#30475E', '#F05454'

fps = 30

cell_size = 86
margin_top = 10
#margin_left = (width - 8 * cell_size) // 2
margin_left = 10
padding = 3

player_text_top = margin_top + 8 * cell_size + 20
player_text_center = margin_left + cell_size * 4

howto_top = margin_top
howto_left = margin_left + 8 * cell_size + 20
howto_padding = 30

howto_text = '''Как играть:
1. Если сейчас ваш ход, 
   доска будет повернута к вам
2. Щелкните на нужную фигуру,
   и вам будут показаны возможные
   ходы синим цветом
3. После этого нажмите на одну из
   подходящих клеток, и фигура
   туда передвинется
4. Ход перейдет к сопернику
   автоматически'''


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image