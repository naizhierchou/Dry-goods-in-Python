# 实例化⼀个单例
class Singleton(object):
    __instance = None
    __is_first = True
    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self, age, name):
        if self. __is_first:
            self.age = age
            self.name = name
            Singleton.__is_first = False


a = Singleton(18, "习⼤⼤")
b = Singleton(28, "习⼤⼤")
print(id(a))
print(id(b))
print(a.age)
print(b.age)
a.age = 19
print(b.age)