from base.view import *
from util.local import *
# from util.utils import *
from base.move import MoveAble
import pygame
from view.bullet import *
from base.suffer import SufferAble
from base.destry import DestroyAble
from base.block import BlockAble

class Tank(Views,MoveAble,SufferAble,DestroyAble,BlockAble):

    def __init__(self,**kwargs):
        self.direction = kwargs['direction']
        self.speed = 10
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
        # 设置血量
        self.hp = 20
        # 设置销毁参数
        self.shouldDestroy = False
        # 设置碰撞参数
        self.coll = False
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # 设置当前类别
        self.type = TankType.User

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

    # 发射子弹
    def fire(self,views):
        # 创建子弹对象
        views.append(Bullet(type=self.type,tank_x=self.x,tank_y=self.y,tank_height=self.height,tank_width=self.width,direction=self.direction,window=self.window,owner=1))
        print("发生了")
    def notifySuffer(self,attack):
        if not isinstance(attack.owner,Tank):
            self.hp -= 1

    def needDestroy(self):
        if self.hp <= 0 :
            self.shouldDestroy = True
            return self.shouldDestroy

    def showDestroy(self):
        pass

    def showBoom(self):
        pass
