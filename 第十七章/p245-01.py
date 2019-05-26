# 元组，列表，字典，字符串，集合，range都是可迭代对象
from collections import Iterable
# 判断对象是否是指定类型
result = isinstance((3, 5), Iterable)
print("元组是否是可迭代对象:", result)
result = isinstance([3, 5], Iterable)
print("列表是否是可迭代对象:", result)
result = isinstance({"name": "张三"}, Iterable)
print("字典是否是可迭代对象:", result)
result = isinstance("hello", Iterable)
print("字符串是否是可迭代对象:", result)
result = isinstance({3, 5}, Iterable)
print("集合是否是可迭代对象:", result)
result = isinstance(range(5), Iterable)
print("range是否是可迭代对象:", result)
result = isinstance(5, Iterable)
print("整数是否是可迭代对象:", result)
# 提示: 以后还根据对象判断是否是其它类型，⽐如以后可以判断函数⾥⾯的参数是否是⾃⼰想要的类型
result = isinstance(5, int)
print("整数是否是int类型对象:", result)
class Student(object):
    pass
stu = Student()
result = isinstance(stu, Iterable)
print("stu是否是可迭代对象:", result)
result = isinstance(stu, Student)
print("stu是否是Student类型的对象:", result)