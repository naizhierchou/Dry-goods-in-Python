class Dog:
    def demo_method(self):
        print("对象⽅法")

    @classmethod
    def demo_method(cls):
        print("类⽅法")

    @staticmethod
    def demo_method():  # 被最后定义
        print("静态⽅法")

dog1 = Dog()
Dog.demo_method()  # 结果: 静态⽅法
dog1.demo_method()  # 结果: 静态⽅法