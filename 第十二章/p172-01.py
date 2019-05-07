try:
        f = open('test.txt')
        try:
            while True:
                content = f.readline()
                if len(content) == 0:
                    break
                print(content)
        except:
 #如果在读取⽂件的过程中，产⽣了异常，那么就会捕获到
 #⽐如 按下了 ctrl+c
            pass
        finally:
            f.close()
            print('关闭⽂件')
except:
        print("没有这个⽂件")