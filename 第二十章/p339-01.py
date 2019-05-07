import copy
a=[11,22]
b=[a]
c=[b]
d=copy.deepcopy(c)
c
d
id(c)
id(d)
id(c[0])
id(d[0])
a
a.append(33)
a
c
d
