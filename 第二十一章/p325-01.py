class Foo:
     def get_bar(self):
        return 'laotie'
     BAR = property(get_bar)
obj = Foo()
reuslt = obj.BAR # ⾃动调⽤get_bar⽅法，并获取⽅法的返回值
print(reuslt)