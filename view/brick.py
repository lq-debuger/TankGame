import pygame
from base.view import *
from base.block import BlockAble
from base.suffer import SufferAble

class Brick(Views,BlockAble,SufferAble):

    def __init__(self,**kwargs):
        super(Brick, self).__init__(**kwargs,img='./img/walls.gif')
        self.image = pygame.image.load('./img/walls.gif')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        # 设置血量值
        self.hp = 3

    def notifySuffer(self):
        self.hp -= 1