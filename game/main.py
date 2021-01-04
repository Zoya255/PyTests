from random import randint
import pygame
from cars import Car


# initialization

WIDTH = 1500
HEIGHT = 800
FPS = 60
STEP = 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()
screen.fill(pygame.Color(0, 50, 0))

print()

data = [[randint(0, 1) for i in range(int(WIDTH / STEP))] for j in range(int(HEIGHT / STEP))]

for row in data:
	for item in row:
		print(item, end=" ")
	print()

# functions

def draw(color, x, y):
	pygame.draw.rect(screen, color, ((x * STEP, y * STEP), (STEP, STEP)))


# cars

audi = Car("Ауди", car_fuel=100)


# game loop

while True:

	# keys

	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()
		elif i.type == pygame.KEYDOWN:
			if i.key == pygame.K_UP:
				audi.move_up(1)
			elif i.key == pygame.K_RIGHT:
				audi.move_right(1)
			elif i.key == pygame.K_DOWN:
				audi.move_down(1)
			elif i.key == pygame.K_LEFT:
				audi.move_left(1)

	# clear screen

	screen.fill(pygame.Color(0, 50, 0))

	# draw grid

	for i in range(int(WIDTH / STEP)):
		pygame.draw.rect(screen, "#666666", ((i * STEP, 0), (1, HEIGHT)))

	for i in range(int(HEIGHT / STEP)):
		pygame.draw.rect(screen, "#666666", ((0, i * STEP), (WIDTH, 1)))

	# update cars

	draw(audi.get_color(), audi.get_x(), audi.get_y())

	# update frame

	pygame.display.flip()
	clock.tick(FPS)
