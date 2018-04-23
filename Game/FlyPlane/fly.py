import math
import os
import time

import pygame as pg

from Game import Game
from Panel.StartPanel import StartPanel
from UI.Label import Label
from UI.Image import Image
from base import sub_file


class WalkGame(Game):

    def __init__(self, width, height, title="Game", *args, **kwargs):
        Game.__init__(self, width, height, title, *args, **kwargs)

    def load_sprites(self):
        files = sub_file('./res')
        for key, value in files.items():
            if key == 'image' or key == 'sound':
                for res in value:
                    if res.find('.') != -1:
                        self.sprites_path[res[:res.find('.')]] = os.path.join(".\\res", key, res)
        for key,value in self.sprites_path.items():
            if value.rfind(".")!=-1:
                if os.path.splitext(value)[1] == '.png' or os.path.splitext(value)[1] == ".jpg":
                    image=Image(value, (0, 0, 0), (0, 0))
                    setattr(self,key,image)
                    self.sprites[key]=image
                if os.path.splitext(value)[1]==".wav":
                    sound = pg.mixer.Sound(value)
                    setattr(self, key, sound)
                    self.sprites[key] = sound

    def ui(self):
        self.load_sprites()

        res = ['bg', "background", "btn_finish", "name", 'restart_nor', 'bullet1']
        voice = ['game_music', 'get_bomb']
        exc = ["hero1", "hero2"]
        self.start=StartPanel(self.sprites_path,self.sprites,res,voice,exc)
        # self.start.from_all_add(self.sprites,res,voice,exc)
        self.panels.append(self.start)

    def draw(self):
        # pg.mouse.set_visible(False)
        # self.start.draw(self.screen)
        pass

    def update(self, dt):
        pass

    def event_loop(self,events):
        pass


if __name__=="__main__":
    pg.init()
    pg.mixer.init()
    game=WalkGame(800,600)
    # game.list_all()
    game.run()
    pg.quit()
