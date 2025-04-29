import pygame
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField

from constants import *

def main():
	
	pygame.init()
	
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	player = Player(x, y)
	asteroid_field = AsteroidField()	
	
	print_count = 0
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill("black")
		updatable.update(dt)
		for d in drawable:
			d.draw(screen)
		for a in asteroids:
			if player.is_collision(a):
				print("Game over!")
				return
		pygame.display.flip()

		dt = clock.tick(60) / 1000

		print_count += 1
		if print_count >= 60 * 5:
			print(f"print_count: {print_count}, dt: {dt}")
			print_count = 0


if __name__ == "__main__":
	main()


