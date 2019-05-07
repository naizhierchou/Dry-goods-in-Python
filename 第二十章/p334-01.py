import copy
a=[11,22]
b=copy.deepcopy(a)
a
b
id(a)
id(b)
#以上结果说明了通过deepcopy确实将a列表中所有的数据引用copy了，而不是只copy了a指向的列表的引用
a.append(33)
a
b