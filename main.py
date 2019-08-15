import pygame
from pygame.locals import *
import sys
from util.local import *
from view.tank import *
from view.brick import *
from view.grass import *
from view.water import *
from view.steel import *
from util.utils import *

# 初始化游戏界面
pygame.init()
# 创建游戏窗口
window = pygame.display.set_mode((13*SIZE,13*SIZE))
# 设置标题
pygame.display.set_caption("坦克大战")
# 加载游戏图标
ico = pygame.image.load('./img/camp.gif')
pygame.display.set_icon(ico)

# 创建地图图片控件
views = []
# 创建地图
Map(views,window)

while True:

    # 显示地图
    for ele in views:
        ele.display()

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