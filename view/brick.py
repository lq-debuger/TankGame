import pygame
from base.view import *
from base.block import BlockAble
from base.suffer import SufferAble
from base.destry import DestroyAble
from view.boom import Boom

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



    def notifySuffer(self,attack):
        self.hp -= 1

    def needDestroy(self):
        if self.hp <= 0:
            self.shouldDestroy = True
            return self.shouldDestroy

    def showBoom(self):
        """
        是否显示爆炸的特效
        :return:
        """
        # 获取中心变量
        self.center_x = self.x + self.width / 2
        self.center_y = self.y + self.height / 2
        if self.shouldDestroy:
            return Boom(center_x=self.center_x,center_y=self.center_y,window=self.window)


