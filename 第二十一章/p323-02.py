#coding=utf-8
# ############### 定义 ###############
class Goods:
     #"""python3中默认继承object类以python2、3执⾏此程序的结果不同，因为只有在python3中才有@xxx.setter@xxx.deleter"""
     @property
     def price(self):
        print('@property')
     @price.setter
     def price(self, value):
        print('@price.setter')
     @price.deleter
     def price(self):
        print('@price.deleter')
# ############### 调⽤ ###############
obj = Goods()
obj.price # ⾃动执⾏ @property 修饰的 price ⽅法，并获取⽅法的返回值
obj.price = 123 # ⾃动执⾏ @price.setter 修饰的 price ⽅法，并将 123 赋值给⽅法
#的参数
del obj.price # ⾃动执⾏ @price.deleter 修饰的 price ⽅法