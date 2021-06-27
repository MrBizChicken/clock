from constants import *
import pygame

class Main_block(pygame.sprite.Sprite):

    """
        # TODO:

    """
    def __init__(self, x, y, size, color):
        super().__init__()
        self.width = size
        self.height = size
        self.size = size
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (x, y)


    def update(self):
        pass
