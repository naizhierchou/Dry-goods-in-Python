class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果⼦配⽅" # 实例变量，属性
    def make_cake(self): # 实例⽅法，⽅法
        print("[古法] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)
class Prentice(Master): # 多继承，继承了多个⽗类
    def __init__(self):
        self.kongfu = "猫⽒煎饼果⼦配⽅"
    def make_cake(self):
        self.__init__() # 执⾏本类的__init__⽅法，做属性初始化 self.kongfu = "猫⽒...."
        print("[猫⽒] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)
 # 调⽤⽗类⽅法格式：⽗类类名.⽗类⽅法(self)
    def make_old_cake(self):
 # 可以通过执⾏Master类的__init__⽅法，来修改self的属性值
        Master.__init__(self) # 调⽤了⽗类Master的__init__⽅法 self.kongfu = "古法...."
        Master.make_cake(self) # 调⽤⽗类Master的实例⽅法
# 实例化对象，⾃动执⾏⼦类的__init__⽅法
damao = Prentice()
damao.make_cake() # 调⽤⼦类的⽅法（默认重写了⽗类的同名⽅法）
print("--" * 10)
damao.make_old_cake() # 进⼊实例⽅法去调⽤⽗类Master的⽅法