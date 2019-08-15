import pygame
from pygame.locals import *
import sys
from util.local import *
from view.tank import *
from view.brick import *
from view.grass import *
from view.water import *
from view.steel import *

# 初始化游戏界面
pygame.init()
# 创建游戏窗口
window = pygame.display.set_mode((13*SIZE,13*SIZE))
# 设置标题
pygame.display.set_caption("坦克大战")
# 加载游戏图标
ico = pygame.image.load('./img/camp.gif')
pygame.display.set_icon(ico)

# 创建对象
tank = Tank(x=60,y=60,window=window)
grass =Grass(x=100,y=100,window=window)
water = Water(x=150,y=150,window=window)
brick = Brick(x=200,y=200,window=window)
steel = Steel(x=250,y=250,window=window)



while True:

    # 显示图片
    tank.display()
    grass.display()
    water.display()
    brick.display()
    steel.display()

    # 刷新界面
    pygame.display.flip()


    # 捕获事件
    eventList = pygame.event.get()
    for eventEle in eventList:
        if eventEle.type == QUIT:
            # 退出游戏
            pygame.quit()
            # 退出程序
            sys.exit()