class Hero:
    # """定义了⼀个英雄类，可以移动和攻击"""
    def __init__(self, name, skill, hp, atk, armor):
        # """ __init__() ⽅法，⽤来做变量初始化 或 赋值 操作"""
        # 英雄名
        self.name = name  # 实例变量
        # 技能
        self.skill = skill
        # ⽣命值：
        self.hp = hp  # 实例变量
        # 攻击⼒
        self.atk = atk
        # 护甲值
        self.armor = armor

    # def info(self):
    # print("英雄 %s 的⽣命值 :%d" % (self.name, self.hp))
    # print("英雄 %s 的攻击⼒ :%d" % (self.name, self.atk))
    # print("英雄 %s 的护甲值 :%d" % (self.name, self.armor))
    def __str__(self):
        # """
        # 这个⽅法是⼀个魔法⽅法 (Magic Method) ，⽤来显示信息
        # 该⽅法需要 return ⼀个数据，并且只有self⼀个参数，当在类的外部 print(对象) 则
        # 打印这个数据
        # """
        return "英雄 <%s> 数据： ⽣命值 %d, 攻击⼒ %d, 护甲值 %d" % (self.name,
                                                       self.hp, self.atk, self.armor)


taidamier = Hero("泰达⽶尔", "旋⻛斩", 2600, 450, 200)
gailun = Hero("盖伦", "⼤宝剑", 4200, 260, 400)
# 如果没有__str__ 则默认打印 对象在内存的地址。
# 当类的实例化对象 拥有 __str__ ⽅法后，那么打印对象则打印 __str__ 的返回值。
print(taidamier)
print(gailun)
