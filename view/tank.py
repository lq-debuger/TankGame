import pygame
from view.base import *

class Tank(Views):

    def __init__(self,**kwargs):
        super(Tank, self).__init__(**kwargs,img='./img/p1tankU.gif')