from base.view import *
from base.block import BlockAble

class Brick(Views,BlockAble):

    def __init__(self,**kwargs):
        super(Brick, self).__init__(**kwargs,img='./img/walls.gif')