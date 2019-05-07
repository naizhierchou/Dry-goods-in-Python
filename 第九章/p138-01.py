class Hero:
    # """定义了⼀个英雄类"""
    def info(self):
        # """info 是⼀个实例⽅法，类对象可以调⽤实例⽅法，实例⽅法的第⼀个参数⼀定是self"""
        print("我帅的已经惊动了天地")
# 实例化了⼀个英雄对象 泰达⽶尔
taidamier = Hero()
# 给对象添加属性，以及对应的属性值
taidamier.name = "泰达⽶尔" # 姓名
taidamier.atk = 450 # 攻击⼒
# 通过.成员选择运算符，获取对象的属性值
print("英雄 %s 的攻击⼒ :%d" % (taidamier.name, taidamier.atk))