from pygame import draw,display
import pygame,designer,model,time,help
pygame.init()
screen = display.set_mode([900, 675])
shrift = pygame.font.SysFont("vinerhanditc", 50)
new_levels = pygame.font.SysFont("vinerhanditc", 200)
print(pygame.font.get_fonts())
win = pygame.font.SysFont("vinerhanditc", 300)
heart_player_font = pygame.font.SysFont("vinerhanditc", 30)
game_over_font=pygame.font.SysFont('vinerhanditc', 150)
#pygame.mixer.music.load('musik/musika.mp3')
#pygame.mixer.music.play()
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
obrabotca_vzriv=pygame.image.load('picture/Взрыв.png')
obrabotca_vzriv =help.izmeni_kartinku(obrabotca_vzriv,100,100,[63,72,204],10)
obrabotca_heal=pygame.image .load('picture/сердце.png')
obrabotca_heal=help.izmeni_kartinku(obrabotca_heal,30,30,[255,255,255],10)
obrabotca_shit=pygame.image.load('picture/разлом.jpg')
obrabotca_shit=help.izmeni_kartinku(obrabotca_shit, 100, 100, [255, 255, 255], 20)
obrabotca_shit=pygame.transform.rotate(obrabotca_shit, 270)


def draw_screen():
    screen.blit(obrabotca_screen, [0, 0])
    draw_player()
    draw_hard_bomb()
    draw_vistrel()
    draw_schet()
    draw_heal()
    draw_new_level()
    draw_heart()
    draw_game_over()
    draw_shit()
    draw_vzriv()
    you_win()
    draw_bomb()
    draw_lazer()
    draw_block()
    display.flip()


def draw_vistrel():
    for vistrel_rect1 in model.vistrel_rect:
        #draw.rect(screen, [111, 222, 121, ], vistrel_rect1, 1)
        screen.blit(obrabotca_vistrel, vistrel_rect1)


def draw_lazer():
    if model.lazer is not None:
        draw.rect(screen,[0,0,147],model.lazer)


def draw_schet():
    a = shrift.render(str(model.schet), True, [255, 255, 0])
    screen.blit(a, [0, 0])


def draw_player():
    #draw.rect(screen, [123, 111, 111], model.obekt_player, 1)
    screen.blit(player, model.obekt_player)


def draw_vzriv():
    if model.vzriv is not None :
        screen.blit(obrabotca_vzriv,model.vzriv)


def draw_new_level():
    global level, obrabotca_screen, nomer_fona, schet, new_level

    if model.new_level <= model.schet :

        model.level += 1
        a = new_levels.render("level " + str(model.level), True, [255, 255, 0])
        screen.fill([0, 0, 0])
        screen.blit(a, [200, 280])
        pygame.display.flip()
        model.new_level += 3
        model.schet = 0
        time.sleep(3)



        level2 = model.level // 2  # номер фона который надо поставить
        if level2 < len(designer.screen):
            obrabotca_screen = pygame.image.load(designer.screen[level2])
            print(level2)


def you_win():
    if model.level == 20:
        a = win.render("win", True, [255, 255, 30])
        screen.fill([0, 0, 0])
        screen.blit(a, [300, 200])
        pygame.display.flip()
        time.sleep(5)
        exit()





def draw_game_over():
    if model.heart<=0   or model.schet<=-10:

        a=game_over_font.render('GAME OVER',True,[200,30,50])
        r=a.get_rect()
        screen.fill([255,0,0])
        r.centerx=900/2
        r.centery=675/2
        screen.blit(a,r)

        pygame.display.flip()
        time.sleep(5)
        exit()


def draw_block():
    for block1 in model.blocks:
        #draw.rect(screen, [0, 0, 0], block1, 1)
        screen.blit(obrabotca_block, block1)


def draw_hard_bomb():
    for hard_bomb in model.hard_bombs:
        #draw.rect(screen, [100, 100, 100], hard_bomb, 1)
        screen.blit(obrabotka_hard_bomb, hard_bomb)


def draw_heart():
    global heart
    a = heart_player_font.render(str(model.heart), True, [255, 0, 0])
    screen.blit(a, [830, 0])


def draw_heal():
    for heal in model.heal:
        screen.blit(obrabotca_heal,heal)



def draw_bomb():
    for bomb1 in model.bombs:
        # draw.rect(screen, [0, 0, 0], bomb1, 1)
        screen.blit(obrabotka_bomb, bomb1)


def draw_shit():
    for udar in model.shit:
        screen.blit(obrabotca_shit, udar)
        #draw.rect(screen,[0,0,0],udar,1)