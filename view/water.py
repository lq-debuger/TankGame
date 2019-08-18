from base.view import *
from base.block import BlockAble
import pygame

class Water(Views,BlockAble):

    def __init__(self,**kwargs):
        super(Water, self).__init__(**kwargs,img='../img/water.gif')
        self.image =pygame.image.load('../img/water.gif')
        self.width = self.image.get_width()
        self.height = self.image.get_height()