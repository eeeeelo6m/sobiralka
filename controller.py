from pygame import event,key
import model,pygame
pygame.init()

TIMER_VISTREL = event.custom_type()
TIMER_FALL_BLOCK = event.custom_type()
TIMER_FALL_BOMB = event.custom_type()
TIMER_POYVLENIE_SHITA=event.custom_type()
TIMER_FALL_HARD_BOMB = event.custom_type()
TIMER_POYVLENUE_VZRIV_HARD_BOMB= event.custom_type()
TIMER_PROPADANIE_VZRIV_HARD_BOMB=event.custom_type()
TIMER_HAEL=event.custom_type()
pygame.time.set_timer(TIMER_FALL_BLOCK, 2000)
pygame.time.set_timer(TIMER_FALL_BOMB, 5000)
pygame.time.set_timer(TIMER_HAEL,3000)
pygame.time.set_timer(TIMER_POYVLENIE_SHITA,3000)
pygame.time.set_timer(TIMER_FALL_HARD_BOMB, model.secunder,1)


def obrabotka_event():
    global mogu_strelyt, fall_block

    e = event.get()
    for r in e:
        if r.type == TIMER_FALL_BOMB:
            model.add_bomb()

        if r.type == TIMER_FALL_BLOCK:
            model.add_block()

        if r.type==TIMER_PROPADANIE_VZRIV_HARD_BOMB:
            model.delete_vzriv()

        if r.type==TIMER_POYVLENUE_VZRIV_HARD_BOMB:

             model.add_vzriv()

        if r.type==pygame.MOUSEBUTTONDOWN and r.button==pygame.BUTTON_RIGHT:
            model.add_shit([200,300])
        if r.type==TIMER_POYVLENIE_SHITA:
            model.mogu_stavit_shit=True
        if r.type == TIMER_FALL_HARD_BOMB:
            model.add_hard_bomb()
        if r.type == TIMER_HAEL:
            model.add_heal()
        if r.type == pygame.QUIT:
            exit()
        if r.type == pygame.MOUSEBUTTONDOWN and r.button == pygame.BUTTON_LEFT:
            model.vistrel()
        if r.type == TIMER_VISTREL:
            model.mogu_strelyt = True


    keys = key.get_pressed()
    # движение игрока
    if keys[pygame.K_a]:
        model.obekt_player.x += -4
    if keys[pygame.K_d]:
        model.obekt_player.x += 4
