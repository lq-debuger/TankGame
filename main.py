import pygame
from pygame.locals import *
import sys
from util.local import *
# from view.tank import *
# from view.brick import *
# from view.grass import *
# from view.water import *
# from view.steel import *
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

# 获取坦克
tank = list(filter(lambda view:isinstance(view,Tank),views))[0]

while True:

    # 清屏
    window.fill((0,0,0))
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

    # 捕获键盘按压列表
    pressList = pygame.key.get_pressed()
    if 1 in pressList:
        if pressList[K_w] == 1:
            tank.move(Direction.UP)
        elif pressList[K_s] == 1:
            tank.move(Direction.DOWN)
        elif pressList[K_a] == 1:
            tank.move(Direction.LEFT)
        elif pressList[K_d] == 1:
            tank.move(Direction.RIGHT)