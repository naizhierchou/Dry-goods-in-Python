class Prentice(object):
    def __init__(self):
       self.kongfu = "猫⽒煎饼果⼦配⽅"
 # 私有属性，可以在类内部通过self调⽤，但不能通过对象访问
       self.__money = 10000
 # 私有⽅法，可以在类内部通过self调⽤，但不能通过对象访问
    def __print_info(self):
       print(self.kongfu)
       print(self.__money)
    def make_cake(self):
       self.__init__()
       print("[猫⽒] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)
class PrenticePrentice(Prentice):
    pass
damao = Prentice()
# 类的外⾯不能访问私有权限的属性和⽅法
# print(damao.__money)
# damao.__print_info()
pp = PrenticePrentice()
# ⼦类可以直接使⽤⽗类的公有属性和⽅法
pp.make_cake()
# ⼦类不能继承⽗类私有权限的属性和⽅法
print(pp.__money)
pp.__print_info()