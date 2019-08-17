import pygame
from base.view import *
from base.block import BlockAble
from base.suffer import SufferAble

class Steel(Views,BlockAble,SufferAble):

    def __init__(self,**kwargs):
        super(Steel, self).__init__(**kwargs,img='./img/steels.gif')
        self.image = pygame.image.load('./img/steels.gif')
        self.width = self.image.get_width()
        self.height = self.image.get_height()

