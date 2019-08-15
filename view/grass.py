import pygame
from view.base import *

class Grass(Views):

    def __init__(self,**kwargs):
        super(Grass, self).__init__(**kwargs,img='./img/grass.png')