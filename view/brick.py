from base.view import *
from base.block import BlockAble
from base.suffer import SufferAble

class Brick(Views,BlockAble,SufferAble):

    def __init__(self,**kwargs):
        super(Brick, self).__init__(**kwargs,img='./img/walls.gif')
        # 设置血量值
        self.hp = 3

    def notifySuffer(self):
        self.hp -= 1