from time import ctime, sleep
def timefun(func):
     def wrapped_func(a, b):
         print("%s called at %s" % (func.__name__, ctime()))
         print(a, b)
         func(a, b)
     return wrapped_func
@timefun
def foo(a, b):
    print(a+b)
foo(3,5)
sleep(2)
foo(2,4)