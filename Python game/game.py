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
py.mixer.music.load("audio/audio.mp3")
py.mixer.music.set_volume(50)
py.mixer.music.play(0, 0, 12000)


begin = tm.time()
prev = tm.time()

initial.startscreen(window, char1, char2, start_button, caption)
py.mixer.music.fadeout(1000)
RUN = True
py.mixer.music.load("audio/gasgas.mp3")
py.mixer.Channel(0).play(py.mixer.Sound('audio/gasgas.mp3'), 100, 0, 10000)
py.mixer.Channel(0).set_volume(10)

scr_x = 0
scr_y = 0

mov = 0
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
    if (char1.x - scr_x >= 400 and char1.vx > 0) or (char2.x - scr_x >= 400 and char2.vx > 0):
        scr_x += char1.vx * (begin - tprev) if char1.vx != 0 else char2.vx *( begin - tprev)
    char1.move(begin - tprev, scr_x)
    char2.move(begin - tprev, scr_x)
    
    #coll.move(begin - tprev)
    window.blit(background, (-scr_x, 100))
    if framecount > 50 and framecount < 100 and char1.vx != 0:
         window.blit(char1.texture, char1.hitbox)
    else:
        window.blit(char1.texture_walk, char1.hitbox)
    if framecount > 50 and framecount < 100 and char2.vx != 0:
         window.blit(char2.texture, char2.hitbox)
        # py.draw.rect(window, (0, 128 ,128),char2.hitbox)
    else:
        window.blit(char2.texture_walk, char2.hitbox)
    for x in obstacles:
         x.move_obstacle(0, scr_x)
         if x.render: window.blit(x.texture, x.hitbox)
        # py.draw.rect(window, (0, 128 ,128), x.hitbox)
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
RUN = True
winner = py.Rect(SCR_HEIGHT/2 - 50, SCR_WIDTH/2 - 50, 100, 100)
py.mixer.Channel(0).play(py.mixer.Sound('audio/victory.mp3'), 100, 0, 10000)
while RUN:
    tprev = begin
    begin = tm.time()
    window.fill((0 ,0, 0))
    for x in py.event.get():
        if x.type == py.QUIT:
            RUN = False
    if framecount < 200:
        window.fill((255, 125, 125))
    else:
        window.fill((0, 125, 125))
    window.blit(victor.texture, winner)
   # py.draw.rect(window, (255, 255, 0), winner)
    py.display.update()
    py.display.flip()
    framecount += 1
    if framecount == 400:
        framecount = 0