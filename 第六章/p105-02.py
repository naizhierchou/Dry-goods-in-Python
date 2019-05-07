 def create_nums(num):
     print("---1---")
     if num == 100:
        print("---2---")
        return num+1 # 函数中下⾯的代码不会被执⾏，因为return除了能够将数据返回
之外，还有⼀个隐藏的功能：结束函数
     else:
        print("---3---")
        return num+2
     print("---4---")
 result1 = create_nums(100)
 print(result1) # 打印101
 result2 = create_nums(200)
 print(result2)  # 打印202