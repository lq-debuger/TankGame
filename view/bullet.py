from base.view import *
import pygame
from util.local import *
from base.autoMove import AutoMove

class Bullet(Views,AutoMove):
    """
    子弹类
    """
    def __init__(self,**kwargs):
        
        self.window = kwargs['window']
        self.image = pygame.image.load('./img/tankmissile.gif')
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # 设置速度属性
        self.speed = 2

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