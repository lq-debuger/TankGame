import pygame
from view.base import *

class Steel(Views):

    def __init__(self,**kwargs):
        super(Steel, self).__init__(**kwargs,img='./img/steels.gif')