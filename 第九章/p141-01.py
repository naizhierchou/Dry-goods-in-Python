class Hero:
 #"""定义了⼀个英雄类，可以移动和攻击"""
    def __init__(self, name, skill, hp, atk, armor):
 #""" __init__() ⽅法，⽤来做变量初始化 或 赋值 操作"""
 # 英雄名
       self.name = name
 # 技能
       self.skill = skill
 # ⽣命值：
       self.hp = hp
 # 攻击⼒
       self.atk = atk
 # 护甲值
       self.armor = armor
    def move(self):
 #"""实例⽅法"""
       print("%s 正在前往事发地点..." % self.name)
    def attack(self):
 #"""实例⽅法"""
       print("发出了⼀招强⼒的%s..." % self.skill)
    def info(self):
       print("英雄 %s 的⽣命值 :%d" % (self.name, self.hp))
       print("英雄 %s 的攻击⼒ :%d" % (self.name, self.atk))
       print("英雄 %s 的护甲值 :%d" % (self.name, self.armor))
# 实例化英雄对象时，参数会传递到对象的__init__()⽅法⾥
taidamier = Hero("泰达⽶尔", "旋⻛斩", 2600, 450, 200)
gailun = Hero("盖伦", "⼤宝剑", 4200, 260, 400)
# 不同对象的属性值的单独保存
print(taidamier.name)
print(gailun.name)