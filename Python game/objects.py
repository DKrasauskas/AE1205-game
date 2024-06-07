import pygame as py
import time as tm
import random as rand
from settings import *


py.init()
background = py.transform.scale_by(py.image.load("textures/Background.png").convert_alpha(), 6.0)
p1_texture = py.transform.scale_by(py.image.load("textures/knight_walk.png").convert_alpha(), 3.2)
p1_walk_texture = py.transform.scale_by(py.image.load("textures/Knight.png").convert_alpha(), 3.2)
p2_texture = py.transform.scale_by(py.image.load("textures/character_walk.png").convert_alpha(), 3.2)
p2_walk_texture = py.transform.scale_by(py.image.load("textures/Character.png").convert_alpha(), 3.2)
p2_flip_texture = py.transform.scale_by(py.image.load("textures/character_flipped.png").convert_alpha(), .1)
obstacle =  py.transform.scale_by(py.image.load("textures/Hurdle.png").convert_alpha(), 7.0)
start_button =  py.transform.scale_by(py.image.load("textures/start_button.png").convert_alpha(), .1)
caption = py.transform.scale_by(py.image.load("textures/title.png").convert_alpha(), .2)
class Character:
    def __init__(self, v) -> None:
        self.hitbox = py.Rect(200, 200, 400, 400)
        self.vx = 0
        self.vy = 0
        self.x = 0
        self.y = 0
        self.a = 0
        self.v = v
        self.render = True
    def move(self, dt, scr_x):
        self.vy += self.a * dt
        self.x = self.x + self.vx * dt
        self.y += self.vy * dt 
        if(self.x - scr_x > 0 and self.x - scr_x < SCR_HEIGHT):
            self.hitbox.update(self.x - scr_x, self.y, 40, 80)
    def move_obstacle(self, dt, scr_x):
        self.vy += self.a
        self.x = self.x + self.vx
        self.y += self.vy 
        if(self.x - scr_x > -400 and self.x - scr_x < SCR_HEIGHT):
            self.hitbox.update(self.x - scr_x, self.y, 200, 80)
            self.render = True
        else:
            self.hitbox.update(-1000, self.y, 20, 20)
            self.render = False
    def handle_bounds(self):
        if self.y >= FLOOR_HEIGHT and self.vy >= 0:
            self.y = FLOOR_HEIGHT
            self.vy = 0
        if self.hitbox.x >= SCR_WIDTH:
            self.vx = -self.vx
        if self.hitbox.x <= 10:
            self.vx = self.v
    def jump(self):
        if self.y >= FLOOR_HEIGHT:
            self.vy = -400
            self.a = 502
        py.mixer.music.load("audio/jump.mp3")
        py.mixer.music.set_volume(1000)
        py.mixer.music.play(0, 0, 12000)
         

obstacles = []

for x in range(1, 200):
    chr = Character(0)
    chr.x = x * (1000 + (abs(rand.random())) * 500)
    chr.hitbox.update(600, 600, 600, 600)
    chr.texture = obstacle
    chr.y = FLOOR_HEIGHT
    obstacles.append(chr)
char1 = Character(800)
char1.texture = p1_texture
char1.texture_walk = p1_walk_texture
char1.x = 100
char1.y = 700
char2 = Character(800)
char2.texture = p2_texture
char2.texture_walk = p2_walk_texture
char2.texture_flip = p2_flip_texture
char2.x = 200
char2.y = 700

def handle_movementP1(event, character):
    if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    character.vx = -character.v if character.vx == 0 else  0
                if event.key == py.K_RIGHT:
                   character.vx = character.v if character.vx == 0 else  0
                if event.key == py.K_UP:
                    character.jump()
def handle_movementP2(event, character):
    if event.type == py.KEYDOWN:
                if event.key == py.K_a:
                    character.vx = -character.v if character.vx == 0 else  0
                if event.key == py.K_d:
                    character.vx = character.v
                if event.key == py.K_w:
                    character.jump()

