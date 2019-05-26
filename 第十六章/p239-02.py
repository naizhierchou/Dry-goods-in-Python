# 进程池:池⼦⾥⾯放的进程，进程池会根据任务执⾏情况⾃动创建进程，⽽且尽量少创建进程，合理利⽤进
# 程池中的进程完成多任务
import multiprocessing
import time
# 拷⻉任务
def work():
     print("复制中...", multiprocessing.current_process().pid)
     # 获取当前进程的守护状态
     # 提示：使⽤进程池创建的进程是守护主进程的状态，默认⾃⼰通过Process创建的进程是不是守住主
    #进程的状态
     # print(multiprocessing.current_process().daemon)
     time.sleep(0.5)
if __name__ == '__main__':
     # 创建进程池
     # 3:进程池中进程的最⼤个数
     pool = multiprocessing.Pool(3)
     # 模拟⼤批量的任务，让进程池去执⾏
     for i in range(5):
         # 循环让进程池执⾏对应的work任务
         # 同步执⾏任务，⼀个任务执⾏完成以后另外⼀个任务才能执⾏
         # pool.apply(work)
         # 异步执⾏，任务执⾏不会等待，多个任务⼀起执⾏
         pool.apply_async(work)
     # 关闭进程池，意思告诉主进程以后不会有新的任务添加进来
     pool.close()
     # 主进程等待进程池执⾏完成以后程序再退出
     pool.join()