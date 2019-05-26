i=10
while i>0:
    print("妈，还要我刷啊")
    if i==5:
        print("好了不用刷了")
        i-=1#continue之前要注意修改i的值，否则容易导致死循环
        continue
    print ("正在刷%d个碗"%i)
    i-=1
print("程序结束")