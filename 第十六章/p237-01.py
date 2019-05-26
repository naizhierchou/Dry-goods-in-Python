import multiprocessing
import time
# 写⼊数据
def write_data(queue):
     for i in range(10):
         if queue.full():
             print("队列满了")
             break
         queue.put(i)
         time.sleep(0.2)
         print(i)
# 读取数据
def read_data(queue):
     while True:
     # 加⼊数据从队列取完了，那么跳出循环
         if queue.qsize() == 0:
             print("队列空了")
             break
         value = queue.get()
         print(value)
if __name__ == '__main__':
     # 创建消息队列
     queue = multiprocessing.Queue(5)
     # 创建写⼊数据的进程
     write_process = multiprocessing.Process(target=write_data, args=(queue,))
     # 创建读取数据的进程
     read_process = multiprocessing.Process(target=read_data, args=(queue,))
     # 启动进程
     write_process.start()
     # 主进程等待写⼊进程执⾏完成以后代码再继续往下执⾏
     write_process.join()
     read_process.start()