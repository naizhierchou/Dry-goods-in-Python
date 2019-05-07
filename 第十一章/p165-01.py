class A(object):
    def __init__(self):
        print("这是 init ⽅法")
    def __new__(cls):
        print("这是 new ⽅法")
        return object.__new__(cls)
A()