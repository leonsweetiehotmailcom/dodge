import pygame
from pygame.sprite import Sprite


class Ghost(Sprite):
    def __init__(self, screen, target):
        super(Ghost, self).__init__()
        self.screen = screen
        self.target = target

        self.velocity = 2
        self.speed = [0, 0]
        self.sprite = pygame.image.load("images/ghost.png")
        self.rect = self.sprite.get_rect()
        self.rect.left = screen.get_rect().right - 20
        self.rect.bottom = screen.get_rect().top + 20
        self.radius = 10

    def handle_event(self, event):
        return

    def update(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > self.screen.get_rect().width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.screen.get_rect().height:
            self.speed[1] = -self.speed[1]

        if self.rect.centerx - self.target.rect.centerx > 0:
            self.speed[0] = -self.velocity
        else:
            self.speed[0] = self.velocity

        if self.rect.centery - self.target.rect.centery > 0:
            self.speed[1] = -self.velocity
        else:
            self.speed[1] = self.velocity

    def blit_me(self):
        self.screen.blit(self.sprite, self.rect)
