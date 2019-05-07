class Dog(object):
    type = "狗" # 类属性
    def __init__(self):
        self.type = "dog" # 对象属性
# 创建对象
dog1 = Dog()
print(Dog.type) # 结果为 "狗" 使⽤ 类对象 访问类属性
print(dog1.type) # 结果为 “dog” 类属性和实例属性同名，使⽤ 实例对象 访问的是 实例属性