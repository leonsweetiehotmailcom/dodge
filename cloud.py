import random

import pygame
from pygame.sprite import Sprite


class Cloud(Sprite):
    def __init__(self, screen):
        super(Cloud, self).__init__()
        self.screen = screen

        self.velocity = 1
        self.speed = [-1, 0]
        if random.randint(0, 1) == 0:
            self.sprite = pygame.image.load("images/cloud_medium.png")
        else:
            self.sprite = pygame.image.load("images/cloud_big.png")
        self.rect = self.sprite.get_rect()
        self.rect.left = screen.get_rect().right - 50
        self.rect.bottom = random.randint(screen.get_rect().top + 50, screen.get_rect().bottom - 50)

    def handle_event(self, event):
        return

    def update(self):
        self.rect = self.rect.move(self.speed)

    def blit_me(self):
        self.screen.blit(self.sprite, self.rect)
