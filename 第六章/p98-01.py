# 第1种⽅式,使⽤中间变量
# a = 4
# b = 5
# c = 0
#
# c = a
# a = b
# b = c
#
# print(a)
# print(b)
# 第2种⽅式，直接交换。
a, b = 4, 5
a, b = b, a # 实际上这⼀步⾥既有打包，也有拆包
print(a)
print(b)