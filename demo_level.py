import pygame
from demo_tiles import *


class Level(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        # groups
        self.walls = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.messages = pygame.sprite.Group()
        self.player = player
        self.chest = Chest("images/chest.gif", (0, 0))
        self.lighting = Lightning("images/lighting.gif", (0, 0))
        self.walls.add(self.chest)
        self.start_pos = (0, 0)
        self.end_pos = (0, 0)
        self.exit = None
        self.start = None