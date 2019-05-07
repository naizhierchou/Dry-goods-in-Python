def inner():
    #验证 1
    #验证 2
    #验证 3
    f1() # func是参数，此时 func 等于 f1
    return inner# 返回的 inner，inner代表的是函数，⾮执⾏函数 ,其实就是将原来的 f1 函
#数塞进另外⼀个函数中