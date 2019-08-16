from pygame.locals import *
from enum import Enum

SIZE = 60
WIDTH = 13*60
HEIGHT = 13*60

class Direction(Enum):
    LEFT  = 0
    RIGHT = 1
    UP = 2
    DOWN = 3