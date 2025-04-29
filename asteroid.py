import pygame
import random
from circleshape import CircleShape

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        try:
            line_width = 2
            pygame.draw.circle(
                screen,
                "blue",
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
        # print(f"asteroid position: {self.position}")
    
    def split(self):
        old_radius = self.radius
        position = self.position
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        split_vector_1 = self.velocity.rotate(split_angle)
        split_vector_2 = self.velocity.rotate(-split_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(position.x, position.y, new_radius)
        asteroid_2 = Asteroid(position.x, position.y, new_radius)
        asteroid_1.velocity = split_vector_1 * 1.2
        asteroid_2.velocity = split_vector_2 * 1.2