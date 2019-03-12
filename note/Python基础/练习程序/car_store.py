# car_store.py
# 汽车租赁模拟程序
class Car: # 车辆类
    def __init__(self, car_id, name,
                  is_lend,price):
        self.car_id = car_id #车辆编号
        self.name = name #名称
        self.price = price #价格
        self.is_lend = is_lend #是否出租
        self.start_date = "" #起租日期
        self.end_date = "" #预计归还日期
        self.cust_id = "" #租车客户编号
    
    def __str__(self):
        ret = "车辆编号:%s,名称:%s,单价:%.2f," \
            "是否出租：%s" %(self.car_id,
            self.name, self.price,self.is_lend)
        return ret

class Customer: #客户类
    def __init__(self,cust_id,cust_name,tel_no):
        self.cust_id = cust_id       
        self.cust_name = cust_name        
        self.tel_no = tel_no

    def __str__(self):
        ret = "客户编号:%s,客户名称:%s,电话:%s" \
          %(self.cust_id, self.cust_name, self.tel_no) 

class CarStore: #租车店类
    def __init__(self):
        self.cars = [] #车辆列表
        self.customers = [] #客户列表
        self.__load_cars() #加载车辆列表
        self.__load_customers()#加载客户列表

    # def __load_cars(self): #加载车辆列表
    #     self.cars.append(Car("1","GOLF",400,"否")) 
    #     self.cars.append(Car("2","凯越",350,"否")) 
    #     self.cars.append(Car("3","奥迪",1200,"否")) 
    #     self.cars.append(Car("4","凯美瑞",800,"否")) 
    #     self.cars.append(Car("5","宝来",450,"否")) 

    def __load_cars(self): #加载车辆列表,从文件中读取
        with open("carlist.txt") as f:
            line = f.readline(256).replace("\n","")
            custinfo = line.split(",")
            car_id = custinfo[0]
            car_name = custinfo[1]
            price = float(custinfo[3])
            is_len = custinfo[2]
            car = Car(car_id,car_name,is_len,price)
            self.cars.append(car) #对象添加到列表

    def __load_customers(self):#加载客户列表
        cust1 = Customer("C0001","张大大","15811223344")
        cust2 = Customer("C0002","李小小","13233333444")
        cust3 = Customer("C0003","赵四","18044445555")
        self.customers.append(cust1) 
        self.customers.append(cust2) 
        self.customers.append(cust3) 

    def print_cars_info(self): #打印车辆信息
        for car in self.cars: #遍历车辆列表并打印
            print(car) 
    
    def find_car(self, car_id): #根据车辆编号查询
        for car in self.cars: #遍历车辆列表
            if car.car_id == car_id: #编号相等
                print(car)
                return
        print("未找到车辆信息")
        return
        
    def add_car(self, car): #添加车辆,car为Car的对象
        if isinstance(car, Car): #car是Car类的实例
            self.cars.append(car)
        else:
            print("对象类型有误")  
        #可以增加id号是否存在的逻辑判断
        return

    def del_car(self, car_id): #根据车辆编号删除
        for car in self.cars:
            if car.car_id == car_id:
                self.cars.remove(car) #删除对象
        return

    def lend(self, car_id, cust_id, 
            start_date, end_date): #租车
        for car in self.cars:
            if car.car_id == car_id:
                if car.is_lend == "是":#已出租
                    print("该车辆已经出租")
                    return
                else: #未出租
                    setattr(car, "is_lend", "是")#改状态
                    setattr(car, "cust_id", cust_id)
                    setattr(car, "start_date", start_date)
                    setattr(car, "end_date", end_date)
                    print("车辆出租登记完成")
                    return
        print("未找到车辆信息")
        return
    
    def back(self, car_id): #还车
        for car in self.cars:
            if car.car_id == car_id:
                setattr(car, "is_lend", "否")#改状态
                setattr(car, "cust_id", "")
                setattr(car, "start_date", "")
                setattr(car, "end_date", "")
                print("还车登记完成")
                return
        print("未找到该车辆信息")
        return

if __name__ == "__main__":
    car_store = CarStore()  #实例化租车店对象
    car_store.print_cars_info() #打印车辆信息
    print("")
    #租车方法测试
    car_store.lend("3","C0001","2018-01-01","2018-01-03")
    car_store.print_cars_info()

    #还车方法测试
    car_store.back("3")
    car_store.print_cars_info()
    
     #添加车辆方法测试
    #car_store.find_car("3") #查找编号为3的车辆

    # car = Car("6","捷达",300,"否")
    # car_store.add_car(car)  #将car对象添加到cars列表
    # car_store.print_cars_info()