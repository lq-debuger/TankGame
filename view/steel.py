from base.view import *
from base.block import BlockAble
from base.suffer import SufferAble

class Steel(Views,BlockAble,SufferAble):

    def __init__(self,**kwargs):
        super(Steel, self).__init__(**kwargs,img='./img/steels.gif')