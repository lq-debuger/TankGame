import pygame
from base.view import Views
from base.autoMove import AutoMove
from util.local import *
from base.autoMove import AutoMove
from base.move import MoveAble

class EnemyTank(Views,AutoMove,MoveAble):
    """
    敌方坦克类
    """
    def __init__(self,**kwargs):
        self.direction = kwargs['direction']
        self.speed = 1
        self.images = [
            pygame.image.load('./img/p2tankL.gif'),
            pygame.image.load('./img/p2tankR.gif'),
            pygame.image.load('./img/p2tankU.gif'),
            pygame.image.load('./img/p2tankD.gif')
        ]
        super(EnemyTank, self).__init__(**kwargs,img='./img/p1tankD.gif')
        self.speed = 0.3
        self.image = self.images[self.direction.value]
        # 设置排序参数
        self.comKey = 1
        # 设置碰撞参数
        self.coll = False
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def autoMove(self):

        if self.coll :
            return 

        if self.direction == Direction.LEFT:
            self.x -= self.speed
        elif self.direction == Direction.RIGHT:
            self.x += self.speed
        elif self.direction == Direction.UP:
            self.y -= self.speed
        elif self.direction == Direction.DOWN:
            self.y += self.speed

    def notifyCollision(self):
        self.coll =True

