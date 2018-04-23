import pygame as pg
from pygame.locals import BLEND_ADD

class Image(pg.sprite.Sprite):

    color = (255, 255, 255)

    def __init__(self,path,color,init_pos):
        pg.sprite.Sprite.__init__(self)
        # 加载并转换图像
        # bkgd = pg.image.load(bkgd_img).convert()
        self.image = pg.image.load(path).convert_alpha()
        self.rect=self.image.fill(color,None,BLEND_ADD)
        self.rect.topleft=init_pos
        self.width, self.height = self.image.get_size()
        self.color=color

    def update(self,screen, *args,**kwargs):
        try:
            if kwargs.get('rect'):
                self.rect = kwargs['rect']
        except KeyError as error:
            print(error)
        screen.blit(self.image,self.rect)

    #--------------属性方法
    def set_image(self,image):
        self.width, self.height = self.image.get_size()
        self.image=image

    def get_size(self):
        return self.image.get_size()

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
    #--------------点击方法
    click = False