import sys
import pygame
import os

sys.path.insert(0, 'board/')
sys.path.insert(0, 'screenwork/')
sys.path.insert(0, 'constants/')

from chess import *
from splash import *
from game import *
from pygame_const import *


def main():
	pygame.init()
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()
	show_splashscreen(screen, clock)


if __name__ == '__main__':
	main()