try:
    print('-----test--1---')
    open('123.txt','r') # 如果123.txt⽂件不存在，那么会产⽣ IOError 异常
    print('-----test--2---')
    print(num)# 如果num变量没有定义，那么会产⽣ NameError 异常
except (IOError,NameError):
    #如果想通过⼀次except捕获到多个异常可以⽤⼀个元组的⽅式
    pass
