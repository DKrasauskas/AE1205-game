import pygame as py
import time as tm
import random as rand
import settings as settings

start = py.Rect(settings.SCR_HEIGHT/2 - 50, settings.SCR_WIDTH/2 - 20, 100, 100)
title = py.Rect(settings.SCR_HEIGHT/2 - 400, settings.SCR_WIDTH/16 - 50, 100, 100)
p1  = py.Rect(550, 550, 100, 100)
p2 = py.Rect(250, 550, 100, 100)
p3 = py.Rect(800, 550, 100, 100)
def startscreen(window, char1, char2, button, caption):
    RUN = True
    framecount = 0
    while RUN:
        window.fill((0, 0, 0))
        for x in py.event.get():
            if x.type == py.QUIT:
                RUN = False
                return True
            if x.type == py.MOUSEBUTTONDOWN:
                if start.collidepoint(py.mouse.get_pos()[0], py.mouse.get_pos()[1]) == 1:
                    RUN = False
                    return False
        if framecount > 200 and framecount < 400 :
            window.blit(char2.texture, p2)
            window.blit(char1.texture, p1)
            window.blit(char2.texture, p3)
        else:
            window.blit(char2.texture_flip, p2)
            window.blit(char1.texture_walk, p1)
            window.blit(char2.texture_walk, p3)
        window.blit(button, start)
        window.blit(caption, title)
        py.display.update()
        py.display.flip()
        framecount += 1
        if framecount == 400:
            framecount = 0
    return False