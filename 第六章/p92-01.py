g_num = 0
def test1():
    global g_num
    # 将处理结果存储到全局变量g_num中.....
    g_num = 100
def test2():
    # 通过获取全局变量g_num的值, 从⽽获取test1函数处理之后的结果
    print(g_num)
# 1. 先调⽤test1得到数据并且存到全局变量中
test1()
# 2. 再调⽤test2，处理test1函数执⾏之后的这个值
test2()