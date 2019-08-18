from base.view import Views
import pygame
from base.block import BlockAble
from base.suffer import SufferAble
from base.destry import DestroyAble

class Home(Views,BlockAble,SufferAble,DestroyAble):
    """
    己方老巢
    """
    def __init__(self,**kwargs):
        super(Home, self).__init__(**kwargs,img='../img/camp.gif')
        self.image = pygame.image.load('../img/camp.gif')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hp = 15
        self.shouldDestroy = False

    def notifySuffer(self,attack):
        self.hp -= 1

    def needDestroy(self):
        if self.hp <= 0:
            self.shouldDestroy =True
            # continue
            return self.shouldDestroy

    # def showDestroy(self):
    #     pass

