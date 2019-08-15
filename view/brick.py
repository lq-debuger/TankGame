import pygame
from view.base import *

class Brick(Views):

    def __init__(self,**kwargs):
        super(Brick, self).__init__(**kwargs,img='./img/walls.gif')