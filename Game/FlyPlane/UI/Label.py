import pygame as pg

class Label(pg.sprite.Sprite):
    text=""
    color=(255, 255, 255)
    rect=(0,0)
    def __init__(self,text,size=30,color=(255, 255, 255),position=(0,0)):
        pg.sprite.Sprite.__init__(self)
        # myfont = pg.font.Font("china.ttf", size)
        self.myfont = pg.font.SysFont("SimHei", size)
        self.text = text
        self.color = color
        self.rect=position
        self.image = self.myfont.render(self.text, True, self.color)

    def update(self,screen, *args,**kwargs):
        try:
            if kwargs.get('text'):
                self.text = kwargs['text']
            if kwargs.get('color'):
                self.color = kwargs['color']
            if kwargs.get('rect'):
                self.rect = kwargs['rect']
        except KeyError as error:
            print(error)
        self.image = self.myfont.render(self.text, True, self.color)
        screen.blit(self.image,self.rect)

    def get_width(self):
        return self.myfont.size(self.text)[0]

    def get_height(self):
        return self.myfont.size(self.text)[1]