from pygame import draw, event, display, key
import pygame, time, help, random

pygame.init()
TIMER_VISTREL = event.custom_type()
TIMER_FALL_BLOCK = event.custom_type()
TIMER_FALL_BOMB = event.custom_type()
screen = display.set_mode([900, 700])
obrabotca_block = pygame.image.load("picture/супер гер бой.jpg")
obrabotca_block = help.izmeni_kartinku(obrabotca_block, 70, 70, [0, 0, 0], 10)
obrabotca_vistrel = pygame.image.load("picture/vistrel.png")
obrabotca_vistrel = help.izmeni_kartinku(obrabotca_vistrel, 40, 110, [0, 0, 0], 10)
player = pygame.image.load("picture/player.jpg")
player = help.izmeni_kartinku(player, 50, 150, [235, 28, 36], 100)
obrabotka_bomb = pygame.image.load("picture/bomb.jpg")
obrabotka_bomb = help.izmeni_kartinku(obrabotka_bomb, 60, 60, [235, 28, 36], 15)
pygame.time.set_timer(TIMER_FALL_BLOCK, 2000, 1)
pygame.time.set_timer(TIMER_FALL_BOMB,5000,1)
bombs=[]
block = []
obekt = pygame.Rect([400, 550, 50, 150])
vistrel_rect = []
mogu_strelyt = True


def draw_vistrel():
    for vistrel_rect1 in vistrel_rect:
        # draw.rect(screen, [111, 222, 121, ], vistrel_rect1)
        screen.blit(obrabotca_vistrel, vistrel_rect1)


def ogranichnie():
    if obekt.x < 0:
        obekt.x = 1
    if obekt.right > 900:
        obekt.right = 900


def obrabotka_event():
    global mogu_strelyt, fall_block

    e = event.get()
    for r in e:
        if r.type ==TIMER_FALL_BOMB:
            add_bomb()

        if r.type == TIMER_FALL_BLOCK:
            add_block()

        if r.type == pygame.QUIT:
            exit()
        if r.type == pygame.KEYDOWN and r.key == pygame.K_r:
            vistrel()
        if r.type == TIMER_VISTREL:
            mogu_strelyt = True

    keys = key.get_pressed()
    # движение игрока
    if keys[pygame.K_a]:
        obekt.x += -3
    if keys[pygame.K_d]:
        obekt.x += 3


def draw_screen():
    screen.fill([123, 0, 255])
    draw_player()
    draw_block()
    draw_vistrel()

    draw_bomb()
    display.flip()


def draw_player():
    draw.rect(screen,[123,111,111],obekt,1)
    screen.blit(player, obekt)


def attack_vistrel():
    speedy = -5
    for bad in vistrel_rect:
        if bad.y < 100:
            speedy = 0
            print("улетел")
            vistrel_rect.remove(bad)

        bad.y += speedy


def vistrel():
    global vistrel_rect, mogu_strelyt

    if mogu_strelyt == True:
        a = pygame.Rect([obekt.x + 20, obekt.top - 100, 10, 100])
        vistrel_rect.append(a)
        mogu_strelyt = False
        pygame.time.set_timer(TIMER_VISTREL, 1000, 1)


def add_block():
    blocks = pygame.Rect([random.randint(30, 870), 10, 70, 70])
    block.append(blocks)
    pygame.time.set_timer(TIMER_FALL_BLOCK, 2000, 1)


def padenie():
    for dvigenie in block:
        dvigenie.y += 4
        un_padenie = dvigenie.colliderect(obekt)
        if un_padenie==1:
            block.remove(dvigenie)


def draw_block():
    for block1 in block:
        draw.rect(screen,[0,0,0],block1,1)
        screen.blit(obrabotca_block, block1)


#def padenie_bomb


def add_bomb():
    bomb = pygame.Rect(random.randint(0,840),0,60,60,)
    bombs.append(bomb)
    pygame.time.set_timer(TIMER_FALL_BOMB,5000,1)




def draw_bomb():
    for bomb1 in bombs:
        draw.rect(screen,[0,0,0],bomb1,1)
        screen.blit(obrabotka_bomb, bomb1)



while 1 == 1:
    time.sleep(1 / 120)
    obrabotka_event()
    attack_vistrel()
    ogranichnie()
    padenie()
    draw_screen()
