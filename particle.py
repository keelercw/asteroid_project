import pygame
import random

class Particle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        angle = random.uniform(0, 360)
        self.velocity.rotate(angle)

    def update (dt):
        self.position += self.velocity * dt
        self.size -= 2
        if self.size == 0:
            self.kill()

    def explode(self):
                    particle1 = Particle(self.position.x, self.position.y)
                    particle2 = Particle(self.position.x, self.position.y)
                    particle3 = Particle(self.position.x, self.position.y)
                    particle4 = Particle(self.position.x, self.position.y)
        