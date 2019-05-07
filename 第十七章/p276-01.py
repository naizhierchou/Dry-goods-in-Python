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
fib = fibonacci(5)
value = next(fib)
print(value)
value = next(fib)
print(value)
value = next(fib)
print(value)
# for value in fib:
# print(value)