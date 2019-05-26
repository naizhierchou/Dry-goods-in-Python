import threading
import time
# 创建互斥锁
lock = threading.Lock()
# 根据下标去取值， 保证同⼀时刻只能有⼀个线程去取值
def get_value(index):
     # 上锁
     lock.acquire()
     print(threading.current_thread())
     my_list = [3,6,8,1]
     # 判断下标释放越界
     if index >= len(my_list):
         print("下标越界:", index)
         return
     value = my_list[index]
     print(value)
     time.sleep(0.2)
     # 释放锁
     lock.release()
if __name__ == '__main__':
     # 模拟⼤量线程去执⾏取值操作
     for i in range(30):
         sub_thread = threading.Thread(target=get_value, args=(i,))
         sub_thread.start()