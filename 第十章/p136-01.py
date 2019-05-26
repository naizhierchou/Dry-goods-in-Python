class Master(object):
    def __init__(self):
       self.kongfu = "古法煎饼果⼦配⽅" # 实例变量，属性
    def make_cake(self): # 实例⽅法，⽅法
       print("[古法] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)
    def dayandai(self):
       print("师傅的⼤烟袋..")
class School(object):
    def __init__(self):
       self.kongfu = "现代煎饼果⼦配⽅"
    def make_cake(self):
       print("[现代] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)
    def xiaoyandai(self):
       print("学校的⼩烟袋..")
# class Prentice(School, Master): # 多继承，继承了多个⽗类（School在前）
# pass
class Prentice(Master, School): # 多继承，继承了多个⽗类（Master在前）
    pass
damao = Prentice()
print(damao.kongfu) # 执⾏Master的属性
damao.make_cake() # 执⾏Master的实例⽅法
# ⼦类的魔法属性__mro__决定了属性和⽅法的查找顺序
print(Prentice.__mro__)
damao.dayandai() # 不重名不受影响
damao.xiaoyandai()
School.make_cake(damao) # 重名，可以强制指定执⾏某⼀个⽗类的⽅法。需要我们⾃⼰为 self传值。