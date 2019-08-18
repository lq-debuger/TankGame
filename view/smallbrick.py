from base.view import Views
from base.destry import DestroyAble
from base.block import BlockAble
import pygame

class SmallBrick(Views,DestroyAble,BlockAble):
    def __init__(self,**kwargs):
        super(SmallBrick, self).__init__(**kwargs, img='./img/wall.gif')
        self.image = pygame.image.load('./img/wall.gif')
        self.width = self.image.get_width()
        self.height = self.image.get_height()