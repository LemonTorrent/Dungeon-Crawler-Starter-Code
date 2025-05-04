import pygame, random
from tiles import Tile

class Player(pygame.sprite.Sprite):
    def __init__(self, path, pos, facing_r):
        super().__init__()
        self.path = path
        self.facing_r = facing_r
        self.image = pygame.image.load(self.path)
        if not self.facing_r:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.movement = [0, 0]
        self.level = None
        self.inventory = {}
        self.health = 100
        self.attack_damage = 5
        self.defense = 1
        self.facing = 'R'
        self.alive = True

