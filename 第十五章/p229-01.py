import threading
import time
# 测试主线程是否会等待⼦线程执⾏完成以后程序再退出
def show_info():
     for i in range(5):
         print("test:", i)
         time.sleep(0.5)
if __name__ == '__main__':
     sub_thread = threading.Thread(target=show_info)
     sub_thread.start()
     # 主线程延时1秒
     time.sleep(1)
     print("over")