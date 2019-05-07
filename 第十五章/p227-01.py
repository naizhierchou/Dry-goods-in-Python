import threading
import time
# 唱歌
def sing():
     # 扩展:-获取当前执⾏代码的线程
     print("sing:", threading.current_thread())
     for i in range(5):
         print("唱歌")
         time.sleep(0.2)
# 跳舞
def dance():
     # 扩展:-获取当前执⾏代码的线程
     print("dance:", threading.current_thread())
     for i in range(5):
         print("跳舞")
         time.sleep(0.2)
if __name__ == '__main__':
     # 扩展:-获取当前执⾏代码的线程
     print("main:", threading.current_thread())
     # 获取当前程序活动线程的列表
     thread_list = threading.enumerate()
     print("111:", thread_list, len(thread_list))
     # 创建唱歌线程, 表示创建的⼦线程执⾏唱歌任务
     sing_thread = threading.Thread(target=sing)
     # 创建跳舞的线程, 表示创建的⼦线程执⾏跳舞任务
     dance_thread = threading.Thread(target=dance)
     thread_list = threading.enumerate()
     print("222:", thread_list, len(thread_list))
     # 启动线程,执⾏对应的任务
     sing_thread.start()
     # 启动线程,执⾏对应的任务
     dance_thread.start()
     #提示：只有线程启动了，才能加⼊到活动线程列表中
     thread_list = threading.enumerate()
     print("333:", thread_list, len(thread_list))