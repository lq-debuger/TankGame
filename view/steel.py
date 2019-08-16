from base.view import *
from base.block import BlockAble

class Steel(Views,BlockAble):

    def __init__(self,**kwargs):
        super(Steel, self).__init__(**kwargs,img='./img/steels.gif')