import pygame, random, controller, view

pygame.init()
obekt_player = pygame.Rect([400, 525, 50, 150])
schet = 0
heart = 3
new_level = 1
level = 1
bombs = []
hard_bombs = []
block = []
vistrel_rect = []
vzriv = False
mogu_strelyt = True


def ogranichnie():
    if obekt_player.x < 0:
        obekt_player.x = 1
    if obekt_player.right > 900:
        obekt_player.right = 900


def attack_vistrel():
    speedy = -5
    for bad in vistrel_rect:
        if bad.y < 100:
            speedy = 0
            print("улетел")
            vistrel_rect.remove(bad)

        bad.y += speedy


def vistrel():
    global vistrel_rect, mogu_strelyt, schet

    if mogu_strelyt == True:
        a = pygame.Rect([obekt_player.x + 20, obekt_player.top - 100, 40, 110, ])
        vistrel_rect.append(a)
        pygame.time.set_timer(controller.TIMER_VISTREL, 1000)
        mogu_strelyt = False

        schet -= 1
        if schet <= -10 and level > 1:
            print("gameover")
            exit()


def add_block():
    blocks = pygame.Rect([random.randint(30, 870), 10, 70, 70])
    block.append(blocks)


def delete_block():
    global schet
    for blocks in block:
        for vistrel_rect1 in vistrel_rect:
            delete = vistrel_rect1.colliderect(blocks)
            if delete == 1:
                block.remove(blocks)
                vistrel_rect.remove(vistrel_rect1)
                schet -= 10


def padenie():
    global schet
    for dvigenie in block:
        dvigenie.y += 4
        un_padenie = dvigenie.colliderect(obekt_player)
        if un_padenie == 1:
            block.remove(dvigenie)
            schet += 1


def add_bomb():
    bomb = pygame.Rect(random.randint(0, 840), 0, 60, 60, )
    bombs.append(bomb)


def delete_bomb():
    for bomb in bombs:
        for vistrel_rect1 in vistrel_rect:
            stolcnovenie = bomb.colliderect(vistrel_rect1)
            if stolcnovenie == 1:
                bomb.y += -300
                bombs.remove(bomb)
                vistrel_rect.remove(vistrel_rect1)


def add_hard_bomb():
    hard_bomb = pygame.Rect(random.randint(0, 830), 0, 80, 80)
    hard_bombs.append(hard_bomb)


def falling_hard_bomb():
    for hard_bomb in hard_bombs:
        hard_bomb.y += 2


def popadanie_hard_bomb():
    global heart, vzriv
    for hard_bomb in hard_bombs:
        a = hard_bomb.colliderect(obekt_player)
        if a == 1:
            heart -= 1.5
            pygame.time.set_timer(controller.TIMER_POYVLENUE_VZRIV_HARD_BOMB, 1000,1)
            hard_bombs.remove(hard_bomb)


def add_vzriv():
    print('взрыв')


def delete_hard_bomb():
    global schet
    for vistrel_rect1 in vistrel_rect:
        a = vistrel_rect1.collidelist(hard_bombs)
        if a >= 0:
            schet += 4
            vistrel_rect.remove(vistrel_rect1)
            del hard_bombs[a]


def game_over():
    global heart
    for bomb in bombs:
        game_over1 = bomb.colliderect(obekt_player)
        if game_over1 == 1:
            heart -= 1
            bombs.remove(bomb)


def fall_bomb():
    for bomb in bombs:
        bomb.y += 3


def model():
    attack_vistrel()
    ogranichnie()
    fall_bomb()
    delete_bomb()
    delete_block()
    popadanie_hard_bomb()
    game_over()
    falling_hard_bomb()
    padenie()
    delete_hard_bomb()
