import os
import shutil
import multiprocessing
# import time
# ⽂件拷⻉任务
def copy_work(src_dir, dst_dir, file_name):
     # 查看进程对象
     pid = multiprocessing.current_process().pid
     print(pid)
     # 拼接源⽂件的路径
     src_file_path = src_dir + "/" + file_name
     # 拼接⽬标⽂件的路径
     dst_file_path = dst_dir + "/" + file_name
     with open(dst_file_path, "wb") as dst_file:
         # 打源⽂件读取⽂件中的数据
         with open(src_file_path, "rb") as src_file:
             while True:
                 # 读取数据
                 src_file_data = src_file.read(1024)
                 if src_file_data:
                     # 写⼊到⽬标⽂件⾥⾯
                     dst_file.write(src_file_data)
                 else:
                    break
             # time.sleep(0.5)
if __name__ == '__main__':
     # 源⽬录
     src_dir = "test"
     # ⽬标⽬录
     dst_dir = "/home/python/Desktop/test"
     # 判断⽂件夹是否存在
     if os.path.exists(dst_dir):
         # 存在则删除⽂件夹及⽂件夹⾥⾯的所有⽂件
         shutil.rmtree(dst_dir)
     # 创建⽬标⽂件夹
     os.mkdir(dst_dir)
     # 获取源⽬录⾥⾯⽂件的列表
     file_name_list = os.listdir(src_dir)
     # 创建进程池
     pool = multiprocessing.Pool(3)
     # 遍历⽂件⾥⾯获取⽂件名
     for file_name in file_name_list:
         # 使⽤进程池执⾏拷⻉任务
         pool.apply_async(copy_work, (src_dir, dst_dir, file_name))
     # 关闭进程池
     pool.close()
     # 主进程等待进程池执⾏完成以后程序再退出
     pool.join()