a=[11,22]
b=[33,44]
c=[a,b]
id(a)
id(b)
id(c)
import copy
d=copy.copy(c)
id(d)
id(d[0])
id(d[1])
a.append(11)
c
d