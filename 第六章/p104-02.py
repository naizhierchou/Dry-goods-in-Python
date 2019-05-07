def test1():
 # 通过return将⼀个数据结果返回
    return 50
def test2(num):
 # 通过形参的⽅式保存传递过来的数据，就可以处理了
    print(num)
# 1. 先调⽤test1得到数据并且存到变量result中
result = test1()
# 2. 调⽤test2时，将result的值传递到test2中，从⽽让这个函数对其进⾏处理
test2(result)