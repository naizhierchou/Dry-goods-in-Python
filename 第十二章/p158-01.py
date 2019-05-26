try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产⽣错误了:%s'%errorMsg)
else:
    print('没有捕获到异常，真⾼兴')

