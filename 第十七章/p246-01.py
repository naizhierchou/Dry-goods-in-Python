from collections import Iterable
# ⾃定义可迭代对象: 在类⾥⾯定义__iter__⽅法创建的对象就是可迭代对象
class MyList(object):
     def __init__(self):
        self.my_list = list()
     # 添加指定元素
     def append_item(self, item):
        self.my_list.append(item)
     def __iter__(self):
        # 可迭代对象的本质：遍历可迭代对象的时候其实获取的是可迭代对象的迭代器， 然后通过迭
        #代器获取对象中的数据
        pass
my_list = MyList()
my_list.append_item(1)
my_list.append_item(2)
result = isinstance(my_list, Iterable)
print(result)
for value in my_list:
    print(value)