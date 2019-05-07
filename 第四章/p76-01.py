# 待查找的列表
nameList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
# 获取⽤户要查找的名字
findName = input('请输⼊要查找的姓名:')
# 查找是否存在
if findName in nameList:
    print('在字典中找到了相同的名字')
else:
    print('没有找到')