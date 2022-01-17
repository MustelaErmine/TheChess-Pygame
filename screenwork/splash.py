import sys
import pygame

sys.path.insert(0, '../constants/')

from pygame_const import *


def show_splashscreen(screen, clock):
	splash = load_image('splash.png')
	screen.blit(splash, (0, 0))
	for _ in range(fps * 1):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
		pygame.display.flip()
		clock.tick(fps)