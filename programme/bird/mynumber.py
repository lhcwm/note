#数值转换函数

class Number:
    def __init__(self,value):
        self.data=value   #值,字符串类型

    def __int__(self):
        return int(float(self.data))

    def __float__(self):
        return float(self.data)

    def __complex__(self):
        return complex(self.data)

if __name__=='__main__':
    n=Number('123.456')
    print(int(n))
    print(float(n))
    print(complex(n))
    print(getattr(n,'data'))
    setattr(n,'data',777)
    print(n.data)