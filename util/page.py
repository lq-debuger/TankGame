import pygame
from util.local import *
import sys

def page1():
    # 初始化游戏界面
    pygame.init()
    # 创建游戏窗口
    window = pygame.display.set_mode((WIDTH, 13 * SIZE))
    # 设置标题
    pygame.display.set_caption("坦克大战")
    # 加载游戏图标
    ico = pygame.image.load('./img/camp.gif')
    pygame.display.set_icon(ico)

    # 创建标题字体
    font1 = pygame.font.Font('./font/happy.ttf', 100)
    text1 = font1.render('坦克大战',True,(255,0,0))
    # 创建选项字体
    font1 = pygame.font.Font('./font/happy.ttf', 40)
    text2 = font1.render('1.单人游戏', True, (0, 255, 0))
    text3 = font1.render('2.双人游戏(暂无)', True, (0, 255, 0))

    while True:

        eventList = pygame.event.get()
        for eventEle in eventList:
            if eventEle.type == QUIT:
                # 退出游戏
                pygame.quit()
                # 退出程序
                sys.exit()

        window.blit(text1,(200,150))
        window.blit(text2,(300,350))
        window.blit(text3,(300,450))
        pygame.display.flip()

if __name__ == '__main__':
    page1()