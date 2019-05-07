class Dog(object):
    type = "狗" # 类属性
# 创建对象
dog1 = Dog()
Dog.type = "Dog" # 使⽤ 类对象 修改类属性
dog1.type = "dog" # 使⽤ 实例对象 创建了对象属性type
print(dog1.type) # 结果为 “dog” 类属性和实例属性同名，访问的是实例属性
print(Dog.type) # 结果为 "Dog" 访问类属性