import threading
import time
# 定义全局变量
my_list = list()
# 写⼊数据任务
def write_data():
     for i in range(5):
         my_list.append(i)
         time.sleep(0.1)
     print("write_data:", my_list)
# 读取数据任务
def read_data():
     print("read_data:", my_list)
if __name__ == '__main__':
     # 创建写⼊数据的线程
     write_thread = threading.Thread(target=write_data)
     # 创建读取数据的线程
     read_thread = threading.Thread(target=read_data)
     write_thread.start()
     # 延时
     # time.sleep(1)
     # 主线程等待写⼊线程执⾏完成以后代码在继续往下执⾏
     write_thread.join()
     print("开始读取数据啦")
     read_thread.start()