f = open('test.txt', 'r')
content = f.read(5) # 最多读取5个数据
print(content)
print("-"*30) # 分割线，⽤来测试
content = f.read() # 从上次读取的位置继续读取剩下的所有的数据
print(content)
f.close() # 关闭⽂件，这个可是个好习惯哦