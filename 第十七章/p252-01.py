my_list = [i * 2 for i in range(5)]
print(my_list)
# 创建⽣成器
my_generator = (i * 2 for i in range(5))
print(my_generator)
# next获取⽣成器下⼀个值
# value = next(my_generator)
#
# print(value)
for value in my_generator:
    print(value)