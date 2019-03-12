#账户类

# 作业:
#  编写一个账户类(Account)
#   属性:账号(acct_no),户名(acct_name),开户日期(acct_date),类型(acct_type),
#        状态(acct_status),余额(balance)
#  方法:存款(diposite) 取款(draw) 冻结(freeze) 解冻(unfreeze) 挂失(report_loss) 
#  解挂失(relieve_loss)  修改账户信息(modify_info)
# 编写测试代码

class Acct:   #父类:包含属性,显示账户信息,冻结,解冻,挂失,解挂失
    def __init__(self,acct_no,acct_name,acct_date,acct_type):
        self.acct_no=acct_no      #账号
        self.acct_name=acct_name  #户名
        self.acct_date=acct_date  #开户日期
        self.acct_type=acct_type  #类型(借记卡,贷记卡)
        self.acct_status=[]       #状态(冻结,挂失)
        self.balance=0            #余额

    def modify_info(self):        #显示账户信息
        print('您的信息如下:\n姓名:%s\n账号:%d\n卡类型:%s\n余额:%.2f'%
        (self.acct_name,self.acct_no,self.acct_type,self.balance))

    def freeze(self):             #冻结
        if 'freeze' not in self.acct_status:
            self.acct_status+=['freeze']
            print('您的卡已冻结')
        else:
            print('您的卡已冻结,无需再次冻结')

    def unfreeze(self):           #解冻
        if 'freeze' in self.acct_status:
            self.acct_status.remove('freeze')
            print('您的卡解冻成功')
        else:
            print('您的卡没有冻结')

    def report_loss(self):        #挂失
        if 'loss' not in self.acct_status:         #判断卡的状态是否为挂失
            self.acct_status+=['loss','freeze']    #卡若挂失,会同时将卡挂失并冻结
            print('您的卡已挂失')
        else:
            print('您的卡已挂失,无需再次挂失')

    def relieve_loss(self):       #解挂失
        if 'loss' in self.acct_status:        #判断是否为挂失状态
            self.acct_status.remove('loss')   #卡若解挂失,会同时将卡解挂失并解冻
            self.acct_status.remove('freeze')
            print('您的卡已解除挂失')
        else:
            print('您的卡没有挂失,无需解除挂失')

class Dip(Acct):                 #子类:存取款
    def diposite(self,money):    #存款
        self.balance += money
        print('存钱成功!您当前余额为:%.2f'%self.balance)

    def draw(self,money):        #取款
        try:
            assert self.acct_status==[]       #断言语句,如果状态不为空,则不能取款
            if self.acct_type=='借记卡':       #判断是否为借记卡
                if money>self.balance:        #取款值与余额的判断
                    print('您的余额不足,当前余额为%.2f'%self.balance)
                else:
                    self.balance-=money
                    print('取款成功,剩余余额为:%.2f'%self.balance)
            else:
                if money>self.balance+5000:    #判断是否为贷记卡,最大透支5000
                    print('取款额度超出取现上限,请重新输入取款金额')
                else:
                    self.balance-=money
                    print('取款成功,剩余余额为:%.2f'%self.balance)

        except AssertionError:    #若状态不为空,判定相关状态并反馈
            if 'freeze' in self.acct_status:
                if 'loss' in self.acct_status:
                    print('您的卡目前处于挂失状态,不能取钱')
                else:
                    print('您的卡目前处于冻结状态,不能取钱')

if __name__=='__main__':    #测试代码
    A=Dip(123666,'张三','20181010','贷记卡')   #实例化
    A.report_loss()         #挂失
    A.diposite(1000)        #存款
    A.draw(5000)            #取款
    A.unfreeze()            #解冻
    A.freeze()              #冻结
    A.relieve_loss()        #解挂失
    A.modify_info()         #显示账户信息