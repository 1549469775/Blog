import pygame as pg

class Button():

    def __init__(self,upimage,downimage,position):
        self.imageUp=upimage
        self.imageDown=downimage
        self.rect=position

    def isOver(self):
        point_x,point_y=pg.mouse.get_pos()
        x,y=self.rect
        w,h=self.imageUp.get_size()
        return point_x>x and point_x<x+w and point_y>y and point_y<y+h
        # int_x=x-w/2<point_x<x+w/2
        # int_y=y-h/2<point_y<y-h/2
        #
        # return int_x and int_y

    def render(self,screen):
        w,h=self.imageUp.get_size()
        x,y=self.rect
        if self.isOver():
            self.imageDown.update(screen,rect=self.rect)
            print("down")
        else:
            self.imageUp.update(screen,rect=self.rect)