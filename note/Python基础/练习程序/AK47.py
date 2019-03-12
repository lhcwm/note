#AK47
from gun import*
class AK(Gun):
    def __init__(self):
        self.name='AK47'
        self.max=30   #弹夹容量
        self.bullet=0
        self.des=0.4  #杀伤力
        self.firing=3  #每次开火打出的子弹数
