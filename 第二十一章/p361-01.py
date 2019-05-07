class Province(object):
    country = 'China'

    def __init__(self, name, count):
        self.name = name

        self.count = count

    def func(self, *args, **kwargs):
        print('func')
    # 获取类的属性，即：类属性、⽅法、


print(Province.__dict__)
# 输出：{'__dict__': <attribute '__dict__' of 'Province' objects>, '__module__':'__main__', 'country': 'China', '__doc__': None, '__weakref__': < attribute'__weakref__'of'Province'
#objects >, 'func': < functionProvince.funcat0x101897950 >, '__init__': < functionProvince.__init__at0x1018978c8 >}
obj1 = Province('⼭东', 10000)
print(obj1.__dict__)
# 获取 对象obj1 的属性
# 输出：{'count': 10000, 'name': '⼭东'}
obj2 = Province('⼭⻄', 20000)
print(obj2.__dict__)
# 获取 对象obj1 的属性
# 输出：{'count': 20000, 'name': '⼭⻄'}