# 账户管理类(业务逻辑层)
# 实现账户的新增,修改,查询,删除等逻辑处理
from db_oper import *
class Acct: #账户类,仅用于数据传输
    def __init__(self,acct_no,acct_name,acct_type,balance):
        self.acct_no=acct_no
        self.acct_name=acct_name
        self.acct_type=acct_type
        self.balance=balance
    def __str__(self):
        ret='账号:%s,户名:%s,类型:%s,余额:%s'%(self.acct_no,
        self.acct_name,self.acct_type,self.balance)
        return ret

class AcctManage:  #账户管理类
    def __init__(self,db_oper):
        self.db_oper=db_oper #数据访问对象

    def query_all_acct(self): #查询所有账户信息
        accts=[] #返回的acct对象列表,可能有多个对象
        #拼装所需的SQL
        sql='select * from acct'
        #执行查询
        result = self.db_oper.do_query(sql)
        if not result:
            print('查询结果为空')
            return None
        #返回结果:实例化一个Acct对象列表再返回
        for r in result:
            acct_no=r[0] #账号
            acct_name=r[1] #户名
            acct_type=r[3] #类型
            balance=r[6] #余额
            accts.append(Acct(acct_no,acct_name,acct_type,balance))
        return accts #返回对象列表

    def query_by_id(self,acct_name): #根据账户查询,最多返回一个acct对象
        sql='select * from acct where acct_name="%s"'% acct_name
        result = self.db_oper.do_query(sql)
        if not result:
            print('查询结果为空')
            return None
        #返回结果:实例化一个Acct对象列表再返回
        r = result[0] #此时result是嵌套元组((),)
        acct_no=r[0] #账号
        acct_name=r[1] #户名
        acct_type=r[3] #类型
        balance=r[6] #余额
        ac=Acct(acct_no,acct_name,acct_type,balance)
        return ac #返回对象列表


if __name__=='__main__':
    al=AcctManage(DBoper())

    #根据用户输入,进行不同操作
    menu = '''
    -------请选取要执行的操作-------
        1,查询所有
        2,根据账户查询
        '''

    oper=input(menu)
    if oper =='1':
        accts=al.query_all_acct()
        for r in accts:
            print(r)
    else:
        print('暂不支持')
