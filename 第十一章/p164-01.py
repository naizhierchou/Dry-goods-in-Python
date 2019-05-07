class Dog(object):
    type = "狗"
    def __init__(self):
        name = None
    # 静态⽅法
    @staticmethod
    def introduce(): # 静态⽅法不会⾃动传递实例对象和类对象
        print("⽝科哺乳动物,属于⻝⾁⽬..")
dog1 = Dog()
Dog.introduce() # 可以⽤ 实例对象 来调⽤ 静态⽅法
dog1.introduce() # 可以⽤ 类对象 来调⽤ 静态⽅法