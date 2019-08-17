from util.local import *
from view.tank import Tank
from view.grass import Grass
from view.steel import Steel
from view.brick import Brick
from view.water import Water
from view.enemyTank import EnemyTank



def Map(views,window):
    # 解析地图
    f = open('./map/1.map', encoding='utf-8')
    fileList = f.readlines()
    for row in range(0, len(fileList)):
        for line in range(0, len(fileList)):
            if fileList[row][line] == '主':
                views.append(Tank(x=SIZE * line, y=SIZE * row, window=window,direction = Direction.UP))
            elif fileList[row][line] == '草':
                views.append(Grass(x=SIZE * line, y=SIZE * row, window=window))
            elif fileList[row][line] == '水':
                views.append(Water(x=SIZE * line, y=SIZE * row, window=window))
            elif fileList[row][line] == '铁':
                views.append(Steel(x=SIZE * line, y=SIZE * row, window=window))
            elif fileList[row][line] == '砖':
                views.append(Brick(x=SIZE * line, y=SIZE * row, window=window))
            elif fileList[row][line] == '敌':
                views.append(EnemyTank(x=SIZE * line, y=SIZE * row, window=window,direction=Direction.DOWN))
    # 对views进行排序，以便能够使坦克隐藏在草丛
    views.sort(key=lambda view:view.comKey)