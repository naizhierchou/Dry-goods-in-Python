import threading
# ⾃定义线程类
class MyThread(threading.Thread):
     # 通过构造⽅法取接收任务的参数
     def __init__(self, info1, info2):
         # 调⽤⽗类的构造⽅法
         super(MyThread, self).__init__()
         self.info1 = info1
         self.info2 = info2
     # 定义⾃定义线程相关的任务
     def test1(self):
         print(self.info1)
     def test2(self):
         print(self.info2)
     # 通过run⽅法执⾏相关任务
     def run(self):
         self.test1()
         self.test2()
 # 创建⾃定义线程
my_thread = MyThread("测试1", "测试2")
# 启动
my_thread.start()