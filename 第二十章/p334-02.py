import copy
a=[11,22]
b=[33,44]
c=[a,b]
d=copy.deepcopy(c)
id(a)
id(b)
id(c)
id(c[0])
id(c[1])
id(d[0])
id(d[1])
id(d)
c[0].append(55)
c
d