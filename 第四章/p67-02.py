# 定义变量A，默认有3个元素
A = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
print("-----添加之前，列表A的数据-----A=%s" % A)
# 提示、并添加元素
temp = input('请输⼊要添加的学⽣姓名:')
A.append(temp)
print("-----添加之后，列表A的数据-----A=%s" % A)