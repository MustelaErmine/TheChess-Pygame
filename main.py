import sys
import pygame
import os

sys.path.insert(0, 'screenwork/')
sys.path.insert(0, 'constants/')
sys.path.insert(0, 'board/')

from splash import *
from game import *
from pygame_const import *


def main():
	pygame.init()
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()
	show_splashscreen(screen, clock)
	main_menu(screen, clock)


if __name__ == '__main__':
	main()