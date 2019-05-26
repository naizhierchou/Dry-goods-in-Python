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
        my_iterator = MyIterator(self.my_list)
        return my_iterator


# ⾃定义迭代器对象: 在类⾥⾯定义__iter__和__next__⽅法创建的对象就是迭代器对象
# 迭代器是记录当前数据的位置以便获取下⼀个位置的值
class MyIterator(object):
    def __init__(self, my_list):
        self.my_list = my_list

    # 记录当前获取数据的下标
        self.current_index = 0

    def __iter__(self):
        return self

    # 获取迭代器中下⼀个值
    def __next__(self):
        if self.current_index < len(self.my_list):
            self.current_index += 1

            return self.my_list[self.current_index - 1]
        else:
    # 数据取完了，需要抛出⼀个停⽌迭代的异常
            raise StopIteration


# 创建了⼀个⾃定义的可迭代对象
my_list = MyList()
my_list.append_item(1)
my_list.append_item(2)
# 获取可迭代对象的迭代器
my_iterator = iter(my_list)
print(my_iterator)
# 获取迭代器中下⼀个值
# value = next(my_iterator)
# print(value)
# 循环通过迭代器获取数据
while True:
    try:
        value = next(my_iterator)
        print(value)
    except StopIteration as e:
        break