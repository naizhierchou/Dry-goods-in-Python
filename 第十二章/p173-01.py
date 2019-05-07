try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            print(content)
    finally:
        f.close()
        print('关闭⽂件')
except:
    print("⽂件读取出错")