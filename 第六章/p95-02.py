def printinfo(name, age=35):
 # 打印任何传⼊的字符串
    print("name: %s" % name)
    print("age %d" % age)
# 调⽤printinfo函数
printinfo(name="miki") # 在函数执⾏过程中 age去默认值35
printinfo(age=9 ,name="miki")