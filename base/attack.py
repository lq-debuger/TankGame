

class Attackable:
    """
    具有攻击的控件： 子弹
    方法： 对攻击和受攻击的控件进行碰撞检测   通知攻击控件攻击到了

    """
    def hasCollision(self,suffer):
        """
        进行碰撞检测
        :param suffer:受到伤害的控件
        :return:
        """

        pass

    def notifySuffer(self):
        """
        通知攻击控件攻击到了物体
        :return:
        """
        pass