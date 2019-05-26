class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果⼦配⽅"
    def make_cake(self):
        print("[古法] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)
class Prentice(Master):
    def __init__(self):
        self.kongfu = "猫⽒煎饼果⼦配⽅"
        self.money = 10000 # 亿美⾦
    def make_cake(self):
        self.__init__() # 执⾏本类的__init__⽅法，做属性初始化 self.kongfu = "猫⽒...."
        print("[猫⽒] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)
 # 调⽤⽗类⽅法格式：⽗类类名.⽗类⽅法(self)
    def make_old_cake(self):
        Master.__init__(self) # 调⽤了⽗类Master的__init__⽅法 self.kongfu = "古法...."
        Master.make_cake(self) # 调⽤了⽗类Master的实例⽅法
class PrenticePrentice(Prentice): # 多层继承
    pass
pp = PrenticePrentice()
pp.make_cake() # 调⽤⽗类的实例⽅法
pp.make_old_cake()
print(pp.money)