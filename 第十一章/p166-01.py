# 实例化⼀个单例
class Singleton(object):
    __instance = None
    def __new__(cls, age, name):
        #如果类属性__instance的值为None，
        #那么就创建⼀个对象，并且赋值为这个对象的引⽤，保证下次调⽤这个⽅法时
        #能够知道之前已经创建过对象了，这样就保证了只有1个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
a = Singleton(18, "zuoge")
b = Singleton(8, "zuoge")
print(id(a))
print(id(b))
a.age = 19 #给a指向的对象添加⼀个属性
print(b.age)#获取b指向的对象的age属性