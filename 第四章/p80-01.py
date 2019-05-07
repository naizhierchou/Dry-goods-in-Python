import random
# 定义⼀个列表⽤来保存3个办公室
offices = [[],[],[]]
# 定义⼀个列表⽤来存储8位⽼师的名字
names = ['A','B','C','D','E','F','G','H']
i = 0
for name in names:

    index = random.randint(0,2)
    offices[index].append(name)
i = 1
for tempNames in offices:

    print('办公室%d的⼈数为:%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:

        print("%s"%name,end='')
        print("\n")
        print("-"*20)