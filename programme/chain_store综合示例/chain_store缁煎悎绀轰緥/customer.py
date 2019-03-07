# customer.py
# 客户类
class Customer: #客户类
    def __init__(self,cust_id,cust_name,tel_no):
        self.cust_id = cust_id       
        self.cust_name = cust_name        
        self.tel_no = tel_no

    def __str__(self):
        ret = "客户编号:%s,客户名称:%s,电话:%s" \
          %(self.cust_id, self.cust_name, self.tel_no) 
        return ret