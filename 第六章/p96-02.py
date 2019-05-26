def fun(a, b, *args, **kwargs):
#"""可变参数演示示例"""
    print("a =%d" % a)
    print("b =%d" % b)
    print("args:")
    print(args)
    print("kwargs: %s" % kwargs)

fun(1, 2, 3, 4, 5, m=6, n=7, p=8) # 注意传递的参数对应