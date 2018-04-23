import math
import os
import time

import pygame as pg

from UI.Image import Image


class Panel(object):

    group = pg.sprite.Group()
    sprites_path={}
    my_sprites={}
    my_voice={}
    my_extra={}

    def __init__(self,sprites_path,sprites,img=[],voice=[],extra=[],*args, **kwargs):
        for r in img:
            if r in sprites.keys():
                self.my_sprites[r]=sprites[r]
                self.sprites_path[r]=sprites_path[r]
                setattr(self, r, sprites[r])
                self.group.add(sprites[r])
        for r in voice:
            if r in sprites.keys():
                self.my_voice[r]=sprites[r]
                self.sprites_path[r] = sprites_path[r]
                setattr(self, r, sprites[r])
        for r in extra:
            if r in sprites.keys():
                self.my_extra[r]=sprites[r]
                self.sprites_path[r] = sprites_path[r]
                setattr(self, r, sprites[r])

    # def from_all_add(self,sprites,res=[],voice=[],exec=[]):
    #     for r in res:
    #         if r in sprites.keys() and r not in exec:
    #             setattr(self, r, sprites[r])
    #             self.group.add(sprites[r])
    #         elif r in exec:
    #             self.exce_sprite[r]=sprites[r]
    #     for v in voice:
    #         if v in sprites.keys() and r not in exec:
    #             setattr(self, v, sprites[v])
    #         elif v in exec:
    #             self.exce_sprite[v] = sprites[v]

    def add_sprite(self,key,sprite):
        setattr(self, key, sprite)
        self.group.add(sprite)

    def add_wav(self,key,voice):
        setattr(self, key, voice)

    def hide_sprite(self,sprite):
        self.group.remove(sprite)

    def show_sprite(self,sprite):
        if not self.group.has(sprite):
            self.group.add(sprite)

    def is_visible(self,sprite):
        return self.group.has(sprite)

    def del_sprite(self,key,sprite):
        del self[key]
        self.group.remove(sprite)

    def show(self):
        print(list(self.group.sprites()))
        for name, value in vars(self).items():
            print('%s=%s' % (name, value))

    def event_loop(self,events):
        pass

    def update(self,screen):
        self.group.update(screen)