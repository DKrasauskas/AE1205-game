import pygame as py
import time as tm
import random as rand
import settings as settings
import startscreen as initial

SCR_WIDTH    = settings.SCR_WIDTH
SCR_HEIGHT   = settings.SCR_HEIGHT
FLOOR_HEIGHT = settings.FLOOR_HEIGHT
py.init()
window = py.display.set_mode((SCR_HEIGHT, SCR_WIDTH))

from objects import *
py.mixer.init()
begin = tm.time()
prev = tm.time()

def main_func():
    global begin, prev, window, obstacles, start_button, caption, vel
    char1 = Character(vel)
    char1.texture = p1_texture
    char1.texture_walk = p1_walk_texture
    char1.x = 100
    char1.y = 700
    char2 = Character(vel)
    char2.texture = p2_texture
    char2.texture_walk = p2_walk_texture
    char2.texture_flip = p2_flip_texture
    char2.x = 200
    char2.y = 700
    grail = Character(0)
    grail.y = FLOOR_HEIGHT - 200
    grail.hitbox.update(600, 600, 600, 600)
    grail.x = 22900
    grail.texture = grailTX
    py.mixer.Channel(0).play(py.mixer.Sound('audio/main_menu.mp3'), 100, 0, 10000)
    if initial.startscreen(window, char1, char2, start_button, caption):return
    py.mixer.music.fadeout(1000)
    RUN = True
    py.mixer.Channel(0).play(py.mixer.Sound('audio/main_theme.mp3'), 100, 0, 100000)
    py.mixer.Channel(0).set_volume(10)

    scr_x = 0
    framecount = 0
    victor = None
    while RUN:
        tprev = begin
        begin = tm.time()
        window.fill((0 ,0, 0))
        for x in py.event.get():
            if x.type == py.QUIT:
                RUN = False
            handle_movementP1(x, char1)
            handle_movementP2(x, char2)
        char1.handle_bounds()
        char2.handle_bounds()
        if (char1.x - scr_x >= 900 and char1.vx > 0) or (char2.x - scr_x >= 900 and char2.vx > 0):
            scr_x += char1.vx * (begin - tprev) if char1.vx != 0 else char2.vx *( begin - tprev)
        char1.move(begin - tprev, scr_x)
        char2.move(begin - tprev, scr_x)
        window.blit(background, (-scr_x, 0))
        if framecount > 50 and framecount < 100 and char1.vx != 0:
            window.blit(char1.texture, char1.hitbox)
        else:
            window.blit(char1.texture_walk, char1.hitbox)
        if framecount > 50 and framecount < 100 and char2.vx != 0:
            window.blit(char2.texture, char2.hitbox)
        else:
            window.blit(char2.texture_walk, char2.hitbox)
        grail.move_obstacle(0, scr_x)
        if grail.render == True :
            window.blit(grailTX, grail.hitbox)
        for x in obstacles:
            x.move_obstacle(0, scr_x)
            if x.render: window.blit(x.texture, x.hitbox)
            if char1.hitbox.colliderect(x.hitbox):
                char1.vx = 0
            if char2.hitbox.colliderect(x.hitbox):
                char2.vx = 0
        if char1.x > 23000:
            RUN = False
            victor = char1
        if char2.x > 23000:
            RUN = False
            victor = char2
        py.display.update()
        py.display.flip()
        framecount += 1
        if framecount == 100:
            framecount = 0
   
    #victory path
    RUN = True
    winner = py.Rect(SCR_HEIGHT/2 - 30, SCR_WIDTH/4 - 50, 100, 100)
    py.mixer.Channel(0).play(py.mixer.Sound('audio/victory.mp3'), 100, 0, 10000)
    central_sign = py.Rect(SCR_HEIGHT/2 - 150, SCR_WIDTH/2 - 150, 300, 300)
    end = py.Rect(SCR_HEIGHT/2 - 150, SCR_WIDTH/2 + 150, 300, 300)
    while RUN:
        tprev = begin
        begin = tm.time()
        window.fill((0 ,0, 0))
        for x in py.event.get():
            if x.type == py.QUIT:
                RUN = False
                break
            if x.type == py.MOUSEBUTTONDOWN:
                if end.collidepoint(py.mouse.get_pos()[0], py.mouse.get_pos()[1]) == 1:
                    scr_x = 0
                    #recursive call cuz python sucks (not really) and doesnt have goto statements
                    main_func()
                    RUN = False
                    break
        if framecount < 200:
            window.fill((255, 125, 125))
        else:
            window.fill((0, 125, 125))
        window.blit(wn, central_sign)
        window.blit(victor.texture, winner)
        window.blit(restart, end)
        py.display.update()
        py.display.flip()
        framecount += 1
        if framecount == 400:
            framecount = 0
main_func()