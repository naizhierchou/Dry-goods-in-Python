def divid(a, b):
    shang = a//b
    yushu = a%b
    return shang, yushu #默认是元组
result = divid(5, 2)
print(result) # 输出(2, 1)