import pygame
from view.base import *

class Water(Views):

    def __init__(self,**kwargs):
        super(Water, self).__init__(**kwargs,img='./img/water.gif')