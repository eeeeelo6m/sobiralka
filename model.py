import pygame, random, controller, time

pygame.init()
obekt_player = pygame.Rect([400, 525, 50, 150])
schet = 0
heart = 3
new_level = 1
level = 1
secunder = 10000

bombs = []
hard_bombs = []
blocks = []
vistrel_rect = []
heal=[]
shit=[]
mogu_stavit_shit=True
vzriv = None
vzriv_x=None
vzriv_y=None
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


def add_shit():
    global mogu_stavit_shit
    if mogu_stavit_shit:
        a=pygame.Rect(random.randint(0,500),301,50,50)
        shit.append(a)
        mogu_stavit_shit=False
        pygame.time.set_timer(controller.TIMER_POYVLENIE_SHITA,3000)


def funkcii_shita():
    global schet
    for block in blocks:
        for bomb in bombs:
            for shits in shit:
                a=block.colliderect(shits)
                if a==1:
                    schet+=1
                    blocks.remove(block)
                    shit.remove(shits)
                    break

def add_block():
    block = pygame.Rect([random.randint(30, 870), 10, 70, 70])
    blocks.append(block)


def delete_block():
    global schet
    for block in blocks:
        for vistrel_rect1 in vistrel_rect:
            delete = vistrel_rect1.colliderect(block)
            if delete == 1:
                blocks.remove(block)
                vistrel_rect.remove(vistrel_rect1)
                schet -= 10


def add_heal():
    if level>=3:
        heal.append(pygame.Rect(random.randint(0, 870), 0, 30, 30))



def heal_player():
    global heart
    for heal_player in heal:

        a = heal_player.colliderect(obekt_player)

        if a == 1:
            heart+=1
            if heart>3:
                heart=3
            heal.remove(heal_player)

        heal_player.y += 2


def padenie():
    global schet
    for dvigenie in blocks:
        dvigenie.y += 4
        un_padenie = dvigenie.colliderect(obekt_player)
        if un_padenie == 1:
            blocks.remove(dvigenie)
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
    pygame.time.set_timer(controller.TIMER_FALL_HARD_BOMB, secunder, 1)


def falling_hard_bomb():
    for hard_bomb in hard_bombs:
        hard_bomb.y += 2


def popadanie_hard_bomb():
    global heart,vzriv_x,vzriv_y
    for hard_bomb in hard_bombs:
        a = hard_bomb.colliderect(obekt_player)
        if a == 1:
            heart -= 1.5
            start_vzriv(hard_bomb)
            hard_bombs.remove(hard_bomb)


def uscorenie():
    global secunder
    for hard_bomb in hard_bombs:
        if hard_bomb.y>515:
            hard_bombs.remove(hard_bomb)
            start_vzriv(hard_bomb)
            if secunder>3000:
                secunder-=500


def popadanie_vzriv():
    global vzriv
    if vzriv is None:
        return

    a=vzriv.colliderect(obekt_player)
    if a==1:
        posledstviy_vzriv()
        vzriv=None


def start_vzriv(hard_bomb):
    global  vzriv_x,vzriv_y
    vzriv_x = hard_bomb.centerx
    vzriv_y = hard_bomb.centery
    pygame.time.set_timer(controller.TIMER_POYVLENUE_VZRIV_HARD_BOMB, 1000, 1)

def add_vzriv():
    global vzriv
    vzriv = pygame.Rect(0,0,100,100)
    vzriv.center=[vzriv_x,vzriv_y]
    pygame.time.set_timer(controller.TIMER_PROPADANIE_VZRIV_HARD_BOMB,500,1)


def posledstviy_vzriv():
    global heart ,schet
    heart -=0.50
    if schet >=0:
        schet /=2

def delete_vzriv():
    global vzriv
    vzriv=None


def delete_hard_bomb():
    global schet,vzriv_x,vzriv_y
    for vistrel_rect1 in vistrel_rect:
        a = vistrel_rect1.collidelist(hard_bombs)
        if a >= 0:
            schet += 4
            start_vzriv(hard_bombs[a])
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
    uscorenie()
    delete_hard_bomb()
    popadanie_vzriv()
    funkcii_shita()
    heal_player()