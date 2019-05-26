# 定义⼀个函数
def test(number):
 # 在函数内部再定义⼀个函数，并且这个函数⽤到了外边函数的变量，那么将这个函数以及⽤到的⼀
#些变量称之为闭包
def test_in(number_in):
    print("in test_in 函数, number_in is %d" % number_in)

    return number + number_in
 # 其实这⾥返回的就是闭包的结果
return test_in
 # 给test函数赋值，这个20就是给参数number


ret = test(20)
# 注意这⾥的100其实给参数number_in
print(ret(100))
# 注 意这⾥的200其实给参数number_in
print(ret(200))