# 数据库访问类
import pymysql
class DBoper:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = '123456'
        self.dbname = 'jason'
        self.conn=self.open_counn()
    def open_counn(self): #连接数据库
        try:
            # 连接数据库
            conn = pymysql.connect(self.host,self.user,self.passwd,self.dbname,charset='utf8')
            print('数据库连接成功')
            return conn
        except Exception as e:
            print('数据库连接失败')
            print(e)

    def close_conn(self): #关闭连接
        try:
            self.conn.close()
            print('数据库关闭成功')
        except Exception as e:
            print('数据库关闭错误')

    def do_query(self,sql): #查询,返回结果集
        if not sql or sql =='':
            print('sql语句不合法')
            return None
        try:
            cursor = self.conn.cursor() #获取游标
            cursor.execute(sql)
            result = cursor.fetchall() #取查询到的数据
            cursor.close() #关闭游标
            return result
        except Exception as e:
            print('数据查询失败')
            print(e)

    def do_update(self,sql):  #执行增删改等数据操作
        if not sql or sql =='':
            print('sql语句不合法')
            return None
        try:
            cursor = self.conn.cursor() #获取游标
            cursor.execute(sql)  #执行插入
            self.conn.commit()  #提交事务
            cursor.close() #关闭游标
            print('修改成功,影响笔数:%d'% cursor.rowcount)
        except Exception as e:
            self.conn.rollback() #出现异常回滚事务
            print('数据修改失败')
            print(e)


    def __del__(self):
        self.close_conn()


if __name__=='__main__':
    def que():
        query=db.do_query('select * from acct')
        for r in query:
            print('账号:%s,姓名:%s,余额:%s'%(r[0],r[1],r[6]))
    db=DBoper()
    # delete=db.do_update(''' delete from acct where cust_no='C007' ''')
    # que()
    update=db.do_update(''' update  acct set acct_type = 1
    where cust_no = 'C003' ''')
    # que()
    # insert=db.do_update('''insert into acct values
    # ('62234500003','亮亮','C007',1,date(now()),2,9877)''')
    que()

