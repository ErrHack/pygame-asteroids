import pygame
from player import Player

from constants import *

def main():
	
	pygame.init()
	
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
	clock = pygame.time.Clock()
	dt = 0

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	player = Player(x, y)
	
	print_count = 0

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill("black")
		player.update(dt)
		player.draw(screen)
		pygame.display.flip()

		dt = clock.tick(60) / 1000

		print_count += 1
		if print_count >= 60 * 5:
			print(f"print_count: {print_count}, dt: {dt}")
			print_count = 0


if __name__ == "__main__":
	main()


