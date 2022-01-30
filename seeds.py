import pygame


class Seed:
    def __init__(self):
        self.count = 0
        self.image = pygame.image.load(r'img/seed.png')
        self.pos = (750, 0)

