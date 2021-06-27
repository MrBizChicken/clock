from constants import *
from main_block import *
import pygame, main_block, random

class Ball(main_block.Main_block):

    def __init__(self, size, speed, color):
        x = random.randint(0, GAME_WIDTH - size)
        y = random.randint(0, GAME_HEIGHT - size)
        super().__init__(x, y, size, color)

        min = int(speed * 0.8)
        max = int(speed * 1.2)
        self.x_speed = random.randint(min, max)
        self.y_speed = random.randint(min, max)
        # print("****", size, self.x_speed, self.y_speed)


    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.x < 0:
            self.x_speed = -self.x_speed

        if self.rect.y < 0:
            self.y_speed = -self.y_speed

        if self.rect.right > GAME_WIDTH:
            self.x_speed = -self.x_speed

        if self.rect.bottom > GAME_HEIGHT:
            self.y_speed = -self.y_speed
