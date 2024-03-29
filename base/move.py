from util.local import *
import pygame
from base.view import *

class MoveAble:
    """
    可以移动的控件: 我方坦克 和 敌方坦克 子弹
    功能：
        1.碰撞检测
        2.通知运动物和阻挡物
    """
    def hasCollision(self,block):

        # 记录当前的坐标
        x = self.x
        y = self.y

        # 预判下一步的轨迹
        # 预判下一步
        if self.direction == Direction.UP:
            y -= self.speed
        elif self.direction == Direction.DOWN:
            y += self.speed
        elif self.direction == Direction.LEFT:
            x -= self.speed
        elif self.direction == Direction.RIGHT:
            x += self.speed

        # 坦克矩形
        selfRect = pygame.Rect(x,y,self.width,self.height)
        # block矩形
        blockRect = pygame.Rect(block.x,block.y,block.width,block.height)


        # 同时对越界进行处理
        return selfRect.colliderect(blockRect) or x <0 or y<0 or x> WIDTH-self.width  or y> HEIGHT - self.height


    def notifyCollision(self):
        pass