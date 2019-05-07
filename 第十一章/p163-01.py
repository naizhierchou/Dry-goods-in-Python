class Dog(object):
    count = 0 # 公有的类属性
    __type = "狗" # 私有的类属性
print(Dog.count) # 正确
#print(Dog.__type) # 错误