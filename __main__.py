from pygame import draw, event, display, key
import pygame, time, help
pygame.init()
TIMER_ID = event.custom_type()
screen = display.set_mode([900, 700])
player = pygame.image.load("picture/player.jpg")
player = help.izmeni_kartinku(player, 50, 150, [235, 28, 36], 100)
obekt = pygame.Rect([400, 550, 50, 150])
vistrel_rect = []
mogu_strelyt = True


def draw_vistrel():
    for vistrel_rect1 in vistrel_rect:
        draw.rect(screen, [111, 222, 121, ], vistrel_rect1)


def ogranichnie():
    if obekt.x < 0:
        obekt.x = 1
    if obekt.right > 900:
        obekt.right = 900


def obrabotka_event():
    global mogu_strelyt
    e = event.get()
    for r in e:
        if r.type == pygame.QUIT:
            exit()
        if r.type == pygame.KEYDOWN and r.key == pygame.K_SPACE:
            vistrel()
        if r.type==TIMER_ID:
            mogu_strelyt=True

    keys = key.get_pressed()
    # движение игрока
    if keys[pygame.K_a]:
        obekt.x += -3
    if keys[pygame.K_d]:
        obekt.x += 3


def draw_screen():
    screen.fill([123, 0, 255])
    draw_player()
    draw_vistrel()
    display.flip()


def draw_player():
    # draw.rect(screen,[123,111,111],obekt,1)
    screen.blit(player, obekt)


def attack_vistrel():
    speedy = -5
    for bad in vistrel_rect:
        bad.y += speedy


def vistrel():
    global vistrel_rect, mogu_strelyt

    if mogu_strelyt == True:

        a = pygame.Rect([obekt.x + 20, obekt.top - 100, 10, 100])
        vistrel_rect.append(a)
        mogu_strelyt = False
        pygame.time.set_timer(TIMER_ID,200,1)
    else:
        print("стрелять нельзя")


while 1 == 1:
    time.sleep(1 / 120)
    obrabotka_event()
    attack_vistrel()
    ogranichnie()
    draw_screen()
