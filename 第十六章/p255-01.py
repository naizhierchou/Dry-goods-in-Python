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
     # 设置守护主进程，主进程退出后⼦进程直接销毁，不再执⾏⼦进程中的代码
     # work_process.daemon = True
     work_process.start()
     # 让主进程等待1秒钟
     time.sleep(1)
     print("主进程执⾏完成了啦")
     # 让⼦进程直接销毁，表示终⽌执⾏， 主进程退出之前，把所有的⼦进程直接销毁就可以了
     work_process.terminate()
     # 总结： 主进程会等待所有的⼦进程执⾏完成以后程序再退出
