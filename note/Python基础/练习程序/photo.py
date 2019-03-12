# 手机类

class Photo:
    def __init__(self,name,price,CPU,screen):
        self.name=name
        self.price=price   #价格
        self.CPU=CPU       #CPU
        self.screen=screen  #屏幕尺寸

    def start(self):    #手机开机
        print('%s开机了'%self.name)

    def shutdown(self):   #手机关机
        print('%s关机了'%self.name)

    def call(self,who):     #手机打电话
        print('用%s给%s打了个电话'%(self.name,who))

    def send(self):     #手机发短信
        print('用%s发了个短信'%self.name)

    def __del__(self):
        print('调用析构函数')


if __name__ == '__main__':
    p=Photo('华为',1000,3.0,6)
    p.start()
    p.call('小王')
    p.send()
    p.shutdown()
    del p
    print('程序退出')

