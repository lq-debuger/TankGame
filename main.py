import pygame
from pygame.locals import *
import sys
from util.local import *

# 初始化游戏界面
pygame.init()
# 创建游戏窗口
window = pygame.display.set_mode((13*SIZE,13*SIZE))



while True:

    # 捕获事件
    eventList = pygame.event.get()
    for eventEle in eventList:
        if eventEle.type == QUIT:
            # 退出游戏
            pygame.quit()
            # 退出程序
            sys.exit()