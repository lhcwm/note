#自定义列表

class Mylist:
    def __init__(self,iterable=[]):
        self.data=[x for x in iterable]

    def __abs__(self):
        # return Mylist(abs(x) for x in self.data)
        return [abs(x) for x in self.data]

    def __len__(self):
        return len(self.data)

    def __round__(self):
        return [round(x) for x in self.data]

    def __reversed__(self):
    #     # return Mylist(reversed(self.data))
        return Mylist(self.data[::-1])

    def __add__(self,l):
        return (self.data+l.data)

    def __eq__(self,l):
        if len(self.data)==len(l.data):
            for x in range(len(self.data)):
                if self.data[x]!=l.data[x]:
                    return False
            return True
        return False

    def __gt__(self,l):
        return (self.data>l.data)

    def __lt__(self,l):
        for x in range(min(len(self.data),len(l.data))):
            if self.data[x]==l.data[x]:
                continue
            if self.data[x]<l.data[x]:
                return True
            if self.data[x]<l.data[x]:
                return False
        if len(self.data)<len(l.data):
            return True
        return False


    def __ne__(self,l):
        if len(self.data)!=len(l.data):
            for x in range(min(len(self.data),len(l.data))):
                if self.data[x]==l.data[x]:
                    return False
            return True
        return False

    def __mul__(self,l):
        return (self.data*l)


    def __str__(self):
        l=''
        for x in self.data:
            l+=str(x)
            l+=' '
        return l

    def __neg__(self):
        return [-x for x in self.data]

    def __invert__(self):
        return [~x for x in self.data]

    def __contains__(self,e):
        return e in self.data

    def __getitem__(self,i):
        return self.data[i]

    def __setitem__(self,i,value):
        self.data[i]=value

    def __delitem__(self,i):
        del self.data[i]

if __name__=='__main__':
    # L=Mylist([-1,2,3,-2.2])
    # print(abs(L))
    # print(len(L))
    # print(round(L))
    # print(reversed(L))
    l1=Mylist([1,2,8,4])
    print(l1[2])
    l1[2]=0
    print(l1)
    del l1[2]
    print(l1)
    # l2=2
    # print(l2 in l1)
    # print(-l1)
    # print(l1)
    # l2=Mylist([1,2,3])
    # print(l1<l2)
    # print(l1*2)
    # print(l1==l2)
