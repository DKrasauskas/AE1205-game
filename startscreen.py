import pygame as py
import time as tm
import random as rand
import settings as settings


start = py.Rect(350, 350, 100, 100)
p1  = py.Rect(550, 550, 100, 100)
p2 = py.Rect(250, 550, 100, 100)

def startscreen(window, char1, char2):
    RUN = True
    framecount = 0
    while RUN:
        window.fill((0, 0, 0))
        for x in py.event.get():
            if x.type == py.QUIT:
                RUN = False
            if x.type == py.MOUSEBUTTONDOWN:
                if start.collidepoint(py.mouse.get_pos()[0], py.mouse.get_pos()[1]) == 1:
                    RUN = False
                    break
        py.draw.rect(window, (128, 128, 128), start)
        if framecount > 500 and framecount < 1000 :
            window.blit(char1.texture, p1)
        else:
            window.blit(char1.texture_walk, p1)
        if framecount > 500 and framecount < 1000 :
            window.blit(char2.texture, p2)
        else:
            window.blit(char2.texture_flip, p2)
        py.display.update()
        py.display.flip()
        framecount += 1
        if framecount == 1000:
            framecount = 0