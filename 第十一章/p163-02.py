class Dog(object):
    __type = "狗"
    # 类⽅法，⽤classmethod来进⾏修饰
    @classmethod
    def get_type(cls):
        return cls.__type
print(Dog.get_type())