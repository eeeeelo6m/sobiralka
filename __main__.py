import pygame, time
from pygame import draw, event, display
screen=display.set_mode([500,700])


def obrabotka_event():
    e = event.get()
    for r in e:
        if r.type == pygame.QUIT:
            exit()


def draw_screen():
    screen.fill([123, 0, 255])
    display.flip()


def draw_player():



while 1 == 1:
    obrabotka_event()
    draw_screen()
