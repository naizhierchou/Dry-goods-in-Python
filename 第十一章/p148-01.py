class Dog:
    type = "狗" # 类属性
dog1 = Dog()
dog1.name = "旺财"
dog2 = Dog()
dog2.name = "来福"
# 类属性 取值
print(Dog.type) # 结果：狗
print(dog1.type) # 结果：狗
print(dog2.type) # 结果：狗