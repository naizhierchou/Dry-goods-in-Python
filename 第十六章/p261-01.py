import multiprocessing
import time
# 拷⻉任务
def work():
     print("复制中...", multiprocessing.current_process().pid)
     time.sleep(0.5)
if __name__ == '__main__':
     # 创建进程池
     # 3:进程池中进程的最⼤个数
     pool = multiprocessing.Pool(3)
     # 模拟⼤批量的任务，让进程池去执⾏
     for i in range(5):
         # 循环让进程池执⾏对应的work任务
         # 同步执⾏任务，⼀个任务执⾏完成以后另外⼀个任务才能执⾏
         pool.apply(work)