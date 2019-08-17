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
from base.move import MoveAble
from base.block import BlockAble
from base.autoMove import AutoMove
from base.destry import DestroyAble
from base.suffer import SufferAble
from base.attack import Attackable
from view.boom import Boom
from base.autofire import AutoFire

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

    # 获取可自动开火的控件
    autofireList = list(filter(lambda view:isinstance(view,AutoFire),views))
    for autofire in autofireList:
        bullet = autofire.autoFire()
        if bullet:
            views.append(bullet)

    # 获取可以攻击的控件
    attackList = list(filter(lambda view:isinstance(view,Attackable),views))
    # 获取遭受攻击的控件
    sufferList = list(filter(lambda view:isinstance(view,SufferAble),views))
    # 判断是否受到攻击
    for attack in attackList:
        for suffer in sufferList:
            # 检测是否发生碰撞
            coll = attack.hasCollision(suffer)
            if coll :
                attack.notifySuffer()
                suffer.notifySuffer(attack)
                break

    # 获取所有可以进行销毁的控件
    destroyList = list(filter(lambda view:isinstance(view,DestroyAble),views))
    # 判断是否要进行摧毁
    for destroyView in destroyList:
        if destroyView.needDestroy():
            # 判断是都需要挂掉的特效
            show = destroyView.showBoom()
            if show:
                views.append(show)
            views.remove(destroyView)
            del destroyView

    # 检测所有自动移动的控件
    autoList = list(filter(lambda view:isinstance(view,AutoMove),views))
    for auto in autoList:
        auto.autoMove()

    # 获取可移动控件
    moveList = list(filter(lambda view:isinstance(view,MoveAble),views))
    # 获取可阻挡控件
    blockList = list(filter(lambda view:isinstance(view,BlockAble),views))
    # 检测移动控件和阻挡控件是否发生了碰撞
    for move in moveList:
        for block in blockList:
            if move == block:
                continue
            colResult = move.hasCollision(block)
            if colResult:
                move.notifyCollision()
                break

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
        # 按enter键发射子弹
        elif eventEle.type == KEYDOWN:
            if eventEle.key == K_RETURN:
                tank.fire(views)

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
