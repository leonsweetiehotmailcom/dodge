import time

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    bullet_charged = False
    bullet_fired = False
    bullet_power = 1
    bullet_charge_start = None

    def __init__(self, screen, owner):
        super(Bullet, self).__init__()
        self.screen = screen
        self.owner = owner

        self.bullet_speed = [4, 0]
        self.reset()

    def handle_event(self, event):
        if pygame.KEYDOWN == event.type:
            if pygame.K_SPACE == event.key:
                self.charge()
        elif pygame.KEYUP == event.type:
            if pygame.K_SPACE == event.key:
                self.fire()

    def reset(self):
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.bullet_charged = False
        self.bullet_fired = False
        self.bullet_power = 1
        self.bullet_charge_start = None

    def charge(self):
        if not self.bullet_charged and not self.bullet_fired:
            self.bullet_charged = True
            self.bullet_charge_start = time.time()

    def fire(self):
        if self.bullet_charged:
            self.bullet_fired = True
            self.bullet_charged = False

    def power_reduce(self, hit):
        self.bullet_power -= hit * 2
        if self.bullet_power <= 0:
            self.reset()

    def update(self):
        if self.bullet_charged:
            power_charged = int((time.time() - self.bullet_charge_start) * 5)
            if power_charged > self.bullet_power and self.bullet_power <= 10:
                if power_charged > 10:
                    power_charged = 10
                self.bullet_power = power_charged
        if self.bullet_fired:
            self.rect = self.rect.move(self.bullet_speed)
            if self.bullet_speed[0] < 0 and self.rect.left < 0:
                self.reset()
            if self.bullet_speed[0] > 0 and self.rect.right > self.screen.get_rect().width:
                self.reset()

    def blit_me(self):
        if self.bullet_charged:
            if self.owner.sprite_direct == -1:
                x = self.owner.rect.left - 5
                self.bullet_speed[0] = -4
            if self.owner.sprite_direct == 1:
                x = self.owner.rect.right + 5
                self.bullet_speed[0] = 4
            y = self.owner.rect.top + 20
            self.rect = pygame.draw.circle(self.screen, (250, 250, 250), (x, y), self.bullet_power)
        if self.bullet_fired:
            self.rect = pygame.draw.circle(self.screen, (250, 250, 250), self.rect.center, self.bullet_power)
