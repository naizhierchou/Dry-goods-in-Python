# 定义⼀个Master类
class Master(object):
    def __init__(self):
 # 属性
       self.kongfu = "古法煎饼果⼦配⽅"
 # 实例⽅法
    def make_cake(self):
       print("按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)
# 定义Prentice类，继承了 Master，则Prentice是⼦类，Master是⽗类。
class Prentice(Master):
 # ⼦类可以继承⽗类所有的属性和⽅法，哪怕⼦类没有⾃⼰的属性和⽅法，也可以使⽤⽗类的属性和⽅法。
    pass
damao = Prentice() # 创建⼦类实例对象
print(damao.kongfu) # ⼦类对象可以直接使⽤⽗类的属性
damao.make_cake() # ⼦类对象可以直接使⽤⽗类的⽅法