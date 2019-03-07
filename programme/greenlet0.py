from greenlet import greenlet

def test1():
    print('执行test1')
    grl2.switch()
    print('结束test1')

def test2():
    print('执行test2')
    grl.switch()
    print('结束test2')

# 将函数变为协程函数
grl=greenlet(test1)
grl2=greenlet(test2)

grl.switch() #执行协程

