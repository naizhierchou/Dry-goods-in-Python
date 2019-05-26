print("******单继承使⽤super().__init__ 发⽣的状态******")
class Parent(object):
     def __init__(self, name):
         print('parent的init开始被调⽤')
         self.name = name
         print('parent的init结束被调⽤')
class Son1(Parent):
     def __init__(self, name, age):
         print('Son1的init开始被调⽤')
         self.age = age
         super().__init__(name) # 单继承不能提供全部参数
         print('Son1的init结束被调⽤')
class Grandson(Son1):
     def __init__(self, name, age, gender):
         print('Grandson的init开始被调⽤')
         super().__init__(name, age) # 单继承不能提供全部参数
         print('Grandson的init结束被调⽤')
gs = Grandson('grandson', 12, '男')
print('姓名：', gs.name)
print('年龄：', gs.age)
#print('性别：', gs.gender)
print("******单继承使⽤super().__init__ 发⽣的状态******\n\n")