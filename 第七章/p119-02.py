def fun(a, b, opt):
    print("a = %d" % a)
    print("b = %d" % b)
    print("result =%d" % opt(a, b))


fun(1, 2, lambda x, y: x + y)
