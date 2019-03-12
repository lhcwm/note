# 修改示例
import pymysql
from db_conf import *
try:
    # 连接数据库
    conn = pymysql.connect(host,user,passwd,dbname,charset='utf8')
    #获取游标
    cursor = conn.cursor()
    # 执行SQL语句
    sql = ''' update  acct set balance = balance+1000
    where cust_no = 'C006' '''
    cursor.execute(sql)  #执行插入
    conn.commit()  #提交事务
    cursor.close() #关闭游标
    print('修改成功,影响笔数:%d'% cursor.rowcount)
except Exception as e:
    conn.rollback() #出现异常回滚事务
    print('数据库操作失败')
    print(e)
finally:
    conn.close()  #关闭连接