import copy
a = [11,22,33]
b = copy.copy(a)
id(a)

id(b)


a.append(44)
a

b

a = (11,22,33)
b = copy.copy(a)
id(a)
id(b)
