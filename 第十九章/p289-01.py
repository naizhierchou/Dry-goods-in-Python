def counter(start=0):
     count=[start]
     def incr():
         count[0] += 1
         return count[0]
     return incr
c1 = closeure.counter(5)
print(c1()) # 6
print(c1()) # 7
c2 = closeure.counter(100)
print(c2()) # 101
print(c2()) # 102