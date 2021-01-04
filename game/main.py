import pygame

# initialization

WIDTH = 1000
HEIGHT = 500
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()
screen.fill(pygame.Color(0, 50, 0))

# game loop

while True:
	for j in pygame.event.get():
		if j.type == pygame.QUIT:
			exit()

	pygame.display.flip()
	clock.tick(FPS)
