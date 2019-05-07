def get_my_info():
    high = 178
    weight = 100
    age = 18
    return high, weight, age # 函数返回三个数据，会⾃动打包为元组
# result = get_my_info() # result 接收到⼀个元组
# print(result)
my_high, my_weight, my_age = get_my_info() # 直接把元组拆分为三个变量来使⽤，更加⽅便
print(my_high)
print(my_weight)
print(my_age)