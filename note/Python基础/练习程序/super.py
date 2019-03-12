class A :
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return 'name=%s'%self.name

class B(A):
    def __init__(self,name,id):
        super().__init__(name)
        self.id=id

    def __repr__(self):  #重写__repr__方法
        return "B('%s','%s')"%(self.name,self.id)

    def __str__(self): #重写__str__函数
        return 'name=%s,id=%s'%(self.name,self.id)

b=B('jerry','01')
print(b.id)
print(b.name)
# super(B,b).print()
# print(b)
# a=str(b)
# print(a)
# s=repr(b)
# print(s)
# e=eval(s)
# print(e)