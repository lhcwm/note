# carstore2.py
# 老师版

class Car:
    def __init__(self,car_id,name,price,is_lend):
        self.car_id=car_id
        self.name=name
        self.price=price
        self.is_lend=is_lend
        self.star_date=0
        self.end_date=0
        self.cus_id=0   #租车客户编号

    def __str__(self):
        ret='车辆编号:%s,名称:%s,单价:%.2f,是否出租:%s'%(self.car_id,self.name,self.price,self.is_lend)
        return ret

class Customer:
    def __init__(self,cust_id,cust_name,tel_no):    
        self.cust_id=cust_id
        self.cust_name=cust_name
        self.tel_no=tel_no

    def __str__(self):
        ret='客户编号:%s,客户名称:%s,电话:%s'%(self.cust_id,self.cust_name,self.tel_no)
        return ret

class Carstore:#租车店类
    def __init__(self):
        self.cars=[] #车辆列表
        self.customers=[] #客户列表
        self.__load_cars()  #加载车辆列表
        self.__load_customers()  #加载客户列表

    def __load_cars(self):  #加载车辆列表
        self.cars.append(Car('1','golf',400,'否'))
        self.cars.append(Car('2','凯越',350,'否'))
        self.cars.append(Car('3','奥迪',1200,'否'))
        self.cars.append(Car('4','凯美瑞',800,'否'))
        self.cars.append(Car('5','宝来',450,'否'))

    def __load_customers(self):  #加载客户列表
        self.customers.append(Customer('C0001','张三','12333445566'))
        self.customers.append(Customer('C0002','李四','15533445588'))
        self.customers.append(Customer('C0003','王五','16633445522'))

    def print_info(self):
        for car in self.cars: #遍历车辆列表并打印
            print(car)

    def find_car(self,car_id):
        for car in self.cars:
            if car.car_id==car_id:
                print(car)
                return
        print('未找到车辆信息')
        return

    def add_car(self,name):
        if isinstance(name,Car):
            self.cars.append(name)
        else:
            print('对象类型有误')
        return

    def del_car(self,car_id):
        for car in self.cars:
            if car.car_id==car_id:
                self.cars.remove(car)
        return

if __name__=='__main__':
    cs=Carstore()  #实例化租车店对象
    cs.print_info()
    print()
    cs.find_car('3')
    print()
    cs.add_car(Car('6','宝马',500,'否'))
    cs.print_info()
