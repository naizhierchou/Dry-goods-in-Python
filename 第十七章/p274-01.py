class Fibonacci(object):
     def __init__(self, num):
         # num:表示⽣成多少fibonacci数字
         self.num = num
         # 记录fibonacci前两个值
         self.a = 0
         self.b = 1
         # 记录当前⽣成数字的索引
         self.current_index = 0
     def __iter__(self):
        return self
     def __next__(self):
         if self.current_index < self.num:
             result = self.a
             self.a, self.b = self.b, self.a + self.b
             self.current_index += 1
             return result
         else:
             raise StopIteration
fib = Fibonacci(5)
# value = next(fib)
# print(value)
for value in fib:
    print(value)