import time
import random
import pygame
from base.view import Views, TankType
from base.autoMove import AutoMove
from util.local import *
from base.autoMove import AutoMove
from base.move import MoveAble
from base.autofire import AutoFire
from view.bullet import Bullet
from util.local import *
from base.destry import DestroyAble
from base.suffer import SufferAble
from view.boom import Boom
from base.move import MoveAble
from base.block import BlockAble
from enum import Enum


# class Loc(Enum):
#     LOC1 = 0
#     LOC2 = 1
#     LOC3 = 2
#     LOC4 = 3


class EnemyTank(Views,AutoMove,MoveAble,AutoFire,DestroyAble,SufferAble,BlockAble):
    """
    敌方坦克类
    """
    def __init__(self,**kwargs):
        self.direction = kwargs['direction']
        self.speed = 0.5
        self.images = [
            pygame.image.load('./img/p2tankL.gif'),
            pygame.image.load('./img/p2tankR.gif'),
            pygame.image.load('./img/p2tankU.gif'),
            pygame.image.load('./img/p2tankD.gif')
        ]
        # super(EnemyTank, self).__init__(**kwargs,img='./img/p1tankD.gif')
        self.image = pygame.image.load('./img/p1tankD.gif')
        self.window = kwargs['window']

        self.speed = 1
        self.image = self.images[self.direction.value]

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x = kwargs['x']
        self.y = kwargs['y']

        # 设置当前类别
        self.type = TankType.Enemy


        # 设置敌机的血量
        self.hp = 3
        # 设置销毁属性
        self.shouldDestroy = False
        # 设置排序参数
        self.comKey = 1
        # 发射子弹的时间间隔
        self.time = time.time()
        # 设置碰撞参数
        self.coll = False
        # 设置碰撞属性
        self.coll = False
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    # def display(self):
    #     self.image = self.image[self.direction.value]
    #     super(EnemyTank, self).display(self.image,(self.x,self,y))

    def randDirection(self,direction):
        """
        随机碰撞后的方向
        :return:
        """
        index = random.randint(0,3)
        if index == 0:
            newDirection = Direction.LEFT
        elif index == 1:
            newDirection = Direction.RIGHT
        elif index == 2:
            newDirection = Direction.UP
        elif index == 3:
            newDirection = Direction.DOWN

        if self.direction == newDirection:
            return self.randDirection(direction)
        else:
            return newDirection


    def autoMove(self):
        # 如果发生了碰撞，就随机改变方向
        if self.coll :
            self.coll = False
            self.direction = self.randDirection(self.direction)
            return

        if self.direction == Direction.LEFT:
            self.x -= self.speed
        elif self.direction == Direction.RIGHT:
            self.x += self.speed
        elif self.direction == Direction.UP:
            self.y -= self.speed
        elif self.direction == Direction.DOWN:
            self.y += self.speed

    def display(self):
        self.image = self.images[self.direction.value]
        self.window.blit(self.image,(self.x,self.y))

    def notifyCollision(self):
        self.coll =True

    def autoFire(self):
        """
        控制发射频率 一秒一次
        :return:
        """
        curtime = time.time()
        offset = curtime - self.time
        #
        if offset > 1:
            self.time = curtime

            return Bullet(type=self.type, tank_x=self.x,tank_y=self.y,tank_height=self.height,tank_width=self.width,direction=self.direction,window=self.window,owner=2)

    def notifySuffer(self,attack):
        if not isinstance(attack.owner,EnemyTank):
            self.hp -= 1


    def needDestroy(self):
        if self.hp <= 0:
            self.shouldDestroy = True
            return  self.shouldDestroy

    def showBoom(self):
        """
        是否显示爆炸的特效
        :return:
        """
        # 获取中心变量
        self.center_x = self.x + self.width / 2
        self.center_y = self.y + self.height / 2
        if self.shouldDestroy:
            return Boom(center_x=self.center_x, center_y=self.center_y, window=self.window)

    def notifyCollision(self):
        self.coll = True

    # 死后重置，不进行销毁
    def reset(self,enemyList,views):
        l = random.randint(0,2)
        if l == 0:
            self.x = 0
            self.y = 0
        elif l == 1:
            self.x = 6* SIZE
            self.y = 0
        elif l == 2:
            self.x = 13 * SIZE
            self.y = 0
        for enemy in enemyList:
            if enemy.x == self.x and enemy.y == self.y:
                self.reset(enemyList)
        return views.append(EnemyTank(x=self.x, y=self.y, window=self.window,direction=Direction.DOWN))


