import pygame
from circleshape import CircleShape
from constants import PLAYER_SPEED


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        try:
            line_width = 2
            pygame.draw.circle(
                screen,
                "white",
                self.position,
                 self.radius,
                 line_width
            )
        except TypeError as t:
            print(t)
        except Exception as e:
            print(e)

    def update(self, dt):
        self.position += self.velocity * dt
        print(f"asteroid position: {self.position}")