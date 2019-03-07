#鸵鸟类

from bird import *
class Ostrich(Bird):
    def fly(self):
        print('%s快速的奔跑起来'%self.name)