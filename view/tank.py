from base.view import *
from util.local import *
# from util.utils import *
from base.move import MoveAble
import pygame


class Tank(Views,MoveAble):

    def __init__(self,**kwargs):
        self.direction = kwargs['direction']
        self.speed = 1
        self.images = [
            pygame.image.load('./img/p1tankL.gif'),
            pygame.image.load('./img/p1tankR.gif'),
            pygame.image.load('./img/p1tankU.gif'),
            pygame.image.load('./img/p1tankD.gif')
        ]
        super(Tank, self).__init__(**kwargs,img='./img/p1tankU.gif')
        self.image = self.images[self.direction.value]
        # 设置排序参数
        self.comKey = 1
        # 设置碰撞参数
        self.coll = False

    def display(self):
        self.image = self.images[self.direction.value]
        super(Tank, self).display()

    # 坦克移动
    def move(self,direction):

        if self.direction != direction:
            self.direction = direction
            return

        if self.coll :
            self.coll = False
            return


        if direction == Direction.UP:
            self.y -= self.speed
        elif direction == Direction.DOWN:
            self.y += self.speed
        elif direction == Direction.LEFT:
            self.x -= self.speed
        elif direction == Direction.RIGHT:
            self.x += self.speed

    # # 碰撞检测
    # def hasCollision(self, block):
    #     tankRect = pygame.Rect(self.x,self.y,SIZE,SIZE)
    #     blockRect = pygame.Rect(block.x,block.y,SIZE,SIZE)
    #
    #     return tankRect.colliderect(blockRect)

    def notifyCollision(self):
        self.coll =True