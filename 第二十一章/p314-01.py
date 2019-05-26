# coding=utf-8
print("******多继承使⽤类名.__init__ 发⽣的状态******")
class Parent(object):
     def __init__(self, name):
         print('parent的init开始被调⽤')
         self.name = name
         print('parent的init结束被调⽤')
class Son1(Parent):
     def __init__(self, name, age):
         print('Son1的init开始被调⽤')
         self.age = age
         Parent.__init__(self, name)
         print('Son1的init结束被调⽤')
class Son2(Parent):
     def __init__(self, name, gender):
         print('Son2的init开始被调⽤')
         self.gender = gender
         Parent.__init__(self, name)
         print('Son2的init结束被调⽤')
class Grandson(Son1, Son2):
     def __init__(self, name, age, gender):
         print('Grandson的init开始被调⽤')
         Son1.__init__(self, name, age) # 单独调⽤⽗类的初始化⽅法
         Son2.__init__(self, name, gender)
         print('Grandson的init结束被调⽤')


gs = Grandson('grandson', 12, '男')
print('姓名：', gs.name)
print('年龄：', gs.age)
print('性别：', gs.gender)
print("******多继承使⽤类名.__init__ 发⽣的状态******\n\n")