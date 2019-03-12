# 自定义迭代器
# class Myiter:
#     def __init__(self,lst):
#         self.data=lst   #lst是列表
#         self.index=0    #计数器

#     def __iter__(self):
#         return Myiter(self.data)

#     def __next__(self):
#         return

# if __name__=='__main__':
#     m=Myiter([1,2,3])
#     for x in m:
#         print (x,end=' ')

#运算符重载
class Truck:
    def __init__(self,load):
        self.load=load  #载重

    def __add__(self,value):
        return Truck(self.load+value)

    def __radd__(self,value):
        return Truck(self.load+value)

    def __iadd__(self,value):
        return Truck(self.load+value)

    def __str__(self):
        return 'load:%d'%self.load

    def __mul__(self,value):
        # return Truck(self.load*value)
        return self.load*value

    def __gt__(self,o):
        return (self.load>o.load)

    def __lt__(self):
        return (self.load<o.load)

if __name__=='__main__':
    t=Truck(20)
    t2=t+1
    print(t2)
    t3=3+t
    print(t3)
    t+=2
    print(t)
    print(t2>t3))