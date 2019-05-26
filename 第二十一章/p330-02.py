# -*- coding:utf-8 -*-
class Foo(object):
     def __getitem__(self, key):
         print('__getitem__', key)

     def __setitem__(self, key, value):
         print('__setitem__', key, value)

     def __delitem__(self, key):
         print('__delitem__', key)


obj = Foo()
result = obj['k1']  # ⾃动触发执⾏ __getitem__
obj['k2'] = 'laotie'  # ⾃动触发执⾏ __setitem__
del obj['k1']  # ⾃动触发执⾏ __delitem__