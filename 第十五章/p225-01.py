import threading
import time
# 唱歌任务
def sing():
     # 扩展： 获取当前线程
     # print("sing当前执⾏的线程为：", threading.current_thread())
     for i in range(3):
         print("正在唱歌...%d" % i)
         time.sleep(1)
# 跳舞任务
def dance():
     # 扩展： 获取当前线程
     # print("dance当前执⾏的线程为：", threading.current_thread())
     for i in range(3):
         print("正在跳舞...%d" % i)
         time.sleep(1)
if __name__ == '__main__':
     # 扩展： 获取当前线程
     # print("当前执⾏的线程为：", threading.current_thread())
     # 创建唱歌的线程
     # target： 线程执⾏的函数名
     sing_thread = threading.Thread(target=sing)
     # 创建跳舞的线程
     dance_thread = threading.Thread(target=dance)
     # 开启线程
     sing_thread.start()
     dance_thread.start()