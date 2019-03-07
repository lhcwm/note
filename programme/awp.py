#awp
#狙击枪
from gun import*
class Awp(Gun):
    def __init__(self):
        self.name='AWP'
        self.max=10   #弹夹容量
        self.bullet=0
        self.des=1  #杀伤力
        self.firing=1  #每次开火打出的子弹数

    def open(self):  #打开瞄准镜
        print('瞄准镜已打开')

    def close(self):   #关闭瞄准镜
        print('瞄准镜已关闭')