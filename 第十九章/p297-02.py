from time import ctime, sleep
def timefun(func):
     def wrapped_func(*args, **kwargs):
         print("%s called at %s"%(func.__name__, ctime()))
         func(*args, **kwargs)
     return wrapped_func@timefun
def foo(a, b, c):
    print(a+b+c)
foo(3,5,7)
sleep(2)
foo(2,4,9)