# 批量在⽂件名前加前缀
import os
funFlag = 1 # 1表示添加标志 2表示删除标志
folderName = './renameDir/'
# 获取指定路径的所有⽂件名字
dirList = os.listdir(folderName)
# 遍历输出所有⽂件名字
for name in dirList:
    print(name)
    if funFlag == 1:
        newName = '[佐哥出品]-' + name
    elif funFlag == 2:
        num = len('[佐哥出品]-')
        newName = name[num:]
    print(newName)
    os.rename(folderName+name, folderName+newName)