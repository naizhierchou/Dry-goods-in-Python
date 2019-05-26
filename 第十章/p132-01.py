# 定义⼀个home类
class Home:
    def __init__(self, area):
       self.area = area #房间剩余的可⽤⾯积
       self.containsItem = []
    def __str__(self):
       msg = "当前房间可⽤⾯积为:" + str(self.area)
       if len(self.containsItem) > 0:
           msg = msg + " 容纳的物品有: "
           for temp in self.containsItem:
               msg = msg + temp.getName() + ", "
           msg = msg.strip(", ")
       return msg
    # 容纳物品
    def accommodateItem(self,item):
       # 如果可⽤⾯积⼤于物品的占⽤⾯积
       needArea = item.getUsedArea()
       if self.area > needArea:
          self.containsItem.append(item)
          self.area -= needArea
          print("ok:已经存放到房间中")
       else:
          print("err:房间可⽤⾯积为:%d,但是当前要存放的物品需要的⾯积为%d"%(self.area, needArea))
# 定义bed类
class Bed:
    def __init__(self,area,name = '床'):
       self.name = name
       self.area = area
    def __str__(self):
       msg = '床的⾯积为:' + str(self.area)
       return msg
 # 获取床的占⽤⾯积
    def getUsedArea(self):
       return self.area
    def getName(self):
       return self.name
# 创建⼀个新家对象
newHome = Home(100)#100平⽶
print(newHome)
# 创建⼀个床对象
newBed = Bed(20)
print(newBed)
# 把床安放到家⾥
newHome.accommodateItem(newBed)
print(newHome)
# 创建⼀个床对象
newBed2 = Bed(30,'席梦思')
print(newBed2)
# 把床安放到家⾥
newHome.accommodateItem(newBed2)
print(newHome)