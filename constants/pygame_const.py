import os
import pygame
import sys

width = 900
height = 900
size = (width, height)

black, white, blue, red = '#121212', '#F5F5F5', '#30475E', '#F05454'

fps = 30

cell_size = 86
margin_top = 10
#margin_left = (width - 8 * cell_size) // 2
margin_left = 10
padding = 3


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image