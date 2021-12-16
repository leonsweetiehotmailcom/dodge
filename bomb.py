import time
import random
import pygame
from pygame.sprite import Sprite


class Bomb(Sprite):
    bullet_charged = False
    bullet_fired = False
    bullet_power = 1
    bullet_charge_start = None

    def __init__(self, screen, owner):
        super(Bomb, self).__init__()
        self.screen = screen
        self.owner = owner
        self.bullet_speed = [4, 0]
        self.reset()

    def handle_event(self, event):
        if pygame.KEYDOWN == event.type:
            if pygame.K_a == event.key:
                self.wait()

        elif pygame.KEYUP == event.type:
            if pygame.K_a == event.key:
                self.launch(3)

    def reset(self):
        self.rect = pygame.Rect(0, 0, 5, 5)

    def wait(self):
        print("LAUNCH BOMB")
    def launch(self, bombs_left):
        if bombs_left >= 1:
            self.bomb_launched = True
            self.rect = pygame.draw.circle(self.screen, (250, 0, 0), self.rect.center, 5)



