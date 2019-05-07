class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果⼦配⽅" # 实例变量，属性
    def make_cake(self): # 实例⽅法，⽅法
        print("[古法] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)
class Prentice(Master):
    def __init__(self):
        self.kongfu = "猫⽒煎饼果⼦配⽅"
    def make_cake(self):
        self.__init__() # 执⾏本类的__init__⽅法，做属性初始化 self.kongfu = "猫⽒...."
        print("[猫⽒] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)
    def make_old_cake(self):
 # ⽅式1. 指定执⾏⽗类的⽅法
 # Master.__init__(self)
 # Master.make_cake(self)
 # ⽅法2. super() 带参数版本
 # super(Prentice, self).__init__() # 执⾏⽗类的 __init__⽅法
 # super(Prentice, self).make_cake()
 # ⽅法3. super()的简化版，只⽀持新式类
        super().__init__() # 执⾏⽗类的 __init__⽅法
        super().make_cake() # 执⾏⽗类的 实例⽅法
damao = Prentice()
damao.make_cake()
damao.make_old_cake()