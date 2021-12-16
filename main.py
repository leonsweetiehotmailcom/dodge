import sys
import time
import random

import pygame
from pygame.sprite import Group

from ghost import Ghost
from hero import Hero
from cloud import Cloud

size = black = screen = None
hero = ghost = ghosts = clouds = start = active = None


def init():
    global size
    global black
    global screen
    size = width, height = 960, 680
    black = 3, 207, 252
    screen = pygame.display.set_mode(size)


def reset():
    global hero
    global ghost
    global ghosts
    global clouds
    global start
    global active
    hero = Hero(screen)
    ghost = Ghost(screen, hero)
    ghosts = Group()
    ghosts.add(ghost)
    clouds = Group()
    start = time.time()
    active = True


pygame.init()
init()
reset()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if pygame.KEYDOWN == event.type:
            if pygame.K_RETURN == event.key:
                reset()

        hero.handle_event(event)

    if active:
        hero.update()
        ghosts.update()
        clouds.update()
        for g in ghosts.sprites():
            if pygame.sprite.collide_circle(hero, g):
                active = False

        crashed = pygame.sprite.spritecollide(hero.bullet, ghosts, True)
        if crashed:
            hero.bullet.power_reduce(len(crashed))

        screen.fill(black)
        hero.blit_me()
        for g in ghosts.sprites():
            g.blit_me()
        for c in clouds.sprites():
            c.blit_me()
        for c in clouds.copy():
            if c.rect.right < 0:
                clouds.remove(c)

        if random.randint(0, 99) > 97:
            clouds.add(Cloud(screen))

        # render the status message
        end = time.time()
        game_time = end - start
        if game_time > len(ghosts.sprites()) * 10:
            g_tmp = Ghost(screen, hero)
            ghosts.add(g_tmp)

        message = 'Survived:  ' + format(end - start, '.2f')
        font = pygame.font.Font(None, 24)
        text = font.render(message, True, (100, 100, 100))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        time.sleep(0.01)
