print("******多继承使⽤super().__init__ 发⽣的状态******")
class Parent(object):
     def __init__(self, name, *args, **kwargs): # 为避免多继承报错，使⽤不定⻓参数，
    #接受参数
         print('parent的init开始被调⽤')
         self.name = name
         print('parent的init结束被调⽤')
class Son1(Parent):
     def __init__(self, name, age, *args, **kwargs): # 为避免多继承报错，使⽤不定⻓
    #参数，接受参数
         print('Son1的init开始被调⽤')
         self.age = age
         super().__init__(name, *args, **kwargs) # 为避免多继承报错，使⽤不定⻓参
        #数，接受参数
         print('Son1的init结束被调⽤')
class Son2(Parent):
     def __init__(self, name, gender, *args, **kwargs): # 为避免多继承报错，使⽤不
    #定⻓参数，接受参数
         print('Son2的init开始被调⽤')
         self.gender = gender
         super().__init__(name, *args, **kwargs) # 为避免多继承报错，使⽤不定⻓参
        #数，接受参数
         print('Son2的init结束被调⽤')
class Grandson(Son1, Son2):
     def __init__(self, name, age, gender):
         print('Grandson的init开始被调⽤')
         # 多继承时，相对于使⽤类名.__init__⽅法，要把每个⽗类全部写⼀遍
         # ⽽super只⽤⼀句话，执⾏了全部⽗类的⽅法，这也是为何多继承需要全部传参的⼀个原因
         # super(Grandson, self).__init__(name, age, gender)
         super().__init__(name, age, gender)
         print('Grandson的init结束被调⽤')
print(Grandson.__mro__)
gs = Grandson('grandson', 12, '男')
print('姓名：', gs.name)
print('年龄：', gs.age)
print('性别：', gs.gender)
print("******多继承使⽤super().__init__ 发⽣的状态******\n\n")