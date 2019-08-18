# 创建一个父类，让坦克、草、砖、水、铁继承此类
import pygame

from enum import Enum

class TankType(Enum):
    User = 0
    Enemy = 1
    Other = 2


class Views:
    """
    属性： x,y  ,image , window
    方法： 显示display
    """
    def __init__(self,**kwargs):
        # 设置排序参数
        self.comKey = 2
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.window = kwargs['window']
        self.image = pygame.image.load(kwargs['img'])
        self.type = TankType.Other

    def display(self):
        self.window.blit(self.image,(self.x,self.y))