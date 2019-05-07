#### 第⼀波 ####
def foo():
    print('foo')
foo # 表示是函数
foo() # 表示执⾏foo函数
#### 第⼆波 ####
def foo():
    print('foo')


foo = lambda x: x + 1
foo()  # 执⾏lambda表达式，⽽不再是原来的foo函数，因为foo这个名字被重新指向了另外⼀个匿名函数