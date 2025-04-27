import pygame as p
import constants as C

def main():
	
	p.init()
	
	print("Starting Asteroids!")
	print(f"Screen width: {C.SCREEN_WIDTH}")
	print(f"Screen height: {C.SCREEN_HEIGHT}")
	
	screen = p.display.set_mode( (C.SCREEN_WIDTH, C.SCREEN_HEIGHT) )
	
	while True:

		for event in p.event.get():
			if event.type == p.QUIT:
				return
			
		screen.fill("black")
		p.display.flip()


if __name__ == "__main__":
	main()


