i=0#内外循环的控制变量不能一样
while i<5:
    j=0#内循环的控制变量必须要在外循环里初始化
    while j<5:
        print("j=%d"%j)
        j+=1
    print("i=%d"%i)
    i+=1