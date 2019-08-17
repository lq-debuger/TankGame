from base.view import *
import pygame
from util.local import *
from base.autoMove import AutoMove
# from base.move import MoveAble
# from base.destry import DestroyAble
from base.destry import DestroyAble
from base.attack import Attackable
from view.boom import Boom

class Bullet(Views,AutoMove,DestroyAble,Attackable):
    """
    子弹类
    """
    def __init__(self,**kwargs):
        
        self.window = kwargs['window']
        self.image = pygame.image.load('./img/tankmissile.gif')
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # 设置拥有者属性
        self.owner = kwargs['owner']

        # 设置速度属性
        self.speed =1.5

        # 设置销毁属性
        self.shouldDestroy =False


        # 获取方向属性
        self.direction  = kwargs['direction']

        tank_x = kwargs['tank_x']
        tank_y = kwargs['tank_y']
        tank_width = kwargs['tank_width']
        tank_height = kwargs['tank_height']

        # 设置坐标
        if self.direction == Direction.LEFT:
            self.x = tank_x-self.width
            self.y = tank_y + tank_height/2 - self.height/2
        elif self.direction == Direction.RIGHT:
            self.x = tank_x + tank_width
            self.y = tank_y + tank_height / 2 - self.height / 2
        elif self.direction == Direction.UP:
            self.x = tank_x + tank_width/2 -self.width/2
            self.y = tank_y - self.height
        elif self.direction == Direction.DOWN:
            self.x = tank_x + tank_width/2 -self.width/2
            self.y = tank_y + tank_height

    # 自动移动
    def autoMove(self):


        if self.direction == Direction.LEFT:
            self.x -= self.speed
        elif self.direction == Direction.RIGHT:
            self.x += self.speed
        elif self.direction == Direction.UP:
            self.y -= self.speed
        elif self.direction == Direction.DOWN:
            self.y += self.speed

    # 进行碰撞处理和越界
    def hasCollision(self,suffer):
        # 子弹矩形
        bulletRect = pygame.Rect(self.x,self.y,self.width,self.height)
        # block矩形
        sufferRect = pygame.Rect(suffer.x,suffer.y,suffer.width,suffer.height)

        # 同时对越界进行处理
        return bulletRect.colliderect(sufferRect)


    def needDestroy(self):
        # 子弹越界
        return  self.x <0 or self.y<0 or self.x> WIDTH  or self.y> HEIGHT  or self.shouldDestroy

    def notifySuffer(self):
        self.shouldDestroy = True

    def showBoom(self):
        pass