
test.py
# -*- coding:utf-8 -*-
class Person(object):
     def __init__(self):
        self.name = 'laowang'
main.py
from test import Person
obj = Person()
print(obj.__module__) # 输出 test 即：输出模块
print(obj.__class__) # 输出 test.Person 即：输出类