class Hero(object):
 # 初始化⽅法
 # 创建完对象后会⾃动被调⽤
    def __init__(self, name):
       print('__init__⽅法被调⽤')
       self.name = name
 # 当对象被删除时，会⾃动被调⽤
    def __del__(self):
       print("__del__⽅法被调⽤")
       print("%s 被 GM ⼲掉了..." % self.name)
# 创建对象
taidamier = Hero("泰达⽶尔")
# 删除对象
print("%d 被删除1次" % id(taidamier))
del(taidamier)
print("--" * 10)
gailun = Hero("盖伦")
gailun1 = gailun
gailun2 = gailun
print("%d 被删除1次" % id(gailun))
del(gailun)
print("%d 被删除1次" % id(gailun1))
del(gailun1)
print("%d 被删除1次" % id(gailun2))
del(gailun2)