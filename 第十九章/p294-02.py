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