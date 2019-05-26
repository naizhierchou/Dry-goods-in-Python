def test1(b): # 变量b⼀定是⼀个局部变量，就看它指向的是谁，可变还是不可变
    b += b
    # b = b+b
    print(b)
# a = [11, 22]
a = 100
test1(a)
print(a)