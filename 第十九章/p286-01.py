def test1():
 print("--- in test1 func----")
# 调⽤函数
test1()
# 引⽤函数
ret = test1
print(id(ret))
print(id(test1))
#通过引⽤调⽤函数
ret()