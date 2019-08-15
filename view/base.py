# 创建一个父类，让坦克、草、砖、水、铁继承此类

class Views:
    """
    属性： x,y  ,image , window
    方法： 显示display
    """
    def __init__(self,x,y,window):
        self.x = x
