# #连锁店类

# class Chain:
#     #类属性
#     store_num=0   #门店数量
#     total_income=0  #所有门店总营业额
#     store_list=[]   #所有门店对象列表
#     cus_list=[]

#     def __init__(self,no,name,address,manager):
#         print('门店开张')
#         self.no=no    #编号
#         self.name=name   #名称
#         self.address=address  #地址
#         self.manager=manager  #经理
#         self.myincome=0  #本店营业额
#         Chain.store_num+=1  #门店开张,总数量加1
#         Chain.store_list.append(self)  #添加当前对象到列表中
#         self.staff_list=[]

#     def cus_r(self,cus):
#         Chain.cus_list.append(cus)

#     def print_info(self):
#         for cust in Chain.cus_list:
#             print(cust)

#     def do_business(self,income):#营业
#         print('正在营业')
#         self.myincome+=income  #营业额累加
#         Chain.total_income+=income  #本店营业额度累加到总的营业额度

#     def __str__(self):
#         ret='编号:%s,名称:%s,地址:%s,店长:%s,总营业额:%.2f'%(self.no,
#         self.name,self.address,self.manager,self.myincome)
#         return ret

#     def add_staff(self,Staff):
#         return self.staff_list.append(Staff)

#     def del_staff(self,name):
#         return self.staff_list.remove(name)



# #     @classmethod
# #     def print_t(cls):
# #         print('门店数量:%d'%cls.store_num)
# #         for x in cls.store_list:
# #             print(str(x))

# #     @staticmethod
# #     def print_r():
# #         r='管理条例'
# #         print(r)

    
# #员工类,演示__slots__属性

# class Staff:
#     'adfafadsf'
#     __slots__=['no','name','position']

#     def __init__(self,no,name,position):
#         self.no=no
#         self.name=name
#         self.position=position
#         # self.salary=8000

#     def __str__(self):
#         return '%s,%s,%s'%(self.no,self.name,self.position)

# # if __name__=='__main__':
# #     s=Staff('01','jerry','经理')
# #     print(s)

# class Customer:
#     def __init__(self,cust_id,cust_name,tel_no):    
#         self.cust_id=cust_id
#         self.cust_name=cust_name
#         self.tel_no=tel_no

#     def __str__(self):
#         ret='客户编号:%s,客户名称:%s,电话:%s'%(self.cust_id,self.cust_name,self.tel_no)
#         return ret

# if __name__=='__main__':
#     s=Chain('1','嘻嘻旗舰店','西单','张三')
# #     s.do_business(20000)
# #     # print ('门店数量',Chain.store_num)
# #     # print('总营业额度',Chain.total_income)
# #     # print('')
# #     s2=Chain('2','哈哈旗舰店','东单','李四')
# #     s2.do_business(30000)
# #     # print ('门店数量',Chain.store_num)
# #     # print('总营业额度',Chain.total_income)
# #     Chain.print_t()
# #     Chain.print_r()
#     s.add_staff(Staff('1','baba','jingli'))
#     print(s.staff_list)
#     s.cus_r(Customer('1','bajie','4546546'))
#     s.print_info()

# with.py
# try:
#     # f=open('jghjh')
#     with open('saf','rt') as f: #不管操作是否发生异常,都能保证文件正确关闭
#         for x in f:
#             print(x)
# except:
#     print('文件操作失败')

# class A:  #自定义资源管理器
#     def __init__(self,name):
#         self.name=name

#     def __enter__(self):
#         print('enter方法被执行')
#         return self

#     def __exit__(self,exc_type,exc_val,exc_tb):
#         print('exit方法被执行')
#         if exc_type is None:
#             print('没有出现异常')
#         else:
#             print('%s,%s,%s'%(exc_type,exc_val,exc_tb))


# if __name__=='__main__':
#     with A('cc') as a:
#         print('with语句被执行')
#         a=int(input('11'))
#     print('程序退出')

# 编写一个程序,模拟扫福,各种福的产生概率如下:
# 爱国福30%
# 敬业福10%
# 富强福30%
# 友善福20%
# 和谐福10%

# def fu():
#     import random as R
#     s=R.randint(1,100)
#     # x=input('扫福')
#     if 0<s<31:
#         print('爱国福')
#     elif 30<s<61:
#         print('富强福')
#     elif 60<s<71:
#         print('敬业福')
#     elif 70<s<91:
#         print('友善福')
#     elif 90<s<101:
#         print('和谐福')
#     return s

# def test():
#     x1=0
#     x2=0
#     x3=0
#     x4=0
#     x5=0
#     for x in range(1000):
#         s=fu()
#         if 0<s<31:
#             x1+=1
#         elif 30<s<61:
#             x2+=1
#         elif 60<s<71:
#             x3+=1
#         elif 70<s<91:
#             x4+=1
#         elif 90<s<101:
#             x5+=1
#     print('爱国福出现%d次,富国福出现%d次,敬业福出现%d次,友善福出现%d次,和谐福出现%d次'
#     %(x1,x2,x3,x4,x5))

# test()



# create table acct(
# acct_no varchar(32),
# acct_name varchar(128)
# ) default charset=utf8;

# A=[]
# l=[1,2,2,2,5,3,4,5,6]
# for x in l :
#     if x not in A:
#         A.append(x)
#         print(l.count(x))
# x='hello word'
# y=x.replace('hello','hi')
# print(y)

# def f(x,l=[]):
#     for i in range(x):
#         l.append(i+i)
#     print (l)

# f(3)
# f(3,[3,2,1])
# f(2)
class A():
    v = 100
    def __init__(self):
        self.v = 200
class B(A):
    v = 300
    def __init__(self):
        super().__init__()
        self.v = 400
a = B()
print(a.v)