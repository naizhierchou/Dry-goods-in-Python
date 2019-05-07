import copy
a=[11,22]
b=[33,44]
c=(a,b)
d=copy.copy(c)
id(c)
id(d)
a.append(33)
c
d
e=copy.deepcopy(c)
id(c)
id(e)
a.append(44)
c
e