class Hero:


# """定义了⼀个英雄类"""
# Python 的类⾥提供的，两个下划线开始，两个下划线结束的⽅法，就是魔法⽅法，__init__()就是⼀个魔法⽅法，通常⽤来做属性初始化或赋值操作。
# 如果类⾯没有写__init__⽅法，Python会⾃动创建，但是不执⾏任何操作，
# 如果为了能够在完成⾃⼰想要的功能，可以⾃⼰定义__init__⽅法，
# 所以⼀个类⾥⽆论⾃⼰是否编写__init__⽅法 ⼀定有__init__⽅法。
   def __init__(self):


    #""" ⽅法，⽤来做变量初始化 或 赋值 操作，在类实例化对象的时候，会被⾃动调⽤"""
      self.name = "泰达⽶尔"  # 姓名
      self.hp = 2600  # ⽣命值
      self.atk = 450  # 攻击⼒
      self.armor = 200  # 护甲值


   def info(self):


    #"""在类的实例⽅法中，通过self获取该对象的属性"""
      print("英雄 %s 的⽣命值 :%d" % (self.name, self.hp))
      print("英雄 %s 的攻击⼒ :%d" % (self.name, self.atk))
      print("英雄 %s 的护甲值 :%d" % (self.name, self.armor))
# 实例化了⼀个英雄对象，并⾃动调⽤__init__()⽅法
taidamier = Hero()
# 通过.成员选择运算符，获取对象的实例⽅法
taidamier.info()  # 只需要调⽤实例⽅法info()，即可获取英雄的属性
