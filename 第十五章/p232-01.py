import threading
# 定义全局变量
g_num = 0
# 循环⼀次给全局变量加1
def sum_num1():
     for i in range(1000000):
         global g_num
         g_num += 1
     print("sum1:", g_num)
# 循环⼀次给全局变量加1
def sum_num2():
     for i in range(1000000):
         global g_num
         g_num += 1
     print("sum2:", g_num)
if __name__ == '__main__':
     # 创建两个线程
     first_thread = threading.Thread(target=sum_num1)
     second_thread = threading.Thread(target=sum_num2)
     # 启动线程
     first_thread.start()
     # 启动线程
     second_thread.start()