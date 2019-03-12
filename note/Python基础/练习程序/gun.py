#枪械类

class Gun:
    # def __init__(self,name,max,bullet,des,firing):
    #     self.name=name
    #     self.max=max   #弹夹容量
    #     self.bullet=bullet
    #     self.des=des   #杀伤力
    #     self.firing=firing  #每次开火打出的子弹数

    def reload(self):  #填弹
        #填弹后,剩余子弹数等于弹夹容量
        self.bullet=self.max
        print('完成填弹')
        
    def fire(self):   #开火
        if self.bullet<=0:
            print('请填弹')
            return

        if self.bullet>=self.firing:
            self.bullet-=self.firing  #打出三发子弹

        else:
            self.bullet=0   #子弹全部打出

        #计算杀伤力
        d=int(self.des*100)
        #模拟声音
        s='哒'*self.firing
        print('%s,%s杀伤力%d,剩余子弹%d'%(s,self.name,d,self.bullet))
