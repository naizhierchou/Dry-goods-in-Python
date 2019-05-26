class Master(object):
    def __init__(self):
       self.kongfu = "古法煎饼果⼦配⽅"
    def make_cake(self):
       print("[古法] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)

class Prentice(Master):
     def __init__(self):
         self.kongfu = "猫⽒煎饼果⼦配⽅"

     def make_cake(self):
         print("[猫⽒] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)

 # 如果⼦类和⽗类的⽅法名和属性名相同，则默认使⽤⼦类的
 # 叫 ⼦类重写⽗类的同名⽅法和属性
damao = Prentice()
print(damao.kongfu)  # ⼦类和⽗类有同名属性，则默认使⽤⼦类的
damao.make_cake()  # ⼦类和⽗类有同名⽅法，则默认使⽤⼦类的
 # ⼦类的魔法属性__mro__决定了属性和⽅法的查找顺序
print(Prentice.__mro__)