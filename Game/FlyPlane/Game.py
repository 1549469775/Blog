import os

import pygame as pg

from base import sub_file


class Game(object):

    sprites = {}
    sprites_path = {}
    panels = []
    __event__=None

    def __init__(self, width, height, title="Game", *args, **kwargs):
        self.screen_width = width
        self.screen_height = height
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption(title)
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.screen.fill((255, 255, 255))  # (200,80,60)
        self.ui()

    def ui(self):
        pass

    def __event_loop_base(self):
        self.__event__=pg.event.get()
        for event in self.__event__:
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.done = True
        for panel in self.panels:
            panel.event_loop(self.__event__)

    def event_loop(self,event):
        pass

    def __draw_base(self):
        for panel in self.panels:
            panel.update(self.screen)

    def draw(self):
        pass

    def __update_base(self, dt):
        pass

    def update(self, dt):
        pass

    def run(self):
        dt = self.clock.tick(self.fps)
        while not self.done:
            self.__event_loop_base()
            self.event_loop(self.__event__)
            self.__update_base(dt)
            self.update(dt)
            self.__draw_base()
            self.draw()
            pg.display.update()

    def list_all(self):
        for name, value in vars(self).items():
            print('%s=%s' % (name, value))
