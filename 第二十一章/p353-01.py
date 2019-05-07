# ############### 定义 ###############
class Foo:
     def func(self):
        pass
     # 定义property属性
     @property
     def prop(self):
        pass
# ############### 调⽤ ###############
foo_obj = Foo()
foo_obj.func() # 调⽤实例⽅法
foo_obj.prop # 调⽤property属性