def counter(start=0):
     def incr():
         nonlocal start
         start += 1
         return start
     return incr
c1 = counter(5)
print(c1())
print(c1())
c2 = counter(50)
print(c2())
print(c2())
print(c1())
print(c1())
print(c2())
print(c2())