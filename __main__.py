import pygame, time,help
from pygame import draw, event, display,key
screen=display.set_mode([900,700])
player=pygame.image.load("picture/player.jpg")
player=help.izmeni_kartinku(player,50,150,[235,28,36],100)
obekt=pygame.Rect([400,550,50,150])







def obrabotka_event():
    e = event.get()
    for r in e:
        if r.type == pygame.QUIT:
            exit()


def draw_screen():
    screen.fill([123, 0, 255])
    draw_player()
    display.flip()

def draw_player():
    #draw.rect(screen,[123,111,111],obekt,1)

    screen.blit(player,obekt)
def go_player():
    keys = key.get_pressed()
    if keys[pygame.K_a]:
        obekt.x+=-3
    if keys[pygame.K_d]:
        obekt.x+=3




while 1 == 1:
    time.sleep(1/120)
    obrabotka_event()
    draw_screen()
    go_player()

