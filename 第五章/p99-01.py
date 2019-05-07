# 打印⼀条横线
def printOneLine():
    print("-"*30)
# 打印多条横线
def printNumLine(num):
    i=0
 # 因为printOneLine函数已经完成了打印横线的功能，
 # 只需要多次调⽤此函数即可
    while i<num:
        printOneLine()
        i+=1
printNumLine(3)