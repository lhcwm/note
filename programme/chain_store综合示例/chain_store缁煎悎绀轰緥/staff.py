# staff.py
# 员工类，演示__slots__属性示例
class Staff:
    "这是一个员工类"
    __slots__ = ["no", "name", "position"]

    def __init__(self, no, name, position):
        self.no = no #员工编号
        self.name = name #员工姓名
        self.position = position #职位
        #self.salary = 8000  #不允许

    def __str__(self):
        ret = "编号:%s, 姓名:%s, 职位:%s" %\
          (self.no, self.name, self.position)
        return ret

    def work(self): #员工工作方法
        print("%s正在工作" % self.name)

#定义机器人类，继承自Staff类
class ServiceRobot(Staff): 
    def __init__(self, no, name, position):
        super().__init__(no, name, position)

    def work(self):  #重写工作方法
        print("%s的工作，扫地" % self.name)

if __name__ == "__main__":
    staff = Staff("0001", "Jerry", "经理")
    #如果没有__slots__属性，则创建一个新属性
    #执行不会报错，但没有起到给属性赋值的作用
    #staff.positino = "副总经理"  
    print(staff)

    robot = ServiceRobot("0002","多啦A梦","服务员")
    print(robot)
    robot.work()  