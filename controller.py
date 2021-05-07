from pygame import event,key
import model,pygame
pygame.init()
secunder = 10000
TIMER_VISTREL = event.custom_type()
TIMER_FALL_BLOCK = event.custom_type()
TIMER_FALL_BOMB = event.custom_type()
TIMER_FALL_HARD_BOMB = event.custom_type()
pygame.time.set_timer(TIMER_FALL_BLOCK, 2000)
pygame.time.set_timer(TIMER_FALL_BOMB, 5000)
pygame.time.set_timer(TIMER_FALL_HARD_BOMB, secunder)


def obrabotka_event():
    global mogu_strelyt, fall_block

    e = event.get()
    for r in e:
        if r.type == TIMER_FALL_BOMB:
            model.add_bomb()

        if r.type == TIMER_FALL_BLOCK:
            model.add_block()

        if r.type == TIMER_FALL_HARD_BOMB:
            model.add_hard_bomb()

        if r.type == pygame.QUIT:
            exit()
        if r.type == pygame.KEYDOWN and r.key == pygame.K_r:
            model.vistrel()
        if r.type == TIMER_VISTREL:
            model.mogu_strelyt = True


    keys = key.get_pressed()
    # движение игрока
    if keys[pygame.K_a]:
        model.obekt_player.x += -4
    if keys[pygame.K_d]:
        model.obekt_player.x += 4
