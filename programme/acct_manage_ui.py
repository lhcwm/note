from db_oper import *
from acct_manage import *
al=AcctManage(DBoper())

#根据用户输入,进行不同操作
menu = '''
-------请选取要执行的操作-------
    1,查询所有
    2,根据姓名查询
    '''

oper=input(menu)
if oper =='1':
    accts=al.query_all_acct()
    for r in accts:
        print(r)
else:

    ac=al.query_by_id(input('请输入姓名'))
    print(ac)