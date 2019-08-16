from base.view import *
from util.local import *
# from util.utils import *


class Tank(Views):

    def __init__(self,**kwargs):
        self.direction = kwargs['direction']
        self.speed = 1
        self.images = [
            pygame.image.load('./img/p1tankL.gif'),
            pygame.image.load('./img/p1tankR.gif'),
            pygame.image.load('./img/p1tankU.gif'),
            pygame.image.load('./img/p1tankD.gif')
        ]
        super(Tank, self).__init__(**kwargs,img='./img/p1tankU.gif')
        self.image = self.images[self.direction.value]
        # 设置排序参数
        self.comKey = 1

    def display(self):
        self.image = self.images[self.direction.value]
        super(Tank, self).display()

    # 坦克移动
    def move(self,direction):

        if self.direction != direction:
            self.direction = direction
            return

        if direction == Direction.UP:
            self.y -= self.speed
        elif direction == Direction.DOWN:
            self.y += self.speed
        elif direction == Direction.LEFT:
            self.x -= self.speed
        elif direction == Direction.RIGHT:
            self.x += self.speed