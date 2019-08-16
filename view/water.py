from base.view import *
from base.block import BlockAble

class Water(Views,BlockAble):

    def __init__(self,**kwargs):
        super(Water, self).__init__(**kwargs,img='./img/water.gif')