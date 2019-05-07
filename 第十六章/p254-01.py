import multiprocessing
import time
# 测试⼦进程是否执⾏完成以后主进程才能退出
def work():
     for i in range(10):
         print("⼯作中...")
         time.sleep(0.2)
if __name__ == '__main__':
     # 创建⼦进程
     work_process = multiprocessing.Process(target=work)
     work_process.start()
     # 让主进程等待1秒钟
     time.sleep(1)
     print("主进程执⾏完成了啦")
     # 总结： 主进程会等待所有的⼦进程执⾏完成以后程序再退出