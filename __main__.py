from pygame import draw, event, display, key
import pygame, time, help, random, designer

pygame.init()
TIMER_VISTREL = event.custom_type()
TIMER_FALL_BLOCK = event.custom_type()
TIMER_FALL_BOMB = event.custom_type()
TIMER_FALL_HARD_BOMB = event.custom_type()
schet = 0
heart = 3
new_level = 1
level = 1
secunder = 3000
screen = display.set_mode([900, 675])
shrift = pygame.font.SysFont("comicsansms", 50)
new_levels = pygame.font.SysFont("comicsansms", 100)
print(pygame.font.get_fonts())
win = pygame.font.SysFont("comicsansms", 300)
heart_player_font = pygame.font.SysFont("comicsansms", 30)
# pygame.mixer.music.load('musik/musika.mp3')
# pygame.mixer.music.play()
obrabotca_screen = pygame.image.load(designer.screen[0])
obrabotca_block = pygame.image.load("picture/супер гер бой.jpg")
obrabotca_block = help.izmeni_kartinku(obrabotca_block, 70, 70, [0, 0, 0], 10)
obrabotca_vistrel = pygame.image.load("picture/vistrel.png")
obrabotca_vistrel = help.izmeni_kartinku(obrabotca_vistrel, 40, 110, [0, 0, 0], 10)
player = pygame.image.load("picture/player.jpg")
player = help.izmeni_kartinku(player, 50, 150, [235, 28, 36], 100)
obrabotka_bomb = pygame.image.load("picture/bomb.jpg")
obrabotka_bomb = help.izmeni_kartinku(obrabotka_bomb, 60, 60, [235, 28, 36], 15)
obrabotka_hard_bomb = pygame.image.load("picture/hard bomb.jpg")
obrabotka_hard_bomb = help.izmeni_kartinku(obrabotka_hard_bomb, 80, 80, [184, 61, 186], 10)
pygame.time.set_timer(TIMER_FALL_BLOCK, 2000, 1)
pygame.time.set_timer(TIMER_FALL_BOMB, 5000, 1)
pygame.time.set_timer(TIMER_FALL_HARD_BOMB, secunder)

bombs = []
hard_bombs = []
block = []
obekt_player = pygame.Rect([400, 525, 50, 150])
vistrel_rect = []
mogu_strelyt = True


def draw_vistrel():
    for vistrel_rect1 in vistrel_rect:
        draw.rect(screen, [111, 222, 121, ], vistrel_rect1, 1)
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
        if r.type == TIMER_FALL_BOMB:
            add_bomb()

        if r.type == TIMER_FALL_BLOCK:
            add_block()

        if r.type == TIMER_FALL_HARD_BOMB:
            add_hard_bomb()

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
    screen.blit(obrabotca_screen, [0, 0])
    draw_player()
    draw_block()
    draw_hard_bomb()
    draw_vistrel()
    draw_schet()
    draw_new_level()
    drawheart()
    draw_bomb()
    display.flip()


def draw_schet():
    a = shrift.render(str(schet), True, [255, 255, 0])
    screen.blit(a, [0, 0])


def draw_player():
    draw.rect(screen, [123, 111, 111], obekt_player, 1)
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
    global vistrel_rect, mogu_strelyt, schet

    if mogu_strelyt == True:
        a = pygame.Rect([obekt_player.x + 20, obekt_player.top - 100, 40, 110, ])
        vistrel_rect.append(a)
        mogu_strelyt = False
        pygame.time.set_timer(TIMER_VISTREL, 1000, 1)
        schet -= 1
        if schet <= -10 and level > 1:
            print("gameover")
            exit()


def add_block():
    blocks = pygame.Rect([random.randint(30, 870), 10, 70, 70])
    block.append(blocks)
    pygame.time.set_timer(TIMER_FALL_BLOCK, 2000, 1)


def delete_block():
    global schet
    for blocks in block:
        for vistrel_rect1 in vistrel_rect:
            delete = vistrel_rect1.colliderect(blocks)
            if delete == 1:
                block.remove(blocks)
                vistrel_rect.remove(vistrel_rect1)
                schet -= 10
                if schet <= -10 and level > 1:
                    print("GAME OVER")
                    exit()




def draw_new_level():
    global level, obrabotca_screen, nomer_fona,schet,new_level

    if new_level <= schet:

        level += 1
        a = new_levels.render("new level " + str(level), True, [255, 255, 0])
        screen.fill([0, 0, 0])
        screen.blit(a, [200, 280])
        pygame.display.flip()
        time.sleep(3)

        new_level += 3
        schet = 0


        level2 = level // 2  # номер фона который надо поставить
        if level2 < len(designer.screen):
            obrabotca_screen = pygame.image.load(designer.screen[level2])
            print(level2)


def you_win():
    if level == 20:
        a = win.render("win", True, [255, 255, 30])
        screen.fill([0, 0, 0])
        screen.blit(a, [300, 200])
        pygame.display.flip()
        time.sleep(5)
        exit()


def padenie():
    global schet
    for dvigenie in block:
        dvigenie.y += 4
        un_padenie = dvigenie.colliderect(obekt_player)
        if un_padenie == 1:
            block.remove(dvigenie)
            schet += 1


def draw_block():
    for block1 in block:
        draw.rect(screen, [0, 0, 0], block1, 1)
        screen.blit(obrabotca_block, block1)


def add_bomb():
    bomb = pygame.Rect(random.randint(0, 840), 0, 60, 60, )
    bombs.append(bomb)
    pygame.time.set_timer(TIMER_FALL_BOMB, 5000, 1)


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
    pygame.time.set_timer(TIMER_FALL_HARD_BOMB, secunder)


def falling_hard_bomb():
    for hard_bomb in hard_bombs:
        hard_bomb.y += 1


def draw_hard_bomb():
    for hard_bomb in hard_bombs:
        draw.rect(screen, [100, 100, 100], hard_bomb, 1)
        screen.blit(obrabotka_hard_bomb, hard_bomb)


def popadanie_hard_bomb():
    global heart
    for hard_bomb in hard_bombs:
        a = hard_bomb.colliderect(obekt_player)
        if a == 1:
            heart /= 2
            hard_bombs.remove(hard_bomb)


def delete_hard_bomb():
    global schet
    for vistrel_rect1 in vistrel_rect:
        a = vistrel_rect1.collidelist(hard_bombs)
        if a >= 0:
            schet+=4
            vistrel_rect.remove(vistrel_rect1)
            del hard_bombs[a]




def game_over():
    global heart
    for bomb in bombs:
        game_over1 = bomb.colliderect(obekt_player)
        if game_over1 == 1:
            heart -= 1
            bombs.remove(bomb)
        if heart <= 0:
            print("game_over")
            exit()


def drawheart():
    global heart
    a = heart_player_font.render(str(heart), True, [255, 0, 0])
    screen.blit(a, [30, 0])


def fall_bomb():
    for bomb in bombs:
        bomb.y += 3


def draw_bomb():
    for bomb1 in bombs:
        draw.rect(screen, [0, 0, 0], bomb1, 1)
        screen.blit(obrabotka_bomb, bomb1)


while 1 == 1:
    time.sleep(1 / 120)
    obrabotka_event()
    attack_vistrel()
    ogranichnie()
    fall_bomb()
    delete_bomb()
    delete_block()
    popadanie_hard_bomb()
    you_win()
    game_over()
    falling_hard_bomb()
    padenie()
    delete_hard_bomb()
    draw_screen()
