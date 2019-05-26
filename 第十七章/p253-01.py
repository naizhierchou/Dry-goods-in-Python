def fibonacci(num):
     a = 0
     b = 1
     # 记录⽣成fibonacci数字的下标
     current_index = 0
     print("--11---")
     while current_index < num:
         result = a
         a, b = b, a + b
         current_index += 1
         print("--22---")
         # 代码执⾏到yield会暂停，然后把结果返回出去，下次启动⽣成器会在暂停的位置继续往下执⾏
         yield result
         print("--33---")
         return "嘻嘻"
fib = fibonacci(5)
value = next(fib)
print(value)
# 提示： ⽣成器⾥⾯使⽤return关键字语法上没有问题，但是代码执⾏到return语句会停⽌迭代，抛出停
#⽌迭代异常
# 在python3⾥⾯可以使⽤return关键字，python2不⽀持
# return 和 yield的区别
# yield: 每次启动⽣成器都会返回⼀个值，多次启动可以返回多个值，也就是yield可以返回多个值
# return: 只能返回⼀次值，代码执⾏到return语句就停⽌迭代
try:
     value = next(fib)
     print(value)
except StopIteration as e:
     # 获取return的返回值
     print(e.value)