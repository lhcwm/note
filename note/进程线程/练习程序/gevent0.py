import gevent

def foo():
    print('funning too')
    gevent.sleep(2)
    print('foo again')

def bar():
    print('funning bar')
    gevent.sleep(1)
    print('bar again')

f=gevent.spawn(foo)
b=gevent.spawn(bar)

gevent.joinall([f,b])