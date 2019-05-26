# ⽗类
class A(object):
   def __init__(self):
       self.num = 10
   def print_num(self):
       print(self.num + 10)
# ⼦类
class B(A):
   pass
b = B()
print(b.num)
b.print_num()