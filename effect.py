# ================================== #
#                                    #
#  Простейший эффект перелива цвета  #
#                                    #
# ================================== #

import pygame

# initialization

WIDTH = 1000
HEIGHT = 800
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Effect")
clock = pygame.time.Clock()

red = 0
green = 0
blue = 0

delete = False


# game loop

while True:
	if red == 255:
		delete = True
	elif red == 0:
		delete = False

	if delete:
		red -= 1
		green -= 1
		blue -= 1
	else:
		red += 1
		green += 1
		blue += 1

	screen.fill(pygame.Color(red, green, blue))

	for j in pygame.event.get():
		if j.type == pygame.QUIT:
			exit()

	pygame.display.flip()
	clock.tick(FPS)
