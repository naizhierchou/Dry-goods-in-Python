# 求3个数的和
def sum3Number(a,b,c):
    return a+b+c # return 的后⾯可以是数值，也可是⼀个表达式
# 完成对3个数求平均值
def average3Number(a,b,c):
 # 因为sum3Number函数已经完成了3个数的就和，所以只需调⽤即可
 # 即把接收到的3个数，当做实参传递即可
    sumResult = sum3Number(a,b,c)
    aveResult = sumResult/3.0
    return aveResult
# 调⽤函数，完成对3个数求平均值
result = average3Number(11,2,55)
print("average is %d"%result)