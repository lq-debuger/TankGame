import pygame
from base.view import *
from base.block import BlockAble
from base.suffer import SufferAble
from base.destry import DestroyAble

class Brick(Views,BlockAble,SufferAble,DestroyAble):

    def __init__(self,**kwargs):
        super(Brick, self).__init__(**kwargs,img='./img/walls.gif')
        self.image = pygame.image.load('./img/walls.gif')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        # 设置血量值
        self.hp = 3
        # 设置销毁状态
        self.shouldDestroy = False

    def notifySuffer(self):
        self.hp -= 1

    def needDestroy(self):
        if self.hp <= 0:
            self.shouldDestroy = True
            return self.shouldDestroy
