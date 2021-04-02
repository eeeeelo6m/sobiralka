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
obekt_player = pygame.Rect([400, 550, 50, 150])
vistrel_rect = []
mogu_strelyt = True


def draw_vistrel():
    for vistrel_rect1 in vistrel_rect:
        draw.rect(screen, [111, 222, 121, ], vistrel_rect1,1)
        screen.blit(obrabotca_vistrel, vistrel_rect1)


def ogranichnie():
    if obekt_player.x < 0:
        obekt_player.x = 1
    if obekt_player.right > 900:
        obekt_player.right = 900


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
        obekt_player.x += -4
    if keys[pygame.K_d]:
        obekt_player.x += 4


def draw_screen():
    screen.fill([123, 0, 255])
    draw_player()
    draw_block()
    draw_vistrel()

    draw_bomb()
    display.flip()


def draw_player():
    draw.rect(screen, [123,111,111], obekt_player, 1)
    screen.blit(player, obekt_player)


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
        a = pygame.Rect([obekt_player.x + 20, obekt_player.top - 100, 40,110,])
        vistrel_rect.append(a)
        mogu_strelyt = False
        pygame.time.set_timer(TIMER_VISTREL, 1000, 1)


def add_block():
    blocks = pygame.Rect([random.randint(30, 870), 10, 70, 70])
    block.append(blocks)
    pygame.time.set_timer(TIMER_FALL_BLOCK, 2000, 1)


def delete_block():
    for blocks in block:
        for vistrel_rect1 in vistrel_rect:
            delete=vistrel_rect1.colliderect(blocks)
            if delete==1:
                block.remove(blocks)
                vistrel_rect.remove(vistrel_rect1)



def padenie():
    for dvigenie in block:
        dvigenie.y += 4
        un_padenie = dvigenie.colliderect(obekt_player)
        if un_padenie==1:
            block.remove(dvigenie)


def draw_block():
    for block1 in block:
        draw.rect(screen,[0,0,0],block1,1)
        screen.blit(obrabotca_block, block1)





def add_bomb():
    bomb = pygame.Rect(random.randint(0,840),0,60,60,)
    bombs.append(bomb)
    pygame.time.set_timer(TIMER_FALL_BOMB,5000,1)


def delete_bomb():
    for bomb in bombs:
        for vistrel_rect1 in vistrel_rect:
            stolcnovenie=bomb.colliderect(vistrel_rect1)
            if stolcnovenie==1:
                bomb.y+=-400
                bombs.remove(bomb)
                vistrel_rect.remove(vistrel_rect1)


def fall_bomb():
    for bomb in bombs:
        bomb.y+=3



def draw_bomb():
    for bomb1 in bombs:
        draw.rect(screen,[0,0,0],bomb1,1)
        screen.blit(obrabotka_bomb, bomb1)



while 1 == 1:
    time.sleep(1 / 120)
    obrabotka_event()
    attack_vistrel()
    ogranichnie()
    fall_bomb()
    delete_bomb()
    delete_block()
    padenie()
    draw_screen()
