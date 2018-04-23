import math
import os
import time

import pygame as pg

from Base.Panel import Panel
from UI.Image import Image


class StartPanel(Panel):
    first=True

    player=None
    exce_sprite={}

    up=False
    down=False
    left=False
    right=False

    rect=(0,0,800,600)
    speed=2

    def __init__(self,*args, **kwargs):
        Panel.__init__(self,*args, **kwargs)
        self.player=Image(".\\res\\image\\plane.png", (0, 0, 0), (0, 0))

    def event_loop(self,events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.up=True
                if event.key == pg.K_s:
                    self.down=True
                if event.key == pg.K_a:
                    self.left=True
                if event.key == pg.K_d:
                    self.right=True
                if event.key == pg.K_SPACE:
                    self.get_bomb.play()
            if event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    self.up=False
                if event.key == pg.K_s:
                    self.down=False
                if event.key == pg.K_a:
                    self.left=False
                if event.key == pg.K_d:
                    self.right=False

    def move_hero(self,plane):
        if self.up:
            plane.rect = (plane.rect[0], plane.rect[1] - self.speed)
        if self.down:
            plane.rect = (plane.rect[0], plane.rect[1] + self.speed)
        if self.left:
            plane.rect = (plane.rect[0] - self.speed, plane.rect[1])
        if self.right:
            plane.rect = (plane.rect[0] + self.speed, plane.rect[1])
        self.limteInSide(plane)

        if self.up==True or self.down==True or self.left==True or self.right==True:
            self.player.image = self.exce_sprite['hero2'].image
        elif self.up==False and self.down==False and self.left==False and self.right==False:
            self.player.image = self.exce_sprite['hero1'].image

    def limteInSide(self,plane):
        if plane.rect[1] <= self.rect[1]:
            plane.rect = (plane.rect[0], self.rect[1])
        if plane.rect[1] >= self.rect[3] - plane.get_height():
            plane.rect = (plane.rect[0], self.rect[3] - plane.get_height())
        if plane.rect[0] <= self.rect[0]:
            plane.rect = (self.rect[0], plane.rect[1])
        if plane.rect[0] >= self.rect[2] - plane.get_width():
            plane.rect = (self.rect[2] - plane.get_width(), plane.rect[1])
    def set_limte(self):
        self.rect = (self.bg.get_width() / 2 - self.background.get_width() / 2, 200,
                     self.bg.get_width() / 2 + self.background.get_width() / 2, 600)

    def update(self,screen):
        if self.first:
            self.first=False

            self.player.rect=self.exce_sprite['hero1'].rect
            self.player.image=self.exce_sprite['hero1'].image
            self.group.add(self.player)

            self.game_music.play(loops=100000000)
            self.player.rect = (self.bg.get_width() / 2 - self.name.get_width() / 2 + 30, 400)
            self.set_limte()
        self.move_hero(self.player)
        self.group.update(screen)