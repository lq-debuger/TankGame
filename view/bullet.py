from base.view import *
import pygame
from util.local import *
from base.autoMove import AutoMove
# from base.move import MoveAble
# from base.destry import DestroyAble
from base.destry import DestroyAble
from base.attack import Attackable
from view.boom import Boom
from base.suffer import SufferAble
# from base.block import BlockAble

class Bullet(Views,AutoMove,DestroyAble,Attackable,SufferAble):
    """
    子弹类
    """
    def __init__(self,**kwargs):
        
        self.window = kwargs['window']
        self.image = pygame.image.load('..'
                                       '/img/tankmissile.gif')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.type = kwargs['type']

        # 设置拥有者属性
        self.owner =0

        # 设置速度属性
        self.speed =3

        # 设置销毁属性
        self.shouldDestroy =False

        self.comKey = 2


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

        if self.type == suffer.type:
            return
        # if self.owner==1:
        #     return False
        # 子弹矩形
        bulletRect = pygame.Rect(self.x,self.y,self.width,self.height)
        # block矩形
        sufferRect = pygame.Rect(suffer.x,suffer.y,suffer.width,suffer.height)

        # 同时对越界进行处理
        return bulletRect.colliderect(sufferRect)
        # if a:
        #     print(sufferRect)
        #     print(bulletRect)
        # return a



    def needDestroy(self):
        # 子弹越界
        return  self.x <0 or self.y<0 or self.x> WIDTH  or self.y> HEIGHT  or self.shouldDestroy

    def notifyAttack(self,suffer,attack):
        # 加载hit音效
        if attack.type == TankType.User:

            hit_snd = pygame.mixer.Sound('../snd/hit.wav')
            hit_snd.play(0)
        # if not isinstance(self.owner,Tank):
        # if self.owner != suffer or (isinstance(suffer,Bullet) and type(self.owner)!=type(suffer.owner)):
        self.shouldDestroy = True

    # 如果是敌我子弹的话就抵消
    def notifySuffer(self,attack):
        if attack.owner != self.owner:
            self.shouldDestroy = True


    def showBoom(self):
        pass