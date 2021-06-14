import pygame
from random import randint
Black = (0, 0, 0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(Black)
        self.image.set_colorkey(Black)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self, direction):
        if direction == 1:
            self.velocity[0] = -self.velocity[0] - 1
            self.velocity[1] = randint(-8, 8)
        if direction == -1:
            self.velocity[0] = -self.velocity[0] + 1
            self.velocity[1] = randint(-8, 8)

    def reset(self):
        self.rect.x = 700/2
        self.rect.y = 500/2

    def launchBall(self, direction):
        if direction == -1:
            self.velocity = [randint(-4, -1), randint(-4, 4)]
        else:
            self.velocity = [randint(1, 4), randint(-4, 4)]
