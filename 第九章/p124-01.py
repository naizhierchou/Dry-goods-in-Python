class Hero:
    # """定义了⼀个英雄类，可以移动和攻击"""
    def move(self):
        # """实例⽅法"""
        print("正在前往事发地点...")

    def attack(self):
        # """实例⽅法"""
        print("发出了⼀招强⼒的普通攻击...")

    def info(self):
        # """在类的实例⽅法中，通过self获取该对象的属性"""
        print("英雄 %s 的⽣命值 :%d" % (self.name, self.hp))
        print("英雄 %s 的攻击⼒ :%d" % (self.name, self.atk))
        print("英雄 %s 的护甲值 :%d" % (self.name, self.armor))


# 实例化了⼀个英雄对象 泰达⽶尔
taidamier = Hero()
# 给对象添加属性，以及对应的属性值
taidamier.name = "泰达⽶尔"  # 姓名
taidamier.hp = 2600  # ⽣命值
taidamier.atk = 450  # 攻击⼒
taidamier.armor = 200  # 护甲值
# 通过.成员选择运算符，获取对象的实例⽅法
taidamier.info()  # 只需要调⽤实例⽅法info()，即可获取英雄的属性
taidamier.move()
taidamier.attack()
