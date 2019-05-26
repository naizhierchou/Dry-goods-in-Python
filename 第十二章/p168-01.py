#test.py
class Test(object):
    def test(self):
        print("-----Test类中的test函数")
def test1():
    print("------test1函数-----")
def test2():
    print("-----test2函数------")

#main.py
from test import *
a=Test()
a.test()
test1()
test2()