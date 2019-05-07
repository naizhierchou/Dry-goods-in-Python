import multiprocessing
# 显示⼈员信息
def show_info(name, age):
    print(name, age)
if __name__ == '__main__':
     # 创建⼦进程
     # 1. group:进程组，⽬前必须使⽤None，⼀般不⽤设置
     # 2. target:执⾏⽬标函数
     # 3. name: 进程名称
     # 4. args: 以元组⽅式给函数传参
     # 5. kwargs: 以字典⽅式给函数传参
     sub_process = multiprocessing.Process(target=show_info, name="myprocess",
     args=("古⼒娜扎", 18))
     # 启动进程
     sub_process.start()
     # sub_process = multiprocessing.Process(target=show_info,name = "myprocess",
     # kwargs={"name": "貂蝉", "age": 20})
     #
     # # 启动进程
     # sub_process.start()