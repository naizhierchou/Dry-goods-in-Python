class Hero:# 新式类定义形式
    def info(self):
 #"""info 是⼀个实例⽅法，类对象可以调⽤实例⽅法，实例⽅法的第⼀个参数⼀定是self"""
       print("我帅的已经惊动了天地")
# Hero这个类 实例化了⼀个对象 taidamier(泰达⽶尔)
taidamier = Hero()
# 对象调⽤实例⽅法info()，执⾏info()⾥的代码
# . 表示选择属性或者⽅法
taidamier.info()