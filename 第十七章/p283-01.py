import gevent
def work(n):
     for i in range(n):
     # 获取当前协程
         print(gevent.getcurrent(), i)
         #⽤来模拟⼀个耗时操作，注意不是time模块中的sleep
         gevent.sleep(1)
g1 = gevent.spawn(work, 5)
g2 = gevent.spawn(work, 5)
g3 = gevent.spawn(work, 5)
g1.join()
g2.join()
g3.join()