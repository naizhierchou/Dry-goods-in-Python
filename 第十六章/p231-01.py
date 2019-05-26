import multiprocessing
import time
# 定义全局变量
my_list = list()
# 写⼊数据
def write_data():
     for i in range(5):
         my_list.append(i)
         time.sleep(0.2)
     print("write_data:", my_list)
# 读取数据
def read_data():
    print(my_list)
if __name__ == '__main__':
     # 创建写⼊数据的进程
     write_process = multiprocessing.Process(target=write_data)
     read_process = multiprocessing.Process(target=read_data)
     write_process.start()
     # 主进程等待写⼊进程执⾏完成以后代码 再继续往下执⾏
     write_process.join()
     read_process.start()