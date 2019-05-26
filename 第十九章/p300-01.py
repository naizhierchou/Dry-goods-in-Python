
class Test(object):
     def __init__(self, func):
         print("---初始化---")
         print("func name is %s"%func.__name__)
         self.__func = func
     def __call__(self):
         print("---装饰器中的功能---")
         self.__func()
    #说明：
#1. 当⽤Test来装作装饰器对test函数进⾏装饰的时候，⾸先会创建Test的实例对象
# 并且会把test这个函数名当做参数传递到__init__⽅法中
# 即在__init__⽅法中的属性__func指向了test指向的函数
#
#2. test指向了⽤Test创建出来的实例对象
#
#3. 当在使⽤test()进⾏调⽤时，就相当于让这个对象()，因此会调⽤这个对象的__call__⽅法
#
#4. 为了能够在__call__⽅法中调⽤原来test指向的函数体，所以在__init__⽅法中就需要⼀个实例
#属性来保存这个函数体的引⽤
# 所以才有了self.__func = func这句代码，从⽽在调⽤__call__⽅法中能够调⽤到test之前的
#函数体
@Test
def test():
    print("----test---")
test()
showpy()#如果把这句话注释，重新运⾏程序，依然会看到"--初始化--"