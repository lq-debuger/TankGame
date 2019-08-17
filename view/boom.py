from base.view import Views
from base.destry import DestroyAble
import pygame


class Boom(Views,DestroyAble):
    """
    挂掉的特效
    """
    def __init__(self,**kwargs):

        # 照片的索引
        self.index = 1
        # 总共照片的数量
        self.total = 32
        center_x = kwargs['center_x']
        center_y = kwargs['center_y']
        self.image = pygame.image.load('./img/blast_{}.png'.format(self.index))
        self.wiidth = self.image.get_width()
        self.height = self.image.get_height()

        self.x =center_x - self.wiidth/2
        self.y = center_y - self.height/2

        self.window = kwargs['window']

    def display(self):
        self.image = pygame.image.load('./img/blast_{}.png'.format(self.index))
        super(Boom, self).display()

        if self.index < self.total:
            self.index += 1

    def needDestroy(self):
        if self.index == self.total:
            return
