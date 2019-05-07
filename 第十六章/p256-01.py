import multiprocessing
import time
if __name__ == '__main__':
     # 创建消息队列, 3:表示队列中最⼤消息个数
     queue = multiprocessing.Queue(3)
     # 放⼊数据
     queue.put(1)
     queue.put("hello")
     queue.put([3,5])
     # 总结: 队列可以放⼊任意数据类型
     # 提示： 如果队列满了，需要等待队列有空闲位置才能放⼊数据，否则⼀直等待
     # queue.put((5,6))
     # 提示： 如果队列满了，不等待队列有空闲位置，如果放⼊不成功直接崩溃
     # queue.put_nowait((5,6))
     # 建议： 向队列放⼊数据统⼀使⽤put
     # 查看队列是否满了
     # print(queue.full())
     # 注意点：queue.empty()判断队列是否空了不可靠
     # 查看队列是否空了
     # print(queue.empty())
     # 解决办法: 1. 加延时操作 2. 使⽤判断队列的个数,不使⽤empty
     # time.sleep(0.01)
     if queue.qsize() == 0:
        print("队列为空")
     else:
        print("队列不为空")
     # 获取队列的个数
     size = queue.qsize()
     print(size)
     # 获取数据
     value = queue.get()
     print(value)
     # 获取队列的个数
     size = queue.qsize()
     print(size)
     # 获取数据
     value = queue.get()
     print(value)
     # 获取数据
     value = queue.get()
     print(value)
     # 获取队列的个数
     size = queue.qsize()
     print(size)
     # 提示：如果队列空了，再取值需要等待，只有队列有值以后才能获取队列中数据
     # value = queue.get()
     # print(value)
     # 提示： 如果队列空了 ，不需要等待队列有值，但是如果取值的时候发现队列空了直接崩溃
     # 建议⼤家: 向队列取值使⽤get
     # value = queue.get_nowait()
     # print(value)