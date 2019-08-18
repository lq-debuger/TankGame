import pygame

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


def gameOver(tank,home):
    if tank.hp <= 0 or home.hp <= 0 :
        return True
    return False


def restart():
    # 创建应用程序
    app = QApplication(sys.argv)
    # # 创建窗口控件
    widget = QWidget()
    # # 设置窗口大小
    # widget.resize(,)
    # # 设置窗口标题
    # widget.setWindowTitle("")
    # # 展示窗口
    btn = QPushButton('重新开始')
    btn.setParent(widget)
    widget.show()
    # 退出应用程序
    sys.exit(app.exec_())

