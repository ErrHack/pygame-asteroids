import pygame
from circleshape import CircleShape
from shot import Shot

from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED


class Player(CircleShape):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
    def draw(self, screen):
        try:
            line_width = 2
            pygame.draw.polygon(screen, "white", self.triangle(), line_width)
        except ValueError as v:
            print(v)
        except TypeError as t:
            print(t)
        except Exception as e:
            print(e)
    
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        print(f"ROTATION: {self.rotation}")


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]: self.rotate(-dt) # rotate left
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: self.rotate(dt)  # rotate right
        if keys[pygame.K_w] or keys[pygame.K_UP]: self.move(dt) # move forward
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: self.move(-dt) # move backward
        if keys[pygame.K_SPACE]: self.shoot() # shoot

        self.timer -= dt
    

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        print(f"self.position: {self.position}")

    
    def shoot(self):
        if self.timer > 0:
            print("timer > 0 is True")
        else:    
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN