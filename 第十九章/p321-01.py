def w1(func):
     def inner():
         # 验证1
         # 验证2
         # 验证3
         func()
     return inner
@w1
def f1():
     print('f1')
@w1
def f2():
     print('f2')
@w1
def f3():
     print('f3')
@w1
def f4():
     print('f4')