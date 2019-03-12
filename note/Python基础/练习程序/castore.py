# car类:
#     属性:
#     car_id  车辆ID号
#     name  车辆名称
#     is_lend 是否出租
#     price 每天单价
#     start_date  起租日期
#     end_date   租赁终止日期
  
#   方法:
#     __str__()

class car:
    def __init__(self):
        self.car_id=''
        self.name=''
        self.is_lend=''
        self.price=''
        self.start_date=''
        self.end_date=''

    def __str__(self):
        pass

# customer类:
#    属性
#    cust_id   客户编号
#    cust_name 客户姓名
#    tel_no    客户电话
#   方法:
#    __str__()

class customer:
    def __init__(self,cust_id,cust_name,tel_no):
        self.cust_id=cust_id
        self.cust_name=cust_name
        self.tel_no=tel_no

    def __str__(self):
        pass

# car_store类:
#    属性:
#     cars   所有车辆列表
#     customer 所有客户列表
#     方法:
#     __load_cars()   加载所有车辆列表
#     __load_costomer() 加载所有客户列表
#     print_cars_info(0 打印所有车辆信息
#     find_cars()       查找车辆
#     add_car()    添加车辆
#     del_car     删除车辆
#     lend()   租车
#     back()   还车

class car_store(car,customer):
    def __init__(self):
        super().__init__()
        self.cars=self.__load_cars()

    def __load_cars(self):
        '''从文件读取信息的函数'''
        # with open('carlist.txt') as f:
        # while 1:
        #     line=f.readline(2560).replace('\n','')
        #     if not line:
        #         break
        #     cars=line.split(',')
        #     ID=cars[0]
        #     name=cars[1]
        #     is_lend=cars[2]
        #     price=cars[3]
        #     start_date=cars[4]
        #     end_date=cars[5]
        #     y=('ID','name','is_lend','price','start_date','end_date')
        #     z=(ID,name,is_lend,price,start_date,end_date)
        #     d=dict(zip(y,z))
        #     self.cars.append(d)
        try:
            f=open('carlist.txt')
        except OSError:
            print('输入的文件名有误')
            return
        y=('ID','name','is_lend','price','start_date','end_date')
        l=[]
        try:
            while 1:
                x=f.readline()
                if not x:
                    break
                x=x.replace('\n','')
                z=x.split(',')
                d=dict(zip(y,z))
                l.append(d)
        finally:
            f.close()
        print('车辆信息导入成功')
        return l

    # def __load_costomer(self):

    def print_cars_info(self,s=None):
        if s==None:
            s=self.cars
        def chinese_char_count(s):
            l=[]
            for n in s:
                for a in n['name']:
                    k=len(n['name'])
                    if 0x4E00<=ord(a)<=0x9FA5:
                        k+=1
                    l+=[k]
            return max(l)
        k=chinese_char_count(s)
        print('+'+('-'*(4))+'+'+('-'*(k+6))+'+'+('-'*(10))+'+'+('-'*(8))+'+'+('-'*(16))+'+'+('-'*(16))+'+')
        print('|'+'ID'.center(4)+'|'+'车辆名称'.center(k+2)+'|'+'是否已出租'.center(4)+'|'
              +'单价'.center(6)+'|'+'起租日期'.center(12)+'|'+'止租日期'.center(12)+'|')
        print('+'+('-'*(4))+'+'+('-'*(k+6))+'+'+('-'*(10))+'+'+('-'*(8))+'+'+('-'*(16))+'+'+('-'*(16))+'+')
        for x in s:
            m=0
            for a in x['name']:
                if 0x4E00<=ord(a)<=0x9FA5:
                    m+=1
            print('|'+str(x['ID']).center(4)+'|'+x['name'].center((k+6-m))+
                '|'+x['is_lend'].center(9)+'|'+str(x['price']).center(8)+
                '|'+str(x['start_date']).center(16)+'|'+str(x['end_date']).center(16)+'|')
        print('+'+('-'*(4))+'+'+('-'*(k+6))+'+'+('-'*(10))+'+'+('-'*(8))+'+'+('-'*(16))+'+'+('-'*(16))+'+')

    def find_cars(self):
        n=input('输入车辆名称')
        for x in self.cars:
            if n == x['name']:
                self.car_id=x['ID']
                self.name=x['name']
                self.is_lend=x['is_lend']
                self.price=x['price']
                self.start_date=x['start_date']
                self.end_date=x['end_date']
                return self.print_cars_info([x])

    def add_car(self):
        m=input('添加的车辆名称:')
        p=input('单价:')
        l=[x['ID'] for x in self.cars]
        d={'ID':str(int(max(l))+1),'name':m,'is_lend':'否','price':p,'start_date':'0','end_date':'0'}
        self.cars.append(d)
        return self.__save()
        # try:
        #     f=open('carlist.txt','a')
        #     f.writelines([str(d['ID']),',',d['name'],',',d['is_lend'],',',d['price'],',',d['start_date'],',',d['end_date'],'\n'])
        #     f.close()
        #     print('保存成功')
        # except OSError:
        #     print('保存失败')

    def __save(self):
        try:
            f=open('carlist.txt','w')
            for d in self.cars:
                f.writelines([str(d['ID']),',',d['name'],',',d['is_lend'],',',d['price'],',',d['start_date'],',',d['end_date'],'\n'])
            print('保存成功')
            f.close()
        except OSError:
            print('保存失败')

    def del_car(self):
        i=input('请输入要删除的车辆ID')
        for x in self.cars:
            if x['ID']==i:
                self.cars.remove(x)
        return self.__save()

    def lend(self):
        import time
        t=time.localtime()
        a=input('请输入要租赁的车辆ID')
        for x in self.cars:
            if x['ID']==a:
                x['is_lend']='是'
                x['start_date']=('%d/%02d/%02d %02d:%02d'% t[0:5])
                x['end_date']='-'
        return self.__save()


    def back(self):
        import time
        t=time.localtime()
        a=input('请输入要还的车辆ID')
        for x in self.cars:
            if x['ID']==a:
                x['is_lend']='否'
                x['end_date']=('%d/%02d/%02d %02d:%02d'% t[0:5])
        return self.__save()

if __name__=='__main__':
    st=car_store()
    st.print_cars_info()
    st.add_car()
    st.lend()
    st.print_cars_info()
    st.back()
    st.print_cars_info()