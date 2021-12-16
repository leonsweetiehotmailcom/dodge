import pygame
from pygame.sprite import Sprite

from bullet import Bullet


class Hero(Sprite):
    def __init__(self, screen):
        super(Hero, self).__init__()
        self.screen = screen

        self.velocity = 4
        self.speed = [0, 0]
        self.sprite_direct = 1
        self.sprite = pygame.image.load("images/hero_right.png")
        self.rect = self.sprite.get_rect()
        self.rect.left = screen.get_rect().left + 20
        self.rect.bottom = screen.get_rect().bottom - 20
        self.radius = 10

        self.bullet = Bullet(screen, self)

    def handle_event(self, event):
        if pygame.KEYDOWN == event.type:
            if pygame.K_LEFT == event.key:
                self.sprite_direct = -1
                self.speed[0] = self.velocity * self.sprite_direct
                self.sprite = pygame.image.load("images/hero_left.png")
            elif pygame.K_RIGHT == event.key:
                self.sprite_direct = 1
                self.speed[0] = self.velocity * self.sprite_direct
                self.sprite = pygame.image.load("images/hero_right.png")
            elif pygame.K_UP == event.key:
                self.speed[1] = -self.velocity
            elif pygame.K_DOWN == event.key:
                self.speed[1] = self.velocity
        elif pygame.KEYUP == event.type:
            if pygame.K_LEFT == event.key:
                self.speed[0] = 0
            elif pygame.K_RIGHT == event.key:
                self.speed[0] = 0
            elif pygame.K_UP == event.key:
                self.speed[1] = 0
            elif pygame.K_DOWN == event.key:
                self.speed[1] = 0
        self.bullet.handle_event(event)

    def update(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > self.screen.get_rect().width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.screen.get_rect().height:
            self.speed[1] = -self.speed[1]
        self.bullet.update()

    def blit_me(self):
        self.screen.blit(self.sprite, self.rect)
        self.bullet.blit_me()
