class Prentice(object):
    def __init__(self):
       self.kongfu = "猫⽒煎饼果⼦配⽅"
 # 私有属性，可以在类内部通过self调⽤，但不能通过对象访问
       self.__money = 10000
 # 现代软件开发中，通常会定义get_xxx()⽅法和set_xxx()⽅法来获取和修改私有属性值。
 # 返回私有属性的值
    def get_money(self):
       return self.__money
 # 接收参数，修改私有属性的值
    def set_money(self, num):
       self.__money = num
damao = Prentice()
# 对象不能访问私有权限的属性和⽅法
# print(damao.__money)
# damao.__print_info()
# 可以通过访问公有⽅法set_money()来修改私有属性的值
damao.set_money(100)
# 可以通过访问公有⽅法get_money()来获取私有属性的值
print(damao.get_money())