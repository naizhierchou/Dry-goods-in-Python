f = open('test.txt', 'r')
content = f.readlines()
print(type(content))
i=1
for temp in content:
    print("%d:%s" % (i, temp))
    i += 1
f.close()